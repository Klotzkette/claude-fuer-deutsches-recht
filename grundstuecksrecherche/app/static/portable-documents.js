/* Offline documents. Load the two vendor IIFEs and generated templates first. */
(function (root) {
  'use strict';
  const own = (object, key) => Object.prototype.hasOwnProperty.call(object, key);
  const encoder = new TextEncoder();
  const docxType = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';
  const fail = (path, reason) => { throw new Error(`${path}: ${reason}`); };
  const templates = () => {
    const data = root.PortableDocumentTemplates;
    if (!data || data.version !== 1) fail('Vorlagen', 'Die lokalen Dokumentvorlagen fehlen oder sind inkompatibel.');
    return data;
  };
  const object = (value) => value !== null && typeof value === 'object' && !Array.isArray(value);
  const truth = (value) => Array.isArray(value) ? value.length > 0 : object(value) ? Object.keys(value).length > 0 : Boolean(value);
  const whitespace = '[\\t\\n\\r\\f\\v \\u001c-\\u001f\\u0085\\u00a0\\u1680\\u2000-\\u200a\\u2028\\u2029\\u202f\\u205f\\u3000]';
  const pyStrip = (text) => text.replace(new RegExp(`^${whitespace}+|${whitespace}+$`, 'gu'), '');
  const fold = (text, data) => Array.from(text, (char) => own(data.casefold, char) ? data.casefold[char] : char.toLowerCase()).join('');
  const pyString = (value) => {
    if (value === null) return 'None';
    if (typeof value === 'boolean') return value ? 'True' : 'False';
    if (typeof value === 'number' && value !== 0 && Math.abs(value) < 0.0001) {
      return value.toExponential().replace(/e(-?)(\d)$/, 'e$10$2');
    }
    return String(value);
  };
  const escapeHTML = (text) => String(text).replace(/[&<>"']/g, (char) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#x27;' })[char]);

  // A closed interpreter for build-time template data, not JavaScript or Python eval.
  function render(data, name, args) {
    function assign(target, value, scope) {
      if (target[0] === 'name') scope[target[1]] = value;
      else if (target[0] === 'list') target[1].forEach((item, index) => assign(item, value[index], scope));
      else fail('Vorlagen', 'Unbekanntes Zuweisungsziel.');
    }
    function call(name, args, scope) {
      if (own(data.functions, name)) {
        const fn = data.functions[name];
        const local = Object.assign(Object.create(null), data.constants);
        fn.args.forEach((key, index) => { local[key] = args[index]; });
        return statements(fn.body, local)?.value;
      }
      if (name === 'v' && own(scope, name)) return scope[name](...args);
      switch (name) {
        case 'str': return pyString(args[0]);
        case 'len': return typeof args[0] === 'string' ? Array.from(args[0]).length : args[0].length;
        case 'isinstance': return args[1] === 'str' && typeof args[0] === 'string';
        case 'all': return args[0].every(truth);
        case 'list': case 'tuple': return [...args[0]];
        case 'enumerate': return args[0].map((value, index) => [index + (args[1] || 0), value]);
        case '_Draft': return { id: args[0], title: args[1], blocks: args[2] };
        case 'escape': return escapeHTML(args[0]);
        default: return fail('Vorlagen', 'Unbekannte Funktion.');
      }
    }
    function expr(node, scope) {
      const [op, a, b, c] = node;
      const ev = (value) => expr(value, scope);
      switch (op) {
        case 'literal': return a;
        case 'name': return own(scope, a) ? scope[a] : a === 'str' ? 'str' : fail('Vorlagen', 'Unbekannter Name.');
        case 'list': return a.map(ev);
        case 'dict': return Object.fromEntries(a.map(([key, value]) => [ev(key), ev(value)]));
        case 'text': return a.map(ev).join('');
        case 'string': return pyString(ev(a));
        case 'add': { const left = ev(a), right = ev(b); return Array.isArray(left) ? left.concat(right) : left + right; }
        case 'not': return !truth(ev(a));
        case 'and': case 'or': {
          let value;
          for (const item of a) { value = ev(item); if (truth(value) === (op === 'or')) break; }
          return value;
        }
        case 'choose': return ev(truth(ev(a)) ? b : c);
        case 'compare': {
          const left = ev(b), right = ev(c);
          if (a === 'Eq' || a === 'Is') return left === right;
          if (a === 'NotEq') return left !== right;
          if (a === 'In' || a === 'NotIn') return right.includes(left) === (a === 'In');
          return fail('Vorlagen', 'Unbekannter Vergleich.');
        }
        case 'item': case 'field': {
          const value = ev(a), key = op === 'field' ? b : ev(b);
          return own(value, key) ? value[key] : fail('Vorlagen', 'Fehlender Vorlagenwert.');
        }
        case 'call': return call(a, b.map(ev), scope);
        case 'lambda': return (...args) => {
          const local = Object.assign(Object.create(null), scope);
          a.forEach((key, index) => { local[key] = args[index]; });
          return expr(b, local);
        };
        case 'map': return ev(b).map((value) => {
          const local = Object.assign(Object.create(null), scope);
          assign(a, value, local); return expr(c, local);
        });
        case 'method': {
          const value = ev(a), args = c.map(ev);
          switch (b) {
            case 'get': return own(value, args[0]) ? value[args[0]] : args.length > 1 ? args[1] : null;
            case 'strip': return pyStrip(value);
            case 'rstrip': return value.replace(new RegExp(`${whitespace}+$`, 'gu'), '');
            case 'casefold': return fold(value, data);
            case 'isdigit': return value.length > 0 && Array.from(value).every((char) => data.digits.includes(char));
            case 'startswith': return value.startsWith(args[0]);
            case 'endswith': return (Array.isArray(args[0]) ? args[0] : [args[0]]).some((suffix) => value.endsWith(suffix));
            case 'join': return args[0].join(value);
            case 'items': return Object.entries(value);
            case 'append': value.push(args[0]); return null;
            case 'extend': value.push(...args[0]); return null;
            case 'insert': value.splice(args[0], 0, args[1]); return null;
            default: return fail('Vorlagen', 'Unbekannte Methode.');
          }
        }
        default: return fail('Vorlagen', 'Unbekannter Ausdruck.');
      }
    }
    function statements(nodes, scope) {
      for (const [op, a, b, c] of nodes) {
        if (op === 'assign') assign(a, expr(b, scope), scope);
        else if (op === 'expression') expr(a, scope);
        else if (op === 'return') return { value: expr(a, scope) };
        else if (op === 'if') {
          const result = statements(truth(expr(a, scope)) ? b : c, scope);
          if (result) return result;
        } else if (op === 'for') {
          for (const value of expr(b, scope)) {
            assign(a, value, scope);
            const result = statements(c, scope);
            if (result) return result;
          }
        } else fail('Vorlagen', 'Unbekannte Anweisung.');
      }
      return null;
    }
    return call(name, args, Object.create(null));
  }

  function text(value, path) {
    if (typeof value !== 'string' || value.length > 40000 || Array.from(value).length > 20000) fail(path, 'Text mit hoechstens 20000 Zeichen erforderlich.');
    if (/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f\ud800-\udfff\ufffe\uffff]/u.test(value)) fail(path, 'Unzulaessige Steuerzeichen.');
    return value;
  }
  function number(value, path) {
    if (typeof value !== 'number' || !Number.isFinite(value) || Math.abs(value) > 1e15) fail(path, 'Endliche Zahl erforderlich.');
    return value;
  }
  function publicV4(host) {
    const octets = host.split('.').map(Number);
    if (octets.length !== 4 || octets.some((value) => !Number.isInteger(value) || value < 0 || value > 255)) return false;
    const [a, b, c, d] = octets;
    return !(a === 0 || a === 10 || a === 127 || a >= 240 || (a === 100 && b >= 64 && b <= 127)
      || (a === 169 && b === 254) || (a === 172 && b >= 16 && b <= 31) || (a === 192 && b === 168)
      || (a === 192 && b === 0 && ((c === 0 && d !== 9 && d !== 10) || c === 2))
      || (a === 198 && (b === 18 || b === 19 || (b === 51 && c === 100))) || (a === 203 && b === 0 && c === 113));
  }
  function publicHost(host) {
    if (host.startsWith('[')) {
      const ip = host.slice(1, -1);
      if (ip.startsWith('::ffff:')) {
        const parts = ip.slice(7).split(':').map((part) => parseInt(part, 16));
        return parts.length === 2 && publicV4(`${parts[0] >> 8}.${parts[0] & 255}.${parts[1] >> 8}.${parts[1] & 255}`);
      }
      // Only global unicast; special-use/documentation/transition networks stay untrusted.
      const parts = ip.split(':');
      if (parts[0] === '2001' && parseInt(parts[1] || '0', 16) < 0x200) return false;
      return /^[23][0-9a-f]{3}:/.test(ip) && !/^(2001:db8:|2002:|3fff:)/.test(ip);
    }
    if (/^[0-9.]+$/.test(host)) return publicV4(host);
    return /^[a-z0-9.-]+$/.test(host) && host.includes('.') && host !== 'localhost' && !/\.(localhost|local|internal)$/.test(host);
  }
  function url(value, path) {
    text(value, path);
    if (!value) return value;
    if (value.length > 4096 || /[\s\\<>"']/.test(value)) fail(path, 'Ungueltige Quellen-URL.');
    let parsed;
    try { parsed = new URL(value); } catch (_) { fail(path, 'Oeffentliche HTTP(S)-URL erforderlich.'); }
    const authority = value.match(/^https?:\/\/([^/?#]*)/i)?.[1] || '';
    const rawHost = authority.slice(authority.lastIndexOf('@') + 1).replace(/:\d*$/, '').replace(/\.$/, '');
    if (rawHost.includes('%') || (/^[\x00-\x7f]+$/.test(rawHost) && !rawHost.startsWith('[')
      && (!rawHost.includes('.') || (/^[0-9.]+$/.test(rawHost) && rawHost !== parsed.hostname)))) fail(path, 'Ungueltiger Quellen-Host.');
    if (!['http:', 'https:'].includes(parsed.protocol) || !/^https?:\/\//i.test(value) || parsed.username || parsed.password
      || parsed.port === '0' || !publicHost(parsed.hostname.toLowerCase().replace(/\.$/, ''))) fail(path, 'Oeffentliche HTTP(S)-URL ohne Zugangsdaten erforderlich.');
    return value;
  }
  function sequence(value, path, limit, validate) {
    if (!Array.isArray(value) || value.length > limit) fail(path, `Liste mit hoechstens ${limit} Eintraegen erforderlich.`);
    return value.map((item, index) => validate(item, `${path}[${index}]`));
  }
  function position(value, path) {
    const result = sequence(value, path, 3, number);
    if (![2, 3].includes(result.length) || Math.abs(result[0]) > 180 || Math.abs(result[1]) > 90) fail(path, 'WGS84-Koordinaten erforderlich.');
    return result;
  }
  function bounds(value, path) {
    if (value === null) return null;
    const result = sequence(value, path, 4, number);
    if (result.length !== 4) fail(path, 'West, Sued, Ost und Nord erforderlich.');
    position(result.slice(0, 2), path); position(result.slice(2), path);
    if (result[0] > result[2] || result[1] > result[3]) fail(path, 'Vertauschte Begrenzung.');
    return result;
  }
  function validate(input, imported = true) {
    const data = templates(), limits = data.limits;
    let nodes = 0, size = 0, positions = 0;
    function bytes(count) { size += count; if (size > limits.MAX_CASE_BYTES) fail('Vorgang', 'Der Vorgang ueberschreitet 2 MiB.'); }
    function preflight(value, depth = 0) {
      if (++nodes > 150000 || depth > 16) fail('Vorgang', 'Die JSON-Struktur ist zu gross oder zu tief.');
      if (typeof value === 'string') { text(value, 'Text'); bytes(encoder.encode(JSON.stringify(value)).length); }
      else if (typeof value === 'number') { number(value, 'Zahl'); bytes(String(value).length); }
      else if (value === null || typeof value === 'boolean') bytes(String(value).length);
      else if (Array.isArray(value)) {
        bytes(2 + Math.max(0, value.length - 1) * 2);
        for (let index = 0; index < value.length; index++) {
          const descriptor = Object.getOwnPropertyDescriptor(value, index);
          if (!descriptor || !own(descriptor, 'value')) fail('Vorgang', 'Nur JSON-Datentypen erlaubt.');
          preflight(descriptor.value, depth + 1);
        }
      } else if (object(value) && [Object.prototype, null].includes(Object.getPrototypeOf(value))) {
        const entries = Object.entries(Object.getOwnPropertyDescriptors(value));
        if (Object.getOwnPropertySymbols(value).length) fail('Vorgang', 'Nur JSON-Datentypen erlaubt.');
        bytes(2 + Math.max(0, entries.length - 1) * 2);
        for (const [key, descriptor] of entries) {
          text(key, 'Feldname'); bytes(encoder.encode(JSON.stringify(key)).length + 2);
          if (!own(descriptor, 'value') || !descriptor.enumerable) fail('Vorgang', 'Nur JSON-Datentypen erlaubt.');
          preflight(descriptor.value, depth + 1);
        }
      } else fail('Vorgang', 'Nur JSON-Datentypen erlaubt.');
    }
    function check(spec, value, path) {
      const [kind, child, limit] = spec;
      switch (kind) {
        case 'text': return text(value, path);
        case 'url': return url(value, path);
        case 'number': return number(value, path);
        case 'area': if (value === null) return null; if (number(value, path) < 0) fail(path, 'Negative Flaeche.'); return value;
        case 'boolean': if (typeof value !== 'boolean') fail(path, 'Wahrheitswert erforderlich.'); return value;
        case 'nullable': return value === null ? null : check(child, value, path);
        case 'sequence': return sequence(value, path, limit, (item, location) => check(child, item, location));
        case 'object': {
          if (!object(value)) fail(path, 'JSON-Objekt erforderlich.');
          return Object.fromEntries(Object.entries(value).map(([key, item]) => {
            if (!own(child, key)) fail(path, 'Nicht erlaubtes Feld.');
            return [key, check(child[key], item, `${path}.${key}`)];
          }));
        }
        case 'text_or_list': return Array.isArray(value) ? sequence(value, path, 100, text) : text(value, path);
        case 'bounds': return bounds(value, path);
        case 'center': {
          if (value === null) return null;
          if (object(value)) {
            const result = check(['object', { latitude: ['number'], longitude: ['number'] }], value, path);
            if (!own(result, 'latitude') || !own(result, 'longitude')) fail(path, 'Breite und Laenge erforderlich.');
            position([result.longitude, result.latitude], path); return result;
          }
          if (!Array.isArray(value) || value.length !== 2) fail(path, 'Kartenzentrum muss Breite und Laenge enthalten.');
          position([value[1], value[0]], path); return [...value];
        }
        case 'geometry': {
          if (value === null) return null;
          if (!object(value) || Object.keys(value).sort().join(',') !== 'coordinates,type') fail(path, 'Geometrie braucht nur type und coordinates.');
          if (encoder.encode(JSON.stringify(value)).length > limits.MAX_GEOMETRY_BYTES) fail(path, 'Geometrie ueberschreitet 256 KiB.');
          let count = 0;
          const point = (item, location) => {
            if (++count > limits.MAX_GEOMETRY_POSITIONS || ++positions > limits.MAX_TOTAL_POSITIONS) fail(path, 'Zu viele Geometriepositionen.');
            return position(item, location);
          };
          const line = (item, location) => {
            const result = sequence(item, location, limits.MAX_GEOMETRY_POSITIONS, point);
            if (result.length < 2) fail(location, 'Linie braucht mindestens zwei Positionen.');
            return result;
          };
          const ring = (item, location) => {
            const result = line(item, location);
            if (result.length < 4 || JSON.stringify(result[0]) !== JSON.stringify(result[result.length - 1])) fail(location, 'Polygonring muss geschlossen sein.');
            return result;
          };
          const nonempty = (validator) => (item, location) => {
            const result = sequence(item, location, limits.MAX_GEOMETRY_POSITIONS, validator);
            if (!result.length) fail(location, 'Leere Geometrie.');
            return result;
          };
          const polygon = nonempty(ring);
          const kinds = { Point: point, MultiPoint: nonempty(point), LineString: line, MultiLineString: nonempty(line), Polygon: polygon, MultiPolygon: nonempty(polygon) };
          if (typeof value.type !== 'string' || !own(kinds, value.type)) fail(path, 'Nicht unterstuetzter Geometrietyp.');
          return { type: value.type, coordinates: kinds[value.type](value.coordinates, `${path}.coordinates`) };
        }
        default: return fail(path, 'Unbekanntes Schema.');
      }
    }
    preflight(input);
    const checked = check(data.schema, input, 'Vorgang'), seen = new Set();
    for (const parcel of checked.selected_parcels || []) {
      if (parcel.stable_id) {
        const key = JSON.stringify([parcel.provider_id || '', parcel.stable_id]);
        if (seen.has(key)) fail('selected_parcels', 'Eine Auswahl-ID ist doppelt vorhanden.');
        seen.add(key);
      }
    }
    if (imported && checked.profile) {
      for (const entry of [checked.profile, ...['authorities', 'providers', 'evidence'].flatMap((key) => checked.profile[key] || [])]) {
        for (const key of ['status', 'verification_state', 'test_result']) {
          if (['verifiziert', 'amtlich_verifiziert', 'verified', 'belegt', 'ok', 'success', 'active'].includes(fold(pyStrip(entry[key] || ''), data))) entry[key] = 'gefunden_ungeprueft';
        }
      }
    }
    return checked;
  }

  const drafts = (checked) => render(templates(), '_drafts', [checked]);
  const html = (items) => render(templates(), '_html', [items]);
  function sources(checked) {
    const data = templates(), lines = [...data.sources.base];
    if (render(data, '_nrw', [checked])) lines.splice(lines.length - 1, 0, data.sources.nrw);
    function collect(value) {
      if (Array.isArray(value)) value.forEach(collect);
      else if (object(value)) {
        for (const [key, item] of Object.entries(value)) {
          if (key.endsWith('url') || ['official_website', 'evidence_urls', 'source_urls'].includes(key)) {
            for (const value of Array.isArray(item) ? item : [item]) if (value && !lines.includes(value)) lines.push(value);
          } else if (object(item) || Array.isArray(item)) collect(item);
        }
      }
    }
    collect(checked); return `${lines.join('\n')}\n`;
  }
  function zip(entries) {
    if (!root.fflate) fail('ZIP', 'Die lokale ZIP-Bibliothek fehlt.');
    return root.fflate.zipSync(Object.fromEntries(entries.map(([name, bytes]) => [name, [bytes, {
      mtime: new Date(1980, 0, 1), os: 3, attrs: 0o600 << 16,
    }]])), { level: 6 });
  }
  async function docx(items) {
    if (!root.docx || !root.fflate) fail('DOCX', 'Die lokalen DOCX/ZIP-Bibliotheken fehlen.');
    const { Document, Paragraph, TextRun, Header, Packer } = root.docx;
    const marker = templates().constants.DRAFT_MARKER;
    const run = { font: { ascii: 'Times New Roman', hAnsi: 'Times New Roman', eastAsia: 'Times New Roman', cs: 'Times New Roman' }, size: 22, sizeComplexScript: 22, color: '000000' };
    const spacing = { after: 120, line: 269 };
    const paragraph = (text, options = {}) => new Paragraph({
      ...options, children: text.replace(/\r\n?/g, '\n').split('\n').flatMap((line, index) => [
        ...(index ? [new TextRun({ ...run, break: 1 })] : []),
        ...line.split('\t').flatMap((part, tab) => [...(tab ? [new TextRun({ ...run, children: [new root.docx.Tab()] })] : []), new TextRun({ ...run, text: part, bold: Boolean(options.bold) })]),
      ]),
    });
    const styles = [
      ['Normal', 'Normal', false], ['Title', 'Title', true], ['Heading1', 'heading 1', true],
      ['Heading2', 'heading 2', true], ['Header', 'Header', false], ['Footer', 'Footer', false],
    ].map(([id, name, bold]) => ({
      id, name, ...(id === 'Normal' ? { default: true } : { basedOn: 'Normal', next: 'Normal' }),
      run: { ...run, bold }, paragraph: {
        spacing: id.startsWith('Heading') ? { ...spacing, before: 240, after: 220 } : spacing,
        ...(bold ? { keepNext: true } : {}), ...(id.startsWith('Heading') ? { outlineLevel: id === 'Heading1' ? 0 : 1 } : {}),
      },
    }));
    const children = items.flatMap((item, index) => [
      paragraph(marker, { bold: true, pageBreakBefore: Boolean(index), keepNext: true }),
      paragraph(item.title, { style: 'Title', bold: true }),
      ...item.blocks.map(([tag, text]) => paragraph(text, { style: { h2: 'Heading1', h3: 'Heading2' }[tag] || 'Normal', bold: tag !== 'p' })),
    ]);
    const document = new Document({
      creator: '', lastModifiedBy: '', description: '', subject: marker,
      title: items.length === 1 ? items[0].title : 'Grundst\u00fccksrecherche: vier Entw\u00fcrfe',
      styles: { default: { document: { run, paragraph: { spacing } } }, paragraphStyles: styles },
      sections: [{
        properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1247, right: 1247 } } },
        headers: { default: new Header({ children: [paragraph(marker, { style: 'Header' })] }) }, children,
      }],
    });
    const bytes = new Uint8Array(await Packer.toArrayBuffer(document));
    const files = root.fflate.unzipSync(bytes);
    // The OOXML library owns the package; normalize only volatile metadata/ZIP dates.
    const core = new TextDecoder().decode(files['docProps/core.xml']).replace(/(<dcterms:(?:created|modified)\b[^>]*>)[^<]*(<\/dcterms:(?:created|modified)>)/g, '$12000-01-01T00:00:00Z$2');
    files['docProps/core.xml'] = encoder.encode(core);
    return zip(Object.keys(files).sort().filter((name) => !name.endsWith('/')).map((name) => [name, files[name]]));
  }
  function sortedJSON(value) {
    if (Array.isArray(value)) return `[${value.map(sortedJSON).join(',')}]`;
    if (object(value)) return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${sortedJSON(value[key])}`).join(',')}}`;
    return JSON.stringify(value);
  }
  function build(input) {
    return drafts(validate(input, false)).map((item) => ({ id: item.id, title: item.title, html: html([item]) }));
  }
  async function exportDocument(input, format, documentId = null) {
    if (!['html', 'docx', 'zip', 'json'].includes(format)) fail('Export', 'Das Exportformat muss html, docx, zip oder json sein.');
    if (documentId !== null && (typeof documentId !== 'string' || !own(templates().constants.TITLES, documentId))) fail('Export', 'Die Dokument-ID ist unbekannt.');
    if (['zip', 'json'].includes(format) && documentId !== null) fail('Export', 'Gesamtexporte duerfen keine Dokument-ID angeben.');
    const checked = validate(input, false), all = drafts(checked);
    const selected = documentId === null ? all : all.filter((item) => item.id === documentId);
    if (format === 'html') return new Blob([html(selected)], { type: 'text/html; charset=utf-8' });
    if (format === 'json') return new Blob([sortedJSON(checked)], { type: 'application/json; charset=utf-8' });
    if (format === 'docx') return new Blob([await docx(selected)], { type: docxType });
    const entries = [];
    for (const item of all) entries.push([`${item.id}.docx`, await docx([item])], [`${item.id}.html`, encoder.encode(html([item]))]);
    entries.push(['vorgang.json', encoder.encode(sortedJSON(checked))], ['quellen.txt', encoder.encode(sources(checked))]);
    return new Blob([zip(entries)], { type: 'application/zip' });
  }
  root.PortableDocuments = Object.freeze({ build, export: exportDocument, validate });
})(window);
