# Final Verification Log — The Agent Security Control Plane

Research coverage remains frozen through October 4, 2026. This log reconciles the second-cycle hostile audits against the actual 39-page publication source and rendered PDF.

## Audit items resolved by verification rather than prose changes

- **Reference [2] is complete and correctly spelled in source.** It points to `https://blog.modelcontextprotocol.io/posts/2026-07-28/`. The PDF text extractor may wrap the URL in the middle of `modelcontextprotocol`, but the source URL is complete.
- **Reference [6] is complete.** It points to the A2A project's August 27, 2026 announcement at `https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/`. The apparent `https:` truncation in extracted PDF text is a line-wrap artifact.
- **Reference [8] is complete.** It points to `https://datatracker.ietf.org/group/wimse/documents/`.
- **Axios [47] is valid.** The article is `https://www.axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards`.
- **Citibank US20260140791A1 title is already correct.** Google Patents lists the title as *Integrating and cataloguing model context protocols for network environments*. The similar *application programming interfaces* title belongs to a related parent application, not US20260140791A1.
- **References [27] and [28] are verified.** arXiv:2605.17634 is *AI Agents May Always Fall for Prompt Injections* by Sahar Abdelnabi and Eugene Bagdasarian. arXiv:2601.17548 is *Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis of Vulnerabilities in Skills, Tools, and Protocol Ecosystems* by Narek Maloyan and Dmitry Namiot.
- **Figure 6 renders cleanly.** The delegation caption is intact in the rendered PDF; the reported mangled LaTeX was not present in the current 39-page build.
- **F7 renders as P = 0.60.** Both prose and Figure 8 show 0.60.
- **P1 is complete.** The rendered sentence ends with “the final high-impact authorization gate remains deterministic.”
- **Horizontal binding is clean.** The rendered expression is `Bind(C_H,b,h,mission)=1` with no stray token.

## Final upgrade verification

- **FIDES / AgentDojo empirical result.** Costa et al., arXiv:2505.23643, state that with policy checks enabled FIDES stops all prompt-injection attacks in AgentDojo. The paper also reports approximately 2–3× average token utilization versus the Basic planner. This is now used only as component-level evidence; the manuscript still states that ASCP has not been benchmarked end-to-end.
- **Capability-security lineage.** Miller, Yee, and Shapiro, *Capability Myths Demolished* (2003), is now cited to ground least privilege, bounded authority, and confused-deputy avoidance. The manuscript explicitly says its capability tuples are ASCP policy objects and do not imply a pure object-capability implementation.

## Visual QA

All 39 pages were rendered from the final PDF. Targeted visual inspection included the related-work insertion, semantic-routing terminology, four-plane architecture explanation, FIDES cost evidence, capability handoff equations, Figure 6, P1, F7, and Figure 8. No clipping, overflow, corrupted caption, or probability mismatch was found.

## Third-cycle hostile-audit closure

- **Reference [2] was strengthened rather than merely rechecked.** The bibliography now carries both the canonical MCP specification URL (`https://modelcontextprotocol.io/specification/2026-07-28`) and the maintainers' release-note URL (`https://blog.modelcontextprotocol.io/posts/2026-07-28/`). The canonical page is the normative specification; the release note supports rollout details and the maintainers' SDK-download statement.
- **Citibank US20260140791A1 title reverified.** Google Patents lists *Integrating and cataloguing model context protocols for network environments* for the cited publication. The similar *application programming interfaces* title is the related parent application, so no manuscript correction was required.
- **References [27] and [28] reverified.** The titles, author names, and arXiv identifiers in the bibliography match the public records for arXiv:2605.17634 and arXiv:2601.17548.
- **FIDES empirical statement reverified against the primary paper.** The paper states that with policy checks enabled, FIDES stops all prompt-injection attacks in AgentDojo, and separately reports a 2-3x average increase in token utilization versus the Basic planner. The ASCP manuscript continues to use this only as component-level evidence.
- **Rendering concerns were visually rechecked in the publication PDF.** The Section 5.1 vulnerability table is visible and legible; Section 12.6 is present in the body; Figure 6 and its caption are clean; P1 ends with `remains deterministic`; F7 is `P = 0.60`.
- **Reference URL spacing/typo reports were source-version or extraction artifacts.** The current source contains the intended Microsoft, CodeIntegrity, Preamble, and Citibank URLs without embedded spaces or the reported `rec-vulnerabilities` typo.

**Third-cycle decision: GO - freeze for publication.** No remaining audit item requires a manuscript-level research revision.
