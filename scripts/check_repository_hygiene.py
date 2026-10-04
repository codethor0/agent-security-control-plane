#!/usr/bin/env python3
"""Fail-closed checks for public repository hygiene and disclosure safety."""
from __future__ import annotations

import re
import struct
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {message}")


TEXT_EXT = {".md", ".txt", ".py", ".json", ".cff", ".yml", ".yaml", ".tex", ".sh"}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"github_pat_[A-Za-z0-9_]+|gh[pousr]_[A-Za-z0-9]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "OpenAI-style API key": re.compile(r"(?<![A-Za-z0-9])sk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
}
# Avoid substring false positives such as the 'sk-' inside ordinary words like 'risk-score'.
_key_pat = SECRET_PATTERNS['OpenAI-style API key']
assert _key_pat.search('risk-score-is-a-policy-heuristic-not-a-probability') is None
assert _key_pat.search('x sk-proj-abcdefghijklmnopqrstuvwxyz1234567890 y') is not None
PRIVATE_SURFACE_PATTERNS = {
    "local macOS user path": re.compile(r"/Users/[A-Za-z0-9._-]+"),
    "local workstation identifier": re.compile(r"Lords-MacBook|Moltbook", re.I),
    "private workflow/tool trace": re.compile(
        r"Kimi|Moonshot|sandbox:/mnt/data|publish_ascp_github|ASCP-ZENODO-FREEZE", re.I
    ),
}
FORBIDDEN_NAMES = {".DS_Store", ".env", "id_rsa", "id_ed25519"}
FORBIDDEN_DIRS = {"__MACOSX", ".ssh", "audit"}


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    require(data[:8] == b"\x89PNG\r\n\x1a\n", f"invalid PNG signature: {path}")
    return struct.unpack(">II", data[16:24])


def main() -> None:
    require(not (ROOT / "audit").exists(), "expanded audit/process directory should not be public")

    scanner_path = Path(__file__).resolve()
    for p in ROOT.rglob("*"):
        if ".git" in p.parts:
            continue
        if p.name in FORBIDDEN_NAMES:
            raise SystemExit(f"FAIL: forbidden file name: {p.relative_to(ROOT)}")
        if any(part in FORBIDDEN_DIRS for part in p.parts):
            raise SystemExit(f"FAIL: forbidden directory on public surface: {p.relative_to(ROOT)}")
        if p.is_file() and p.suffix.lower() in TEXT_EXT:
            # The scanner itself intentionally contains the signatures it detects.
            # Exclude only this one validator source file from signature matching;
            # all other public text/config/code surfaces remain fail-closed.
            if p.resolve() == scanner_path:
                continue
            body = p.read_text(encoding="utf-8", errors="ignore")
            for name, pattern in SECRET_PATTERNS.items():
                require(not pattern.search(body), f"possible {name} in {p.relative_to(ROOT)}")
            for name, pattern in PRIVATE_SURFACE_PATTERNS.items():
                require(not pattern.search(body), f"{name} in {p.relative_to(ROOT)}")

    source_zip = ROOT / "The-Agent-Security-Control-Plane-source.zip"
    with zipfile.ZipFile(source_zip) as zf:
        for name in zf.namelist():
            parts = Path(name).parts
            require(not any(part in {".DS_Store", "__MACOSX", ".env", ".ssh", "id_rsa", "id_ed25519"} for part in parts),
                    f"suspicious member in frozen source ZIP: {name}")

    pdfs = sorted((ROOT / "source/figures").glob("*.pdf"))
    pngs = sorted((ROOT / "figures").glob("*.png"))
    require(len(pdfs) == 8, f"expected 8 reviewed vector figures, found {len(pdfs)}")
    require(len(pngs) == 8, f"expected 8 PNG previews, found {len(pngs)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for png in pngs:
        width, height = png_dimensions(png)
        require(width >= 600 and height >= 300, f"preview unexpectedly small: {png.name} {width}x{height}")
        require(f"figures/{png.name}" in readme, f"README does not reference {png.name}")

    workflow = (ROOT / ".github/workflows/reproducibility.yml").read_text(encoding="utf-8")
    require("permissions:\n  contents: read" in workflow, "workflow permissions are not read-only")
    uses = []
    for line in workflow.splitlines():
        stripped = line.strip()
        if "uses:" not in stripped:
            continue
        prefix, value = stripped.split("uses:", 1)
        if prefix.strip() not in {"", "-"}:
            continue
        action = value.split("#", 1)[0].strip()
        uses.append(action)
    require(uses, "workflow contains no actions")
    action_ref = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@[0-9a-fA-F]{40}$")
    for action in uses:
        require(action_ref.fullmatch(action) is not None,
                f"workflow action is not pinned to a full commit SHA: {action}")

    print("REPOSITORY HYGIENE CHECK: PASS")
    print(f"vector_figures={len(pdfs)} previews={len(pngs)}")
    print("workflow_permissions=contents:read")
    print("private_surface_scan=clean")


if __name__ == "__main__":
    main()
