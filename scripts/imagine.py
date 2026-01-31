#!/usr/bin/env python3
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path

def generate_image(api_key, prompt, model, out_path):
    url = "https://api.x.ai/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "prompt": prompt,
        "n": 1,
        "response_format": "url"
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            image_url = res_data["data"][0]["url"]
            
            # Download the image
            urllib.request.urlretrieve(image_url, out_path)
            print(f"MEDIA:{out_path}")
            return True
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.read().decode('utf-8')}", file=sys.stderr)
        return False
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
