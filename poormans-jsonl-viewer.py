import collections
import json
import logging
import sys

_log = logging.getLogger("poormans-jsonl-viewer")


def main():
    logging.basicConfig(level=logging.INFO)
    fields = sys.argv[1:]
    stats = collections.Counter()
    if not fields:
        raise RuntimeError("Specify which fields to render.")
    try:
        for line in sys.stdin:
            stats["lines read"] += 1
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except Exception as e:
                _log.warn(f"Failed to parse {line!r}: {e}")
                stats["parse errors"] += 1
                continue
            finally:
                values = [data.get(f) for f in fields]
                print("\t".join(repr(v) for v in values))
                stats["entries shown"] += 1
    finally:
        _log.info(f"Stats: {stats}")


if __name__ == "__main__":
    main()
