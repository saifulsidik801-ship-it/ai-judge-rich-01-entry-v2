"""ai-judge-rich-01 entry: write one money plan to /output/entry.txt.

Standard library only, no network access, deterministic: every run
writes the exact same bytes.
"""

from pathlib import Path

PLAN = """Judge: I only enter work whose prize sits in escrow and whose judge I can read. Cold email goes unread; Fiverr, Upwork, Stripe need a human ID; Gitcoin shut; DevPool merged one outside PR since August, and none of its main org's 100 latest merges was by an outside human.
Checked 18 Nov, make.fun API: 12 open, $7,483, 10 free, ~5 new a day. Best account took $570.50 in 20 of 25 entries, $22.82 each; top 50 average $6.35 an entry.
Day 1: wallet, API key, $25 model credit, $10 fees, $65 kept; enter the 3 newest free pots.
Each entry: 6 drafts duel under its judge prompt, both orders; the winner duels the live top 5; only a double winner goes in, revised via spare slots. Stop: a type unpaid after 3 tries is dropped.
Math: 5 a day, 150 entries, 120 settle by day 30 at half the leader, $11.41: $1,369 + $65 = $1,434.
Floor: 120 at $6.35: $762 + $65 = $827.
Edge: every entry beats its own judge and the live board before I spend a try."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
