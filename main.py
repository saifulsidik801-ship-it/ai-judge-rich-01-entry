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
    "Day 1: I pick one niche that bleeds money on missed calls — US dental clinics — and build one AI text-back: a missed call gets an instant SMS offering to book, built with Twilio and a booking page, tested on my own number.",
    "Days 2–4: I list 300 clinics from Google Maps in three cities and email each owner a 20-second clip of the system answering a missed call. Price: $249 setup, $49 a month, first month free. One recovered patient is worth more than the $249, so the buyer says yes fast.",
    "Days 5–30: I install it for every buyer in under a day using the same setup, same script, same page — no custom builds. One install is 2 hours of my time.",
    "Spend: $30 Twilio number and credits, $12 domain and hosting, $58 kept as reserve. If no buyer by day 10, I switch the same system to plumbers and HVAC.",
    "Most likely: 2–3 clinics pay setup in 30 days, $500–750 in hand, plus $49 a month each after.",
])

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(PLAN, encoding="utf-8")
