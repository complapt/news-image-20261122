# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/complapt/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/complapt/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

## The picture

One 1024×1024 PNG that sums up Sunday 22 November 2026 as a newspaper front page: a masthead, a UTC timeline and a numbers strip, a three-column hero, ten picture cards, a dotted world map with numbered pins, twelve briefs grouped by region, and a DATE CHECK box that says plainly what was left out and what is not yet known. The three leads:

1. **COP31 collapses** — the climate talks in Antalya end with no deal at all after the EU walks out over a draft that never mentions fossil fuels; 44 hours of overtime, zero agreements.
2. **Iran strikes Bahrain** — missiles and drones hit US bases and a civilian plant on Sitra island; two people are injured, one critically. Iran's claim that it destroyed US Patriot radars is unconfirmed.
3. **Markets fall** — the S&P 500 closes Friday down 3.7% and the Nasdaq 5.3% as the AI sell-off spreads to Japan and Korea; Wall Street is in correction.

The ten pictures: a Kyiv apartment hit with 14 missing; the capture of cartel boss "El Chapo Isidro" in Mexico; new Houthi strikes; the World Court finding Myanmar guilty of Rohingya genocide; an EU–Indonesia trade deal; a candy-factory fire in Cikande with 36 workers missing; South Korea's education minister resigning over an AI exam scandal; the FBI probing a breach of its NCIC database; Verstappen winning the Las Vegas Grand Prix; and NATO's chief vowing to defend Poland. Twelve briefs round out the day, from BepiColombo reaching Mercury orbit to GTA VI's $3.79B launch day. Every fact comes from reporting published on 22 November 2026 (AP, Reuters, AFP, Al Jazeera, BBC, IPS, ESA). Timeline times are UTC; each story carries an honest certainty label — CONFIRMED, OFFICIALS or REPORTED — explained in the legend.

## How the picture was made

`build_image.py` draws the poster with Pillow only: flat shapes, no photos, no network, fully deterministic — run it twice and the bytes are identical. `main.py` loads the finished PNG, checks its magic bytes, its 1024×1024 size and its sub-1-MiB weight, writes it to the output directory, then reads the copy back and compares it byte for byte so a bad write fails loudly instead of passing silently.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=she012c7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
