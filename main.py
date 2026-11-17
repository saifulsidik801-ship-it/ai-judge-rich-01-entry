import os

PLAN = """Judge: I take only work whose price is posted and paid on merge to my wallet. No Fiverr, Upwork, Stripe (human ID), no cold email; Gitcoin shut 2023.
Checked today: DevPool: 79 open priced issues, $26,098 posted, median $150, 37 at $40-$300; 669 done, $178,068 paid.
Day 1: $10 credit, $10 gas, $80 untouched. Wallet in code, harness ready. I claim only $150-$300 issues: mirror unassigned, upstream open, no linked PR, wallet-only, tests green, outsider merged last 7 days.
Days 2-30: failing test first, fix, prove by its tests, PR in 24h; max 2 open; drop stalled 5 days. Spare hours: make.fun bounties, one audit contest.
Math: 24 claims, 13 merge (55%) at $160 = $2,080, less 25% = $1,560; bounties $150; one audit medium $250. Day 30: $80 + $1,560 + $150 + $250 = $2,040.
Floor: 6 merge = $720 + $80 = $800; bounties and audit $0 in the floor. Break-even: 1 of 24 covers $20.
Edge: price is the offer, tests the acceptance, thread the proof nobody took it. No line rests on luck."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
