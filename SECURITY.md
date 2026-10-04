# Security Policy

## Scope

This repository contains a research publication, reviewed source artifacts, figure previews, mathematical sanity tests, and publication-integrity checks. It is not a deployed ASCP implementation and does not expose a network service.

Security-relevant repository issues include:

- a mismatch between GitHub artifacts and the published Zenodo hashes;
- a secret, credential, private key, local workstation path, or other unintended private material committed to the repository;
- a CI change that weakens publication-integrity checks or grants unnecessary workflow permissions;
- a reproducible mathematical or implementation error in the verification utilities;
- a malicious or compromised dependency/workflow reference.

## Reporting

For research corrections, counterexamples, missing prior art, or reproducibility findings, use the repository issue template.

Do **not** paste credentials, private keys, tokens, or other sensitive material into a public issue. If a finding itself contains sensitive material, use GitHub's private security-reporting surface when available or contact the repository owner through their GitHub profile without including the secret in public text.

## Publication integrity

The canonical paper is the Zenodo record at:

https://doi.org/10.5281/zenodo.23146801

The repository-root PDF, Markdown, and source ZIP are checked against fixed SHA-256 values corresponding to that publication. CI must never rewrite those immutable artifacts.
