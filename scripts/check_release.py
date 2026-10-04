#!/usr/bin/env python3
"""Fail-closed checks for the public ASCP publication surface."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TITLE = "The Agent Security Control Plane: Toward a Zero-Trust Architecture for Autonomous Machine Cognition"
DOI = "10.5281/zenodo.23146801"
CONCEPT_DOI = "10.5281/zenodo.23146800"
ORCID = "0009-0001-6573-385X"
PDF_SHA = "26f5a9bef6a02d2fe8f2f13c33420686fe389f51616d94b7afc220efe80f09f6"
MD_SHA = "2b473a4d3efdf77503296452e754fbf719093862c66662b0f6476e3a52767ac1"
SOURCE_SHA = "ec9b76e0cb3dcf983e913d4c563a35b9342872bb3bbef7cdc6c917b9902eb007"
RECORD_ID = "23146801"


def require(cond: bool, message: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {message}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    required = [
        "The-Agent-Security-Control-Plane.pdf",
        "The-Agent-Security-Control-Plane.md",
        "The-Agent-Security-Control-Plane-source.zip",
        "README.md",
        "SECURITY.md",
        "CITATION.cff",
        ".zenodo.json",
        "LICENSE-PAPER.md",
        "LICENSE-CODE",
        "SHA256SUMS.txt",
        "Makefile",
        "publication/manifest.json",
        f"publication/zenodo-{RECORD_ID}/The-Agent-Security-Control-Plane.pdf",
        "scripts/check_release.py",
        "scripts/check_repository_hygiene.py",
        "tests/test_math.py",
        ".github/CODEOWNERS",
        ".github/workflows/reproducibility.yml",
    ]
    for rel in required:
        require((ROOT / rel).is_file(), f"missing {rel}")

    md = (ROOT / "The-Agent-Security-Control-Plane.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    zenodo = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / "publication/manifest.json").read_text(encoding="utf-8"))

    require(sha256(ROOT / "The-Agent-Security-Control-Plane.pdf") == PDF_SHA, "root PDF SHA-256 mismatch")
    require(sha256(ROOT / "The-Agent-Security-Control-Plane.md") == MD_SHA, "root Markdown SHA-256 mismatch")
    require(sha256(ROOT / "The-Agent-Security-Control-Plane-source.zip") == SOURCE_SHA, "root source ZIP SHA-256 mismatch")
    require(
        sha256(ROOT / f"publication/zenodo-{RECORD_ID}/The-Agent-Security-Control-Plane.pdf") == PDF_SHA,
        "archived Zenodo PDF SHA-256 mismatch",
    )

    require(manifest["status"] == "published", "publication manifest not marked published")
    require(manifest["doi"] == DOI, "publication manifest DOI mismatch")
    require(manifest["concept_doi"] == CONCEPT_DOI, "publication manifest concept DOI mismatch")
    require(manifest["published"]["pdf_sha256"] == PDF_SHA, "manifest PDF hash mismatch")
    require(manifest["published"]["markdown_sha256"] == MD_SHA, "manifest Markdown hash mismatch")
    require(manifest["published"]["source_zip_sha256"] == SOURCE_SHA, "manifest source ZIP hash mismatch")

    require(zenodo["title"] == TITLE, "Zenodo title mismatch")
    require(zenodo["creators"][0]["name"] == "Thor, Thor", "Zenodo creator mismatch")
    require(zenodo["creators"][0]["orcid"] == ORCID, "Zenodo ORCID mismatch")
    require(zenodo["license"] == "cc-by-4.0", "Zenodo license mismatch")
    require(zenodo["publication_type"] == "preprint", "Zenodo publication type mismatch")

    for marker in (
        TITLE,
        DOI,
        ORCID,
        "actions/workflows/reproducibility.yml/badge.svg?branch=main",
        "paper-CC%20BY%204.0",
        "code-MIT",
        "figures/fig3_architecture.png",
        "figures/fig4_delegation.png",
        "figures/fig8_hop_risk.png",
    ):
        require(marker in readme, f"README marker missing: {marker}")

    for marker in (TITLE, DOI, ORCID, "https://github.com/codethor0/agent-security-control-plane"):
        require(marker in cff, f"CITATION.cff marker missing: {marker}")

    math_markers = (
        r"C_{i+1}\preceq C_i",
        r"C_H = \operatorname{Issue}",
        r"\operatorname{Bind}(C_H,b,h,\textsf{mission})=1",
        r"\pi(q)=1",
        r"\land \neg V(q)\land [\rho(q)<\tau_e]",
        r"P\!\left(\bigcup_{i=1}^{n}F_i\right)",
        r"\left[1-P\!\left(F_i\mid \bigcap_{j<i}F_j^{c}\right)\right]",
        "F7 - P = 0.60",
        "final high-impact authorization gate remains deterministic",
        "semantic routing hijack",
        "Audit as obligation",
    )
    for marker in math_markers:
        require(marker in md, f"manuscript marker missing: {marker}")

    require(r"\land A(q)" not in md, "audit obligation regressed into authorization conjunct")
    require("independent coin-flip model" in md, "correlated-risk caveat missing")
    require("not a theorem" in md, "formal-model scope boundary missing")
    require("can still be harmful" in md, "authorized-but-harmful limitation missing")

    figures = sorted((ROOT / "source/figures").glob("*.pdf"))
    previews = sorted((ROOT / "figures").glob("*.png"))
    require(len(figures) == 8, f"expected 8 vector figures, found {len(figures)}")
    require(len(previews) == 8, f"expected 8 figure previews, found {len(previews)}")
    require((ROOT / "source/The-Agent-Security-Control-Plane.tex").is_file(), "reviewed TeX source missing")

    print("RELEASE SURFACE CHECK: PASS")
    print(f"doi={DOI}")
    print(f"pdf_sha256={PDF_SHA}")
    print(f"markdown_sha256={MD_SHA}")
    print(f"source_zip_sha256={SOURCE_SHA}")
    print(f"vector_figures={len(figures)} previews={len(previews)}")


if __name__ == "__main__":
    main()
