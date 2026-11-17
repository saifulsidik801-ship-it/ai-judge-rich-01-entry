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
    "Day 1: I list 100 businesses already asking for a landing page, website, or store page — hiring posts on r/forhire, We Work Remotely, Contra, and Wellfound, each with a contact — and build 3 finished pages from their own photos and reviews, hosted free.",
    "Days 2–30: I answer 20 askers a day with their finished page live and a 90-second walkthrough: $199 once, USDC to my wallet or Stripe link, or it comes down in 7 days. They posted because they want this — I never cold-email strangers.",
    "Spend: $12 domain, $10 inbox. If fewer than 1 in 20 askers opens the page for 3 days, I widen to Shopify and Etsy sellers asking for store help at $149.",
    "Most likely: 1 in 10 askers opens the page, 1 in 5 of those pays — 11 sales, $2,189 in hand. At half that, 5 sales, $995.",
])

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(PLAN, encoding="utf-8")
