#!/usr/bin/env python3
import argparse
import os
import sys
import urllib.request
from pathlib import Path
from xai_sdk import Client

def generate_image(api_key, prompt, model, out_path):
    try:
        client = Client(api_key=api_key)
        response = client.image.sample(
            model=model,
            prompt=prompt,
            image_format="url"
        )
        image_url = response.url
        # Download the image
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        req = urllib.request.Request(image_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(out_path, "wb") as f:
                f.write(response.read())
        print(f"MEDIA:{out_path}")
        return True
    except Exception as e:
        print(f"Failed: {str(e)}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Grok Imagine Image Generation")
    parser.add_argument("--prompt", "-p", required=True, help="Image prompt")
    parser.add_argument("--out", "-o", default="./grok-imagine.jpg", help="Output path")
    parser.add_argument("--model", default="grok-imagine-image", help="Grok model")
    parser.add_argument("--api-key", help="XAI API Key")
    
    args = parser.parse_args()
    
    api_key = args.api_key or os.environ.get("XAI_API_KEY")
    if not api_key:
        print("Error: Missing XAI_API_KEY environment variable.", file=sys.stderr)
        sys.exit(1)
        
    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    if generate_image(api_key, args.prompt, args.model, str(out_path)):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
