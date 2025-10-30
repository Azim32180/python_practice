#!/usr/bin/env python3
"""Print a chosen emoji and optional message from the command line."""

import argparse
from emoji import emojize
from rich import print

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Display an emoji with an optional message") # TODO:replace None with a helpful description of the function
    parser.add_argument("--name", default=":rocket:", help="The emoji name in :alias: format") # TODO: default like ":rocket:" and a clear help string
    parser.add_argument("--msg", default="", help="The message to display alongside the emoji") # TODO: default empty string and clear help
    return parser
def render_emoji(name: str, msg: str) -> str:
    """Return the combined emoji + message string."""
    symbol = emojize(name, language="alias") # DO NOT Change this
    output = f"{symbol} {msg}".rstrip() # TODO: build f-string combining symbol + msg (strip trailing spaces)
    return output
def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    # TODO: ensure args.name and args.msg become strings
    name = str(args.name)
    msg = str(args.msg)
    result = render_emoji(name, msg)
    print(result)
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
    
