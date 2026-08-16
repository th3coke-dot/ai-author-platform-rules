#!/usr/bin/env python3
"""Validate AI-author platform-rules records.

Checks:
  * every data/*.json matches schema.json (jsonschema if available)
  * required fields present and non-empty
  * every row has source_url, accessed (YYYY-MM-DD), and a quote
  * payout_kyc is never empty or whitespace
  * at least 10 platform files

Exit 0 only if every check passes.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema.json"
DATA_DIR = ROOT / "data"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
REQUIRED = (
    "platform",
    "account_creator",
    "ai_content_allowed",
    "disclosure_rule",
    "payout_kyc",
    "source_url",
    "accessed",
    "quote",
)
ALLOWED_AI = {"yes", "yes_with_conditions", "no", "not_applicable"}


def load_jsonschema():
    venv_pkg = ROOT / ".venv" / "lib"
    if venv_pkg.exists():
        for site in venv_pkg.glob("python*/site-packages"):
            sys.path.insert(0, str(site))
    try:
        import jsonschema
        from jsonschema import Draft202012Validator
        return jsonschema, Draft202012Validator
    except ImportError:
        return None, None


def is_uri(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def check_record(path: Path, data: dict, errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    for key in REQUIRED:
        if key not in data:
            errors.append(f"{rel}: missing required field {key}")
            continue
        val = data[key]
        if not isinstance(val, str) or not val.strip():
            errors.append(f"{rel}: {key} is empty")
    kyc = data.get("payout_kyc")
    if kyc is None or (isinstance(kyc, str) and not kyc.strip()):
        errors.append(f"{rel}: payout_kyc is empty")
    url = data.get("source_url", "")
    if isinstance(url, str) and url.strip() and not is_uri(url):
        errors.append(f"{rel}: source_url is not an http(s) URL: {url!r}")
    accessed = data.get("accessed", "")
    if isinstance(accessed, str) and accessed and not DATE_RE.match(accessed):
        errors.append(f"{rel}: accessed is not YYYY-MM-DD: {accessed!r}")
    quote = data.get("quote", "")
    if isinstance(quote, str) and quote.strip() and len(quote.strip()) < 20:
        errors.append(f"{rel}: quote is too short")
    allowed = data.get("ai_content_allowed")
    if allowed is not None and allowed not in ALLOWED_AI:
        errors.append(f"{rel}: ai_content_allowed {allowed!r} not in {sorted(ALLOWED_AI)}")
    extras = data.get("additional_sources") or []
    if extras and not isinstance(extras, list):
        errors.append(f"{rel}: additional_sources must be an array")
        extras = []
    for i, src in enumerate(extras):
        if not isinstance(src, dict):
            errors.append(f"{rel}: additional_sources[{i}] is not an object")
            continue
        for key in ("source_url", "accessed", "quote"):
            val = src.get(key, "")
            if not isinstance(val, str) or not val.strip():
                errors.append(f"{rel}: additional_sources[{i}].{key} is empty")
        if src.get("source_url") and not is_uri(str(src.get("source_url"))):
            errors.append(f"{rel}: additional_sources[{i}].source_url is not an http(s) URL")
        if src.get("accessed") and not DATE_RE.match(str(src.get("accessed"))):
            errors.append(f"{rel}: additional_sources[{i}].accessed is not YYYY-MM-DD")


def main() -> int:
    errors: list[str] = []
    if not SCHEMA_PATH.is_file():
        print("FAIL: schema.json missing", file=sys.stderr)
        return 1
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    files = sorted(DATA_DIR.glob("*.json"))
    if len(files) < 10:
        errors.append(f"need at least 10 platform files, found {len(files)}")
    jsonschema, Draft202012Validator = load_jsonschema()
    validator = Draft202012Validator(schema) if Draft202012Validator else None
    engine = "jsonschema" if validator else "stdlib-fallback"
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        if validator is not None:
            for err in validator.iter_errors(data):
                loc = "/".join(str(p) for p in err.path) or "(root)"
                errors.append(f"{path.relative_to(ROOT)}: schema {loc}: {err.message}")
        check_record(path, data, errors)
    if errors:
        print(f"FAIL ({len(errors)} issue(s), engine={engine}):")
        for item in errors:
            print(f"  - {item}")
        return 1
    print(f"OK: {len(files)} platforms validated (engine={engine})")
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        print("  -", data.get("platform"), " (" + path.name + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
