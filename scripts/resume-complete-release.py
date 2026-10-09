#!/usr/bin/env python3
"""Veröffentlicht ausschließlich ein fest dokumentiertes, vollständig geprüftes Build-Artefakt."""

import argparse
import importlib.util
import json
import os
from pathlib import Path
import subprocess

from release_asset_common import expected_asset_metadata, read_checksums, sha256_file
import release_routing as R

SCRIPTS = Path(__file__).resolve().parent
CONFIG = SCRIPTS / 'data/complete-release-artifact-v445.35.3.json'
spec = importlib.util.spec_from_file_location('recovery_publisher', SCRIPTS / 'publish-release-assets.py')
PUBLISH = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PUBLISH)


def api(repo, resource):
    return json.loads(subprocess.check_output(['gh', 'api', f'repos/{repo}/{resource}'], text=True, timeout=60))


def verify_run(config, run, jobs, artifact, tag_sha):
    if (run.get('id') != config['run_id'] or run.get('head_sha') != config['source_commit']
            or run.get('repository', {}).get('full_name') != config['repo']
            or run.get('head_repository', {}).get('full_name') != config['repo']
            or run.get('path') != '.github/workflows/release-plugin-zips.yml'
            or run.get('event') != 'workflow_dispatch' or run.get('head_branch') != 'main'
            or run.get('status') != 'completed' or run.get('conclusion') != 'failure'
            or tag_sha != config['source_commit']):
        raise ValueError('Quelllauf, Repository oder unveränderlicher Release-Tag stimmen nicht überein')
    if jobs.get('total_count') != 1 or len(jobs.get('jobs', [])) != 1:
        raise ValueError('Unerwarteter Jobbestand')
    job = jobs['jobs'][0]
    steps = job.get('steps', [])
    required = config['required_steps']
    if (job.get('name') != 'build-and-release' or job.get('conclusion') != 'failure'
            or [s['name'] for s in steps[:len(required)]] != required
            or any(s.get('conclusion') != 'success' for s in steps[:len(required)])
            or [(s['name'], s.get('conclusion')) for s in steps if s.get('conclusion') == 'failure']
                != [('Beide Releases hochladen, verifizieren und geordnet veröffentlichen', 'failure')]
            or not any(s['name'] == 'Artefakte hochladen (immer)' and s.get('conclusion') == 'success' for s in steps)):
        raise ValueError('Nicht alle Build- und Paketprüfungen bestanden')
    if (artifact.get('id') != config['artifact_id'] or artifact.get('name') != 'plugin-zips'
            or artifact.get('expired') is not False or artifact.get('digest') != config['artifact_digest']
            or artifact.get('size_in_bytes') != config['artifact_bytes']
            or artifact.get('workflow_run', {}).get('id') != config['run_id']
            or artifact.get('workflow_run', {}).get('head_sha') != config['source_commit']):
        raise ValueError('Artefakt stammt nicht aus dem festgelegten geprüften Build')


def inspect(config):
    repo = config['repo']
    verify_run(config, api(repo, f"actions/runs/{config['run_id']}"),
               api(repo, f"actions/runs/{config['run_id']}/jobs?per_page=100"),
               api(repo, f"actions/artifacts/{config['artifact_id']}"),
               PUBLISH.tag_commit(repo, config['tag']))
    values = {'sha': config['source_commit'], 'artifact_id': config['artifact_id'], 'run_id': config['run_id']}
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
            for key, value in values.items():
                output.write(f'{key}={value}\n')
    print(json.dumps(values))


def restore(config, artifact_root, source, staging):
    head = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
    if head != config['source_commit'] or R.marketplace_version(source) != config['tag'][1:]:
        raise ValueError('Quellcheckout stimmt nicht mit dem geprüften Tag überein')
    manifests = {}
    for relative, expected in config['checksums'].items():
        path = artifact_root / relative
        if path.is_symlink() or not path.is_file() or path.stat().st_size != expected['size'] or sha256_file(path) != expected['sha256']:
            raise ValueError(f'Gesicherte Prüfsummenliste verändert: {relative}')
        manifests[relative] = read_checksums(path)
    hashes = manifests['dist/checksums-sha256.txt']
    expected_files = set(config['checksums']) | {f'dist/{name}' for name in hashes}
    paths = list(artifact_root.rglob('*'))
    if any(p.is_symlink() for p in paths) or {p.relative_to(artifact_root).as_posix() for p in paths if p.is_file()} != expected_files:
        raise ValueError('Artefakt enthält fehlende, fremde oder verknüpfte Dateien')
    if len(hashes) != config['dist_hashed_assets']:
        raise ValueError('Unvollständiger Gesamtbestand')
    for name, digest in hashes.items():
        if sha256_file(artifact_root / 'dist' / name) != digest:
            raise ValueError(f'Paketbytes verändert: {name}')
    groups = R.companion_case_groups(R.companion_cases(root=source, config=source / 'scripts/release-routes.json'))
    expected_groups = {R.companion_stage(n): R.companion_asset_names(slugs) for n, slugs in enumerate(groups, 1)}
    expected_groups['main'] = set(hashes) - set().union(*expected_groups.values())
    if set(expected_groups) != set(config['group_assets_including_checksums']):
        raise ValueError('Unerwartete Releaseaufteilung')
    for group, names in expected_groups.items():
        saved = manifests[f'release-staging/{group}/checksums-sha256.txt']
        if (set(saved) != names or len(saved) + 1 != config['group_assets_including_checksums'][group]
                or any(hashes.get(name) != digest for name, digest in saved.items())):
            raise ValueError(f'Unvollständige oder abweichende Gruppe: {group}')
    # Erst nach vollständiger Herkunfts-, Hash- und Bestandsprüfung Staging erzeugen.
    staging.mkdir()
    for group, names in expected_groups.items():
        directory = staging / group
        directory.mkdir()
        for name in sorted(names):
            os.link(artifact_root / 'dist' / name, directory / name)
        (directory / 'checksums-sha256.txt').write_bytes((artifact_root / f'release-staging/{group}/checksums-sha256.txt').read_bytes())
        expected_asset_metadata(directory)
    print(f'{len(hashes)} unveränderte Paketdateien geprüft; Staging vollständig')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('inspect', 'restore', 'publish'))
    parser.add_argument('--artifact-root', type=Path)
    parser.add_argument('--source', type=Path)
    parser.add_argument('--staging', type=Path)
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text())
    if args.command == 'inspect':
        inspect(config)
    elif args.command == 'restore':
        restore(config, args.artifact_root, args.source, args.staging)
    else:
        PUBLISH.publish(args.staging, config['tag'], config['repo'], root=args.source,
                        config=args.source / 'scripts/release-routes.json')


if __name__ == '__main__':
    main()
