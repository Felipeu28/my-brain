---
tags:
  - graph/spoke
---
# Local AI Inference (Mac Silicon)

**Type:** concept (infrastructure)
**Last updated:** 2026-04-12
**Source:** [[raw/x-bookmarks-2026-04-11 copy]]
**Related:** [[wiki/concepts/brain-architecture]], [[wiki/concepts/openclaw-hermes]]

---

## Summary
Running full AI models locally on Apple Silicon (M1/M2/M3/M4) chips using MLX — Apple's machine learning framework optimized for unified memory. The March–April 2026 bookmark period marked a real inflection: Gemma 4 was available on MLX on day 0, Qwen3.5 27B runs near-Opus quality locally, and community creators are building their entire AI workflows on $600 Mac Minis.

## Key Signals from Bookmarks

### Models That Now Run Locally on Apple Silicon
- **Gemma 4 (vision/audio/MoE)** — MLX + mlx-vlm v0.4.3, day-0 support (@neural_avb, Apr 2)
- **Qwen3.5 27B** — near-Opus-level locally on Mac Mini (@TheCraigHewitt, Apr 1, 447K views)
- **LFM2.5-350M** — Liquid AI's tiny agentic model: reliable agent loops at only 350M parameters (@liquidai, Mar 31, 340K views)
- **Falcon-OCR, Granite 4.0, SAM 3.1, RF-DETR** — all MLX-supported in the same mlx-vlm release

### Running AI on MacBook Air M4 16GB (Fully Offline)
@kimmonismus (Apr 3): "Running a full AI assistant locally on a MacBook Air M4 with 16GB, completely offline — free, open source" using OpenClaw + Gemma 4. Tagged as a paid partnership but the technical claim is real.

### LFM2.5-350M — The Tiny Agentic Model
Liquid AI's 350M parameter model is notable because it runs reliable agentic loops at extremely small size. Implications:
- Could run on edge devices (phones, embedded)
- Near-zero inference cost at scale
- Opens path to always-on background agents with no meaningful compute cost

## Privacy Implications
Local inference = zero data egress. All processing stays on device. For the Moil Brain specifically: emails, contacts, calendar data, and business intelligence never leave the Mac Mini M4. This is the entire privacy posture of the Brain architecture per `~/My Brain/CLAUDE.md`.

## Connection to Moil Brain Architecture
Per memory notes: the Brain runs Qwen 2.5 Coder 7B MLX as primary (tool use / code) and Qwen 3.5 9B for non-tool reasoning — both on the M4 Mac Mini's MLX stack. The Gemma 4 day-0 support from @neural_avb is directly relevant: there may be headroom to upgrade the primary model as MLX efficiency improves.

## Connections
- Powers the local inference layer of [[wiki/concepts/brain-architecture]]
- Enables [[wiki/concepts/openclaw-hermes]] to run on local models (no Anthropic API cost)
- LFM2.5-350M is worth monitoring for Moil's future embedded/edge agent needs

## Moil Relevance
The Mac Mini M4 as an AI workstation is now validated by multiple community builders. The key constraint for Moil Brain (16GB RAM) is real — Gemma 4 26B-A4B doesn't fit, which is why the Brain uses Qwen 7B/9B. The LFM2.5-350M signal suggests a near-future where very capable agentic loops run in a fraction of the RAM, removing the hardware ceiling.

**Watch:** @neural_avb for MLX model drops. @TheCraigHewitt for local inference benchmarks.
