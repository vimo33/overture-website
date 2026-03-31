#!/usr/bin/env python3
import hashlib
import json
import mimetypes
import re
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets" / "images"
MANIFEST_FILE = ASSET_DIR / "manifest.json"
URL_RE = re.compile(r"https://lh3\.googleusercontent\.com/aida-public/[^\"')\s]+")


def load_manifest() -> dict:
    if MANIFEST_FILE.exists():
        return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    return {}


def detect_extension(content_type: str) -> str:
    guessed = mimetypes.guess_extension((content_type or "").split(";")[0].strip()) or ".jpg"
    if guessed == ".jpe":
        guessed = ".jpg"
    return guessed


def download_asset(url: str, manifest: dict) -> str:
    if url in manifest:
        return manifest[url]

    with urllib.request.urlopen(url) as response:
        content = response.read()
        extension = detect_extension(response.headers.get("Content-Type", "image/jpeg"))

    name = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16] + extension
    target = ASSET_DIR / name
    target.write_bytes(content)
    manifest[url] = name
    return name


def rewrite_file(path: Path, manifest: dict) -> None:
    content = path.read_text(encoding="utf-8")
    urls = sorted(set(URL_RE.findall(content)))
    if not urls:
        return

    updated = content
    for url in urls:
        filename = download_asset(url, manifest)
        updated = updated.replace(url, f"../assets/images/{filename}")

    if updated != content:
        path.write_text(updated, encoding="utf-8")


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()
    html_files = sorted((ROOT / "site").glob("*.html")) + sorted((ROOT / "pitch-deck").glob("*.html"))
    for html_file in html_files:
        rewrite_file(html_file, manifest)
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    print(f"Mirrored remote images for {len(html_files)} html files")


if __name__ == "__main__":
    main()
