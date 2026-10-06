"""Build-time-only bridge from documents.py to the offline browser engine.

Include template_script() as a local classic script before portable-documents.js.
No case data is embedded here. The browser interprets a closed, data-only subset
of the existing draft functions; unsupported template changes fail the build.
"""

from __future__ import annotations

import ast
from functools import lru_cache
import hashlib
import inspect
import json

if __package__:
    from . import documents
else:
    import documents


FUNCTIONS = ("_value", "_sentence", "_nrw", "_parcel_blocks", "_authority_blocks", "_drafts", "_html")
METHODS = {"get", "strip", "rstrip", "casefold", "endswith", "startswith", "isdigit",
           "extend", "append", "insert", "join", "items"}
CALLS = set(FUNCTIONS) | {"v", "str", "len", "isinstance", "all", "list", "tuple", "enumerate", "_Draft", "escape"}


def _encode(node):
    """Serialize only the operations used by the text templates, never code."""
    if isinstance(node, ast.Constant):
        return ["literal", node.value]
    if isinstance(node, ast.Name):
        return ["name", node.id]
    if isinstance(node, (ast.List, ast.Tuple)):
        return ["list", [_encode(item) for item in node.elts]]
    if isinstance(node, ast.Dict):
        return ["dict", [[_encode(key), _encode(value)] for key, value in zip(node.keys, node.values)]]
    if isinstance(node, ast.JoinedStr):
        return ["text", [_encode(item) for item in node.values]]
    if isinstance(node, ast.FormattedValue) and node.conversion == -1 and node.format_spec is None:
        return ["string", _encode(node.value)]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return ["add", _encode(node.left), _encode(node.right)]
    if isinstance(node, ast.BoolOp):
        return ["and" if isinstance(node.op, ast.And) else "or", [_encode(item) for item in node.values]]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return ["not", _encode(node.operand)]
    if isinstance(node, ast.Compare) and len(node.ops) == 1:
        op = type(node.ops[0]).__name__
        if op not in {"Eq", "NotEq", "Is", "In", "NotIn"}:
            raise ValueError(f"Unsupported template comparison: {op}")
        return ["compare", op, _encode(node.left), _encode(node.comparators[0])]
    if isinstance(node, ast.IfExp):
        return ["choose", _encode(node.test), _encode(node.body), _encode(node.orelse)]
    if isinstance(node, ast.Subscript):
        return ["item", _encode(node.value), _encode(node.slice)]
    if isinstance(node, ast.Attribute) and node.attr in {"id", "title", "blocks"}:
        return ["field", _encode(node.value), node.attr]
    if isinstance(node, ast.Call):
        args = [_encode(arg) for arg in node.args]
        if isinstance(node.func, ast.Name) and node.func.id in CALLS:
            keywords = {keyword.arg: _encode(keyword.value) for keyword in node.keywords}
            if any(key != "quote" for key in keywords):
                raise ValueError("Unsupported template keyword")
            return ["call", node.func.id, args, keywords]
        if isinstance(node.func, ast.Attribute) and node.func.attr in METHODS and not node.keywords:
            return ["method", _encode(node.func.value), node.func.attr, args]
    if isinstance(node, ast.Lambda) and not node.args.defaults:
        return ["lambda", [arg.arg for arg in node.args.args], _encode(node.body)]
    if isinstance(node, (ast.ListComp, ast.GeneratorExp)) and len(node.generators) == 1:
        generator = node.generators[0]
        if not generator.ifs and not generator.is_async:
            return ["map", _encode(generator.target), _encode(generator.iter), _encode(node.elt)]
    if isinstance(node, ast.Assign) and len(node.targets) == 1:
        return ["assign", _encode(node.targets[0]), _encode(node.value)]
    if isinstance(node, ast.AugAssign) and isinstance(node.op, ast.Add):
        return ["assign", _encode(node.target), ["add", _encode(node.target), _encode(node.value)]]
    if isinstance(node, ast.Expr):
        return ["expression", _encode(node.value)]
    if isinstance(node, ast.If):
        return ["if", _encode(node.test), [_encode(item) for item in node.body], [_encode(item) for item in node.orelse]]
    if isinstance(node, ast.For) and not node.orelse:
        return ["for", _encode(node.target), _encode(node.iter), [_encode(item) for item in node.body]]
    if isinstance(node, ast.Return):
        return ["return", _encode(node.value)]
    raise ValueError(f"Unsupported portable template syntax: {ast.dump(node)}")


def _schema(validator):
    primitives = {"_text", "_url", "_number", "_area", "_boolean", "_text_or_list", "_center", "_bounds", "_geometry"}
    if validator.__name__ in primitives:
        return [validator.__name__[1:]]
    closure = inspect.getclosurevars(validator).nonlocals
    if set(closure) == {"schema"}:
        return ["object", {key: _schema(value) for key, value in closure["schema"].items()}]
    if set(closure) == {"validator", "limit"}:
        return ["sequence", _schema(closure["validator"]), closure["limit"]]
    if validator.__name__ == "<lambda>" and set(closure) == {"validator"}:
        return ["nullable", _schema(closure["validator"])]
    raise ValueError(f"Unsupported portable validator: {validator.__qualname__}")


@lru_cache(maxsize=1)
def template_data():
    functions = {}
    for name in FUNCTIONS:
        source = ast.parse(inspect.getsource(getattr(documents, name))).body[0]
        functions[name] = {"args": [arg.arg for arg in source.args.args], "body": [_encode(item) for item in source.body]}
    # Full Unicode casefold and digit semantics keep status and NRW tests equal to Python.
    casefold = {chr(i): chr(i).casefold() for i in range(0x110000) if chr(i).casefold() != chr(i).lower()}
    digits = "".join(chr(i) for i in range(0x110000) if chr(i).isdigit())
    return {
        "version": 1,
        "source_sha256": hashlib.sha256(inspect.getsource(documents).encode()).hexdigest(),
        "functions": functions,
        "constants": {"MISSING": documents.MISSING, "DRAFT_MARKER": documents.DRAFT_MARKER, "TITLES": documents.TITLES},
        "schema": ["object", {key: _schema(value) for key, value in documents.CASE_SCHEMA.items()}],
        "limits": {key: getattr(documents, key) for key in ("MAX_CASE_BYTES", "MAX_GEOMETRY_BYTES", "MAX_GEOMETRY_POSITIONS", "MAX_TOTAL_POSITIONS")},
        "sources": {"base": documents._sources({}).decode().splitlines(), "nrw": ": ".join(documents.NRW_SOURCE)},
        "casefold": casefold,
        "digits": digits,
    }


@lru_cache(maxsize=1)
def template_script() -> str:
    """Return safe JavaScript for a local .js file or an inline script element."""
    data = json.dumps(template_data(), ensure_ascii=True, separators=(",", ":"), allow_nan=False)
    data = data.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    return "window.PortableDocumentTemplates=" + data + ";\n"


if __name__ == "__main__":
    print(template_script(), end="")
