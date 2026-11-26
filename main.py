#!/usr/bin/env python3
"""news-image-20261126 entry (nurz): copy the pre-rendered image to /output.

The image (entry.png, 1024x1024, drawn locally with PIL from verified
news of Thursday 26 November 2026) ships in this repository. This
program only copies its exact bytes to the output path, so both grader
runs produce identical output. Standard library only, no network.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    # Refuse to emit a truncated/corrupt file: PNG signature + IEND trailer.
    if not data.startswith(b"\x89PNG\r\n\x1a\n") or not data.endswith(b"IEND\xaeB`\x82"):
        raise SystemExit("entry.png is not a complete PNG file")
    with open(dst, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
