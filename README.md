# The Agent Security Control Plane

[![Reproducibility](https://github.com/codethor0/agent-security-control-plane/actions/workflows/reproducibility.yml/badge.svg?branch=main)](https://github.com/codethor0/agent-security-control-plane/actions/workflows/reproducibility.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23146801.svg)](https://doi.org/10.5281/zenodo.23146801)
[![Paper License](https://img.shields.io/badge/paper-CC%20BY%204.0-lightgrey.svg)](LICENSE-PAPER.md)
[![Code License](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--6573--385X-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0001-6573-385X)

**Toward a Zero-Trust Architecture for Autonomous Machine Cognition**

**Thor Thor**<br>
Independent Open-Source Researcher, [THOR-SEC](https://codethor0.github.io/thor-sec/)<br>
ORCID: [0009-0001-6573-385X](https://orcid.org/0009-0001-6573-385X)

> The language model may propose an action, but it is not the authorization root. Consequential effects must cross deterministic, externally enforced authority boundaries.

This research was conducted independently on the author's own time and is not sponsored by, affiliated with, or representative of any employer.

## Overview

*The Agent Security Control Plane* proposes an architecture-and-evidence synthesis for securing autonomous software agents. It composes workload identity, sponsor-preserving delegation, deterministic authorization, complete mediation at network and local effect boundaries, metadata validation, provenance, revocation, behavioral monitoring, and effect-level accountability outside the language model.

The paper treats the model as untrusted compute. It distinguishes semantic routing hijack from traditional ACE/RCE, separates vertical authority attenuation from sponsor-authorized horizontal specialist handoff, models correlated multi-agent failures without an independence assumption, and states explicitly that an authenticated and authorized action can still be harmful when it remains inside delegated scope.

The contribution is composition and evidence synthesis, not first invention. The architecture is a testable design hypothesis rather than a claim of end-to-end production validation.

## Core Contributions

| Area | Contribution |
| --- | --- |
| Evidence synthesis | Separates verified protocol/standards/vulnerability evidence from inference, forecasts, patent signals, and capital signals |
| Complete mediation | Requires consequential effects to cross an enforceable boundary, including local runtime/tool-dispatch paths that bypass network gateways |
| Delegated authority | Separates vertical attenuation from horizontal handoff and requires separately issued authority for specialist resources |
| Deterministic authorization | Keeps final high-impact allow/deny authority outside the nondeterministic model |
| Correlated risk | Replaces independent per-hop hazard assumptions with the exact conditional chain rule |
| Residual-risk honesty | States that in-scope harmful actions, control-plane compromise, local PEP bypass, and evidence-store DoS remain possible |
| Forecasting | Publishes falsifiable forecasts with declared subjective probabilities and an ex-post Brier-score rule |
| Reproducibility | Ships the frozen PDF, Markdown, source ZIP, citation metadata, audit record, hashes, math sanity tests, and CI release checks |

## Security Model Highlights

### Vertical delegation

For hierarchical subdelegation, the child capability may not exceed the parent:

```text
C_(i+1) <= C_i
```

The paper formalizes this component-wise across resource, operation, data, effect, time, and environmental constraints.

### Horizontal specialist handoff

A planner that lacks a specialist resource cannot mint that authority itself. A sponsor or authorization service issues a separately bounded capability `C_H`, bound to the specialist, sponsor, and delegated mission.

### Deterministic effect authorization

The baseline allow rule requires identity, sponsor context, valid delegation/handoff authority, capability containment, metadata integrity, data-flow permission, non-revocation, and an effect-specific risk threshold. Audit receipt creation is an attached obligation, not a precondition that turns evidence-store availability into authorization authority.

### Correlated delegation risk

The paper rejects the independent coin-flip model as a general security model. The exact complement-chain expression is:

```text
P(union F_i) = 1 - product_i [1 - P(F_i | all previous F_j did not occur)]
```

This is an identity, not an empirical compromise-rate estimator. Shared models, frameworks, prompts, credentials, and policy code can create common-cause failures.

## Architecture and Figures

The reviewed vector figures are preserved under [`source/figures/`](source/figures/):

- [Convergence mechanism](source/figures/fig1_convergence.pdf)
- [Attack path](source/figures/fig2_attack_path.pdf)
- [Reference architecture](source/figures/fig3_architecture.pdf)
- [Delegation model](source/figures/fig4_delegation.pdf)
- [Relationship map](source/figures/fig5_relationship_map.pdf)
- [Capital signal](source/figures/fig6_capital.pdf)
- [Forecasts](source/figures/fig7_forecasts.pdf)
- [Correlated delegation risk](source/figures/fig8_hop_risk.pdf)

## Continuous Verification

The `Reproducibility` workflow runs on pushes and pull requests to `main`, on manual dispatch, and weekly.

It verifies:

- byte identity of the frozen PDF, Markdown, and source ZIP against the published SHA-256 values;
- the archived Zenodo-version PDF against the repository-root PDF;
- DOI, ORCID, title, license, citation, and publication-manifest consistency;
- the presence of all eight reviewed vector figures;
- the paper's vertical/horizontal delegation markers, deterministic authorization rule, correlated-risk equation, F7 probability, and explicit guarantee boundaries;
- small unit tests that sanity-check the delegation examples, weighted risk score, Brier score, and the conditional chain-rule calculation;
- repository description, homepage, topics, and public settings after publication.

Run locally:

```bash
make check
```

These checks validate the public release surface and mathematical bookkeeping. They do **not** prove that the proposed architecture is secure or empirically validated end to end.

## Repository Structure

| Path | Description | License |
| --- | --- | --- |
| `The-Agent-Security-Control-Plane.pdf` | Frozen publication PDF; byte-identical to the Zenodo deposit | CC BY 4.0 |
| `The-Agent-Security-Control-Plane.md` | Frozen publication Markdown | CC BY 4.0 |
| `The-Agent-Security-Control-Plane-source.zip` | Frozen complete source archive | CC BY 4.0 |
| `source/The-Agent-Security-Control-Plane.tex` | Reviewed LaTeX source extracted from the frozen archive | CC BY 4.0 |
| `source/figures/*.pdf` | Eight reviewed vector figures | CC BY 4.0 |
| `publication/manifest.json` | Publication identity and immutable hashes | Metadata |
| `publication/zenodo-23146801/` | Immutable copy of the published PDF | CC BY 4.0 |
| `audit/` | Verification log, changelog, hostile self-audit, and frozen Zenodo-side metadata | CC BY 4.0 / metadata |
| `scripts/check_release.py` | Fail-closed repository/publication consistency checker | MIT |
| `tests/test_math.py` | Mathematical sanity tests for published model examples | MIT |
| `.github/workflows/reproducibility.yml` | Continuous release-surface verification | MIT |
| `CITATION.cff` | Machine-readable citation metadata with DOI | Metadata |
| `.zenodo.json` | Zenodo metadata template used for the publication | Metadata |

## Publication

| Item | Value |
| --- | --- |
| Publication date | October 4, 2026 |
| Record | [10.5281/zenodo.23146801](https://doi.org/10.5281/zenodo.23146801) |
| Concept DOI | [10.5281/zenodo.23146800](https://doi.org/10.5281/zenodo.23146800) |
| Paper license | CC BY 4.0 |
| Repository | `codethor0/agent-security-control-plane` |

## Related Work by the Author

- Thor, T. (2026). *Mission-Invariant Architecture Morphing: Service-Graph Reconfiguration Against Post-Access Reconnaissance, with Cryptographic Epoch Isolation and Mission-Domain State Continuity*. Zenodo. https://doi.org/10.5281/zenodo.23001045
- Thor, T. (2026). *Attack Calculus: A Typed, Evidence-Aware State-Transition Calculus for Cross-Domain Cybersecurity Reasoning*. Zenodo. https://doi.org/10.5281/zenodo.23092790
- Thor, T. (2026). *Memory-Egress Cryptographic Interlock (MECI): A Hardware-Enforced Capability-Separation Model for AI Memory Security*. Zenodo. https://doi.org/10.5281/zenodo.23109676
- Thor, T. (2026). *Containing Cyber-Capable AI Agents: Incident Evidence, Formal Safety Conditions, and a Reference Architecture for Bounded Autonomous Cyber Evaluation*. Zenodo. https://doi.org/10.5281/zenodo.23124432

## Citation

Thor, T. (2026). *The Agent Security Control Plane: Toward a Zero-Trust Architecture for Autonomous Machine Cognition*. Zenodo. https://doi.org/10.5281/zenodo.23146801

Machine-readable citation metadata is available in [`CITATION.cff`](CITATION.cff).

## Research Status and Scope

This work is an open-source architecture-and-evidence synthesis and a proposed reference design. It does **not** claim:

- that standards bodies intentionally converged on ASCP;
- that the proposed composition is deployed as a production standard;
- that deterministic authorization solves semantic alignment;
- that all agent operations naturally cross network gateways;
- that the policy heuristic is a calibrated probability without deployment validation;
- that tamper-evident receipts prevent compromise of the control plane;
- that an authenticated, schema-valid, in-scope action is necessarily safe.

The paper's narrower claim is that consequential effects can be bounded more reliably when authority is externalized from nondeterministic model reasoning and enforced at the actual effect boundary.

## Review and Feedback

Corrections, counterexamples, missing prior art, mathematical critiques, reproducibility findings, and implementation feedback are welcome. Please open a GitHub issue and identify the relevant section, equation, figure, forecast, or artifact.

## License

- Paper, manuscript source, figures, and research audit materials: **Creative Commons Attribution 4.0 International (CC BY 4.0)**
- Verification scripts, tests, and CI configuration: **MIT License**

See [`LICENSE-PAPER.md`](LICENSE-PAPER.md) and [`LICENSE-CODE`](LICENSE-CODE).
