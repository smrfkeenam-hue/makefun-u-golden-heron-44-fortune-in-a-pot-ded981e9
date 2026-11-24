"""Fortune in a Pot — one kind, funny fortune for the houseplant on the sill."""

import os

ENTRY = "Your tallest leaf catches the morning sun first this week, and your keeper learns your name is not 'the green one'."


def entry_path():
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def write_entry(text, path="/output/entry.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(ENTRY, entry_path())


if __name__ == "__main__":
    main()
