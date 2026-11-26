"""make.fun entry: The Funniest Sick-Day Excuse.

Writes one excuse line to /output/entry.txt.

The excuse starts as a genuine sick reason — waking up with no
voice — and turns on a fresh idea: the phone's voice unlock now
thinks its owner is an intruder. The funniest words land near the
end, and the whole line reads like a real person typing a message,
not a joke built for a contest. No fever, no dog, no dead
grandmother: the illness is real, the consequence is absurd, and
every word is doing work.
"""

import os

ENTRY = (
    "I woke up with no voice, which would be fine, except my "
    "phone's voice unlock now thinks I'm an intruder and has "
    "locked me out of my own life."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
