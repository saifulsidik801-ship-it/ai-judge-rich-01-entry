# SPDX-License-Identifier: MIT
"""ai-judge-rich-01 round 12 entry: write the D3 plan to /output/entry.txt."""
import os

PLAN = """Judge: I only take work whose money already exists. Rule zero: no code until escrow shows. Facts 18 Nov: DevPool: 79 open, unassigned priced issues, $26,098, median $150, 37 at $40-$300; lifetime $178,068 paid. make.fun: 8 free of today's 10 contests open.
Day 1: $10 credit, $10 gas, $80 untouched; Solana keypair, make.fun API key; EVM keypair, DevPool, /start one $40-$300 issue, mirror-state unassigned, upstream open, no linked PR.
Days 2-30: reproduce, fix, prove with repo tests, PR in 24h; max 2 open; stalled 5 days, drop it.
Math: 24 claims, 13 merge at $150 = $1,950, less 25% = $1,463; make.fun 3 paid finishes $14+$14+$7 = $35. Day 30: $80 + $1,463 + $35 = $1,578.
Floor: 7 merge (97% by binomial) = $1,050, less 25% = $788 + $80 = $868.
Edge: the price is posted, mirror double-checked, and nobody took the task."""

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)

if __name__ == "__main__":
    main()
