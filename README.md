# grok-imagine

A Clawdbot skill for generating images using xAI's Grok Imagine API (Flux-based).

## Installation

1. Copy this folder into your Clawdbot `skills/` directory.
2. Ensure you have `python3` installed.
3. Set your `XAI_API_KEY` in your environment or `clawdbot.json`.

## Usage

```bash
imagine a hyper-realistic crystal ghost in a rainy Manchester pub
```

Or manually:

```bash
python3 scripts/imagine.py --prompt "your description" --out ./output.jpg
```

## License

MIT
