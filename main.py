"""Turned Off for Good.

For years the tech on the helpdesk has had exactly one answer for
everything: turn it off and on again. Now he is quitting, and the
punchline writes itself — he runs his own fix one last time, except
there is no "on again" waiting at the end of it. The gag is that the
man who kept rebooting everyone else's machines has finally rebooted
himself, permanently. This program writes that one-line resignation
to the output file, exactly as the gate demands: a single line, no
trailing newline.
"""

import os

ENTRY_LINE = "I resign effective today: I have turned it off and on again for the last time — this time, the thing staying off is me."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Gate: exactly one line, no trailing newline — write the constant as-is.
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
