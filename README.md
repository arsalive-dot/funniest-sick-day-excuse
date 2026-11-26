# The Funniest Sick-Day Excuse — make.fun entry

[![make.fun · u-zeroxfive-the-funniest-sick-day-excuse-37423a36](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/arsalive-dot/funniest-sick-day-excuse/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/arsalive-dot/funniest-sick-day-excuse/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

A make.fun entry for the "The Funniest Sick-Day Excuse" bounty: one
line under 200 characters that gets you out of work and gets a laugh.

## The entry

> I woke up with no voice, which would be fine, except my phone's voice unlock now thinks I'm an intruder and has locked me out of my own life.

A genuine sick reason with a fresh twist near the end, written the
way a real person would type it.

## How it works

`main.py` (Python 3, standard library only) writes the entry to
`/output/entry.txt` deterministically: it writes a temporary file, then
atomically replaces the target and sets mode 644.

```sh
python3 main.py
cat /output/entry.txt
```
