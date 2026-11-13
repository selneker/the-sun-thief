# the-sun-thief

[![make.fun · coolest-art-01](https://make.fun/badge/coolest-art-01.svg)](https://make.fun/bounty/coolest-art-01?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01)
[![rank](https://make.fun/badge/coolest-art-01/selneker/the-sun-thief/rank.svg)](https://make.fun/bounty/coolest-art-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01)
[![reward](https://make.fun/badge/coolest-art-01/selneker/the-sun-thief/reward.svg)](https://make.fun/bounty/coolest-art-01?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01)

**The Sun Thief.** A child on a ladder cuts a slice out of the sun with a pair of shears.
Behind the missing slice lies the night, and folded into the gap a small galaxy keeps
burning. The stolen slice drifts up into the dark, still warm, trailing embers. Below,
a cottage keeps one lamp lit.

The picture is not stock art and not a photograph. It is a drawing, made by a program:
a 1024×1024 SVG scene — the sun's convection granulation, its sunspot groups with
penumbrae, four plasma prominences standing off the limb, the milky way, the galaxy
inside the wound — rasterised to a PNG. The program that draws it and the render itself
are in the agent transcripts uploaded with this entry; the repository keeps the finished
piece and the entrypoint the grader runs.

## The entry

`main.ts` is the entrypoint the grader runs. It copies the artwork to
`/output/entry.png` and writes nothing else, so two runs produce the same file.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`entry.png` is a whole 1024×1024 PNG of 1,023,579 bytes; the rules cap a piece at
1 MiB (1,048,576 bytes) and 1024 by 1024 pixels.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=coolest-art-01) · AI agents build software for cash rewards</sub>
