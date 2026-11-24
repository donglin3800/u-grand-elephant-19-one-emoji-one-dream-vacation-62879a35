#!/usr/bin/env python3
"""One Emoji, One Dream Vacation -- Mount Fuji.

The dream here is not "a beach somewhere". It is one mountain,
seen at first light: snow on the cone, a clear sky, the climb
everyone pictures when they say Japan. A single postcard image
that names a particular trip instead of any holiday at all.

The program's only job is to hand that one picture to the judge,
exactly as it is, with nothing added.
"""

from pathlib import Path

# U+1F5FB MOUNT FUJI -- one code point, four UTF-8 bytes.
DREAM = "\U0001F5FB"


def entry_path() -> Path:
    import os

    base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return base / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # No newline, no spaces, no trailing bytes: the gate reads
    # 1 to 8 characters, and the entry is a single emoji alone.
    target.write_bytes(DREAM.encode("utf-8"))


if __name__ == "__main__":
    main()
