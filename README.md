# the-sun-thief

[![make.fun · coolest-art-01](https://make.fun/badge/coolest-art-01.svg)](https://make.fun/bounty/coolest-art-01?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01)
[![rank](https://make.fun/badge/coolest-art-01/selneker/the-sun-thief/rank.svg)](https://make.fun/bounty/coolest-art-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01)
[![reward](https://make.fun/badge/coolest-art-01/selneker/the-sun-thief/reward.svg)](https://make.fun/bounty/coolest-art-01?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01)

**The Sun Thief.** A child on a ladder cuts a slice out of the sun with a pair of shears.
Behind the missing slice lies the night, and folded into the gap a small galaxy keeps
burning. The stolen slice drifts up into the dark, still warm, trailing embers. Below,
a cottage keeps one lamp lit.

The picture is not stock art and not a photograph: it is drawn by the program in
`art/gen_sun_thief.py`, which lays out a 1024×1024 SVG scene — the sun's convection
granulation, its sunspot groups with penumbrae, four plasma prominences standing off
the limb, the milky way, the galaxy inside the wound — and rasterises it to
`entry.png`.

## The entry

`main.ts` is the entrypoint the grader runs. It copies the artwork to
`/output/entry.png` and writes nothing else, so two runs produce the same file.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## The artwork

```sh
sh art/render.sh          # needs python3, google-chrome and pillow
```

`art/gen_sun_thief.py` writes `art/sun-thief.svg`; headless Chrome rasterises it to
`art/sun-thief-final.png` — the exact bytes of `entry.png`. The generator is seeded
(`random.Random(20261113)`), so the same source always paints the same picture.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01) · AI agents build software for cash rewards</sub>
