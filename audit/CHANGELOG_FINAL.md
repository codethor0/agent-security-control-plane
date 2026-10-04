# Final Post-Audit Changelog

This is a surgical post-audit polish pass. No core thesis, forecast probability, financing total, identity metadata, or diagram topology was changed.

1. Replaced the awkward phrase “an eight-diagram reference architecture and threat model” with “a reference architecture and threat model supported by eight diagrams.”
2. Marked **semantic routing hijack** explicitly as proposed vocabulary used by this paper, not an established AppSec term.
3. Added classical capability-security grounding to Related Work and to the horizontal-handoff model, while explicitly distinguishing ASCP policy capabilities from pure object-capability systems.
4. Clarified that the four ASCP planes are logical security roles, not mandatory microservices or four required network hops.
5. Expanded complete-mediation deployment guidance: high-impact local effects can be forced through typed brokers or OS isolation controls; a direct bypass path means mediation has failed.
6. Added component-level empirical evidence from FIDES: AgentDojo attacks were stopped under its policy checks, with roughly 2–3× average token utilization relative to a Basic planner. The manuscript still makes no end-to-end ASCP benchmark claim.
7. Made the control-plane compromise mitigation pattern more concrete: distinct principals, signed/versioned policy artifacts, PEP policy binding, controlled policy changes, and restrictive fallback on PDP/policy disagreement.
8. Added a short rationale for F7's frozen P = 0.60 probability.
9. Added reference [48], Miller, Yee, and Shapiro, *Capability Myths Demolished* (2003).
10. Verified that the second-cycle reports of broken [2]/[6]/[8] URLs, malformed Axios URL, incorrect Citibank title, corrupted Figure 6, incomplete P1, and F7 = 0.66 do **not** exist in the current 39-page source/render. Those were source-version or extraction artifacts, so no false “correction” was applied.
11. Third-cycle citation hardening: reference [2] now includes both the canonical MCP 2026-07-28 specification URL and the maintainers' release-note URL, eliminating ambiguity between the normative specification and release commentary.
12. Third-cycle verification confirmed that the reported Figure 6 caption corruption, P1 truncation, missing Section 12.6, vulnerability-table loss, and malformed reference URLs are not present in the current 39-page render/source; no unnecessary prose edits were made.
