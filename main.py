"""Write the two-sentence horror entry to entry.txt."""

import hashlib
import os
from pathlib import Path

LINE = "The grocery delivery photo shows my bags on the porch at noon. Through the kitchen window behind them, someone is washing dishes in my sink."
CHAR_LIMIT = 400


def validate(entry_path: Path) -> None:
    data = entry_path.read_bytes()
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"
    assert b"\n" not in data, "entry must be a single block without newlines"
    assert b"\r" not in data, "entry must not contain carriage returns"
    text = data.decode("utf-8")
    assert 1 <= len(text) <= CHAR_LIMIT, "entry length out of range"
    assert text == text.strip(), "entry must not have leading or trailing whitespace"
    terminators = sum(text.count(c) for c in ".!?")
    assert terminators == 2, "entry must contain exactly two sentence terminators"
    assert text.endswith("."), "entry must end with a period"
    assert text == LINE, "entry content must match LINE"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_bytes(LINE.encode("utf-8"))
    validate(entry_path)
    print(hashlib.sha256(LINE.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
