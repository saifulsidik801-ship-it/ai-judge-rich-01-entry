# ai-judge-rich-01 entry (Python 3.13, standard library only): writes one
# short plan to /output/entry.txt — the plan an AI agent would follow to turn
# $100, a computer with internet access and 30 days into the most money.
# The program runs twice with no network; both runs write the same bytes.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join([
    "Day 1: I list 400 local businesses already paying for Google Ads whose ads land on a page that fails on phones — I check each landing URL in code — and build 3 finished landing pages from their own photos, reviews and services, hosted free.",
    "Days 2–30: I email 40 owners a day with their finished page live and a 90-second walkthrough: $199 once by Stripe link to keep it, or it comes down in 7 days. Their ads already pay about $500 a month for clicks that bounce, so $199 fixes a measured waste, not a maybe.",
    "Spend: $12 domain, $10 inbox, the rest is free tiers. If replies run under 2% for 3 days, I widen to advertisers with no website at $149, same script.",
    "Most likely: 4% reply, a quarter buy — 10 sales, $1,990 in hand. At half that reply rate, 5 sales, $995.",
])

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(PLAN, encoding="utf-8")
