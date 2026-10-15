# TYPECHECK.md — GATE T

Reel: `claude-liam-houseghost-a3-gamedev`  |  Checked: 2026-10-15T17:17  |  Overall: PASS  |  Beats checked: 44  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B01] narration recites the card (0.95) — discuss it, don't read it
> - §8.10 [B36] narration recites the card (0.89) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | — | no video | SKIP | — |
| B16 | ? | — | no video | SKIP | — |
| B17 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | ? | — | no video | SKIP | — |
| B20 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B26 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B27 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B28 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B32 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | ? | — | no video | SKIP | — |
| B34 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B35 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B36 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B37 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B38 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B39 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B40 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B41 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B42 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B43 | ? | dark | min-size §8.1: min text-run height 52px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 29 | 0 |
| min-size §8.1 | 39 | 0 |
| overflow §8.2 | 39 | 0 |
| contrast §8.3 | 39 | 0 |
| contrast-local §8.3b | 39 | 0 |
| bbox-overlap §8.6b | 39 | 0 |
| card-clip §8.13 | 39 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 7 | 2 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
