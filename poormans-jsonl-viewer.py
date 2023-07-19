import json
import logging
import sys


_log = logging.getLogger("poormans-jsonl-viewer")


def main():
    logging.basicConfig(level=logging.WARNING)
    fields = sys.argv[1:]
    if not fields:
        raise RuntimeError("Specify which fields to render.")
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            data = json.loads(line)
        except Exception as e:
            _log.warn(f"Failed to parse {line}: {e}")
        values = [data.get(f) for f in fields]
        print("\t".join(repr(v) for v in values))


if __name__ == "__main__":
    main()
