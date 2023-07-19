# Poor man's JSON lines viewer

Very simple, Python based utility to help inspecting [JSON Lines](https://jsonlines.org/) files (text format where each line is a single JSON construct).
For those situations or environments where you can not or do not want to install/use a more powerful tool.


## Suggested usage

Pass JSON lines through standard input,
specify which fields to render as command line arguments,
and pipe the output to `less -S` to interactively scroll (up/down/left/right) through your data:

    # Classic `cat` piping
    cat logs.json | python poormans-jsonl-viewer.py levelname name message | less -S

    # Or more efficiently:
    python poormans-jsonl-viewer.py levelname name message < logs.jsonl | less -S


`poormans-jsonl-viewer.py` will print tabs between field values,
so they align a bit in poor man's columns by default.

For real column rendering, leverage the [`column` tool](https://github.com/util-linux/util-linux),
for example as follows
(assuming a Bash-like shell here to specify the tab character
with [ANSI-C quoted](https://www.gnu.org/software/bash/manual/html_node/ANSI_002dC-Quoting.html) `$'\t'`):

    python poormans-jsonl-viewer.py levelname name message < logs.jsonl | column -t -s $'\t' | less -S


## "Installation"

Requirements are very light:
only Python 3.6 or higher is required
(the tool only uses a couple of modules from the Python standard library).

Download `poormans-jsonl-viewer.py` and put it where it suits you.
