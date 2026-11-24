"""Dad Joke Showdown entry.

Writes one dad joke (at most 200 characters) to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

JOKE = (
    'Dad said, "When I\'m gone, have my ashes pressed into a diamond." '
    'I said, "No pressure."'
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
