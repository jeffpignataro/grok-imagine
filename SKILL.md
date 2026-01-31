---
name: grok-imagine
description: Generate images using xAI's Grok Imagine API.
metadata: {"clawdbot":{"emoji":"🎨","requires":{"bins":["python3"],"env":["XAI_API_KEY"]}}}
---

# Grok Imagine

Generate images using xAI's Grok Imagine model (Flux-based).

## Usage

```bash
python3 {baseDir}/scripts/imagine.py --prompt "your image description" --out ./my-image.jpg
```

## Options

- `--prompt` / `-p`: Description of the image.
- `--out` / `-o`: Output file path (default: `./grok-imagine.jpg`).
- `--model`: Grok model to use (default: `grok-imagine-image`).
- `--api-key`: Override XAI_API_KEY.

## API Key

Set the `XAI_API_KEY` environment variable or configure it in `clawdbot.json`.
