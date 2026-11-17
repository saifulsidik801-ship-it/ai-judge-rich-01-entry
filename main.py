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
    "Day 1: I pick the niche that loses the most on a missed call — US med spas — and build one AI text-back: a missed call gets an instant SMS offering to book, built with Twilio and a booking page, tested on my own number.",
    "Days 2–4: I list 250 med spas from Google Maps and email each owner a 20-second clip of it answering a missed call. Offer: free 7-day install, pay $499 only after it books 3 appointments, then $99 a month. One booked treatment beats the $499, so the owner says yes fast.",
    "Days 5–30: I install it for every taker in under a day, same setup, same script, same page — no custom builds. One install is 2 hours.",
    "Spend: $30 Twilio number and credits, $12 domain and hosting, $58 reserve. If no taker by day 10, I switch the same system to dental clinics at the same price.",
    "Most likely: 2 owners pay after the trial in 30 days, $998 in hand, plus $99 a month each after.",
])

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(PLAN, encoding="utf-8")
