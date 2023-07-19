# Poor man's JSON lines viewer

Very simple, Python based utility to help inspecting [JSON Lines](https://jsonlines.org/) files (text format where each line is a single JSON construct).
For those situations or environments where you can not or do not want to install/use a more powerful tool.


## Suggested usage

Pass JSON lines through standard input, specify which fields to render as command line arguments, and pipe the output to `less -S` to interactively scroll (up/down/left/right) through your data:

    python poormans-jsonl-viewer.py levelname name message < logs.jsonl  | less -S


## "Installation"

Requirements are very light: 
it only needs Python 3.6 or higher
and just uses a couple of modules from the Python standard library.

Download`poormans-jsonl-viewer.py` and put it where it suits you.
