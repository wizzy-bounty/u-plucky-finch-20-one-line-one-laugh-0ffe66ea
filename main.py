import os

LINE = "I bought a standing desk so I could disappoint myself at two different heights."


def entry_path(out_dir: str) -> str:
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(entry_path(out_dir), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
