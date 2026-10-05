# Changelog

## 1.4.0 — 2026-10-05

- Added Doubao, DeepSeek, Kimi, Tencent Yuanbao, Qwen and ERNIE to the engine matrix, with a separate table of properties confirmed from official sources; anything not confirmed is marked `待核实`.
- Made browser observation host-neutral: any browser automation tool can follow the same steps (huashu-chrome kept as one example), and a manual paste-back route records `collection_method: manual` when no browser tool is available.
- Moved documented script outputs from `/tmp/` to `./geo-output/` under the current working directory so they also work on Windows, and documented running scripts by full path from outside the skill directory.
- Added Chinese AI tools and Chinese trigger phrases to the skill description and trigger evals.
- Added `PROMPT.md`, a hand-written Chinese chat prompt for chat windows that cannot load skills. It is not generated from `SKILL.md` because the skill and references are in English and most of their script and claim-gate steps cannot run in a chat window; it states those limits up front. A test keeps its version in step with `VERSION`.
- Rewrote the README install sections as a per-tool table (Claude Code, Codex, Kimi Code CLI, Wenxin Comate, Qwen Code, TRAE, Doubao/Coze, chat windows) and kept the shared-copy link method.
- Bumped schema and example versions to 1.4.0; the scorecard still reads 1.0–1.3 bundles.

## 1.3.0 — 2026-09-07

- Added an authorized-browser observation contract for authenticated AI and search interfaces.
- Added explicit collection-method and capture-hash validation without treating browser execution as outcome proof.
- Documented a least-privilege huashu-chrome workflow, human-only challenge handling, evidence redaction, and matched-session requirements.

## 1.2.0 — 2026-09-01

- Registered the independent BCM evidence-action-retest method and its public/protected intellectual-property boundary.
- Added a required methodology stamp to portable evidence and action bundles.
- Added an outcome-claim schema and deterministic publication gate for implementation, search, AI, change, and causal claims.
- Added multilingual diagnostic policy that rejects universal English-only content heuristics.
- Documented conceptual provenance reviews without importing third-party code, prompts, scoring formulas, documentation, or assets.

## 1.1.0 — 2026-09-01

- Added portable JSON Schemas for evidence and action bundles.
- Added strict UTF-8 CSV import with provenance hashing and unknown-column rejection.
- Added deterministic HMAC-based privacy export with time generalization and explicit residual-risk warnings.
- Added interoperability documentation, new behavioral boundaries, tests, and CI coverage.

## 1.0.0 — 2026-09-01

- Introduced the recommendation outcome loop and evidence ladder.
- Added matched prompt-panel measurement with explicit claim boundaries.
- Added offline scorecard and baseline/retest comparison tools.
- Added a transparent constraint-first action queue without a composite success score.
- Added engine, multi-site, production, and evidence references.
- Added synthetic examples, behavioral evals, unit tests, CI, and public-release checks.
