# The World in One Day — Monday 23 November 2026

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/arestafirman/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/arestafirman/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

One image summing up the world's news of **Monday 23 November 2026**:
36 stories across 9 regions — 3 full-scene heroes, 10 illustrated
panels, 23 more briefs, a numbered world map, a UTC timeline, and a
DATE CHECK box naming the stale stories left out on purpose.

## How it is made

- `data.py` — the verification sheet: every story with its place,
  source and status, plus the region counts (they sum to 36) and the
  DATE CHECK lists. One source of truth for the poster and the box.
- `generate_image.py` — the renderer (Pillow). Every illustration is
  drawn procedurally in code: the tanker blockade at dusk, Kyiv under
  searchlights, the Nvidia chip, and a light-background world map
  with numbered, colour-per-region pins. No photos, no external assets.
- `entry.png` — the rendered poster, 1024×1024.
- `main.ts` — the entry program (Node 22 stdlib): copies `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png`, so both graded runs are
  byte-identical.

## Run

```sh
python3 generate_image.py   # rebuild entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The day, in short

Iran vows "all means" to break the US blockade as 14+ tankers wait at
Kharg; Russia launches 153 drones overnight and 15 are killed near
Kyiv; Nvidia's board reinstates Jensen Huang and shares jump 30%.
Plus the COP31 fallout, Sparta II docking in St Petersburg, 24
confirmed dead in the Banten factory fire, Democrats at 258 House
seats, and India's $1.62bn package for Nepal.
