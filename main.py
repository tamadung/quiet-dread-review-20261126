"""Two Days of Quiet Dread: writes a single code review comment to /output/entry.txt.

The comment approves a pull request while carrying quiet existential dread:
the code works, the tests pass, and none of it matters in the heat death
of the universe. Ship it.
"""
import os

COMMENT = "LGTM. The code works, the tests pass, and none of it matters in the heat death of the universe. Ship it."


def main() -> None:
    # The gate requires 1-140 characters of UTF-8 text, one line.
    # 104 characters: short enough to read at a glance, long enough to dread.
    assert 1 <= len(COMMENT) <= 140, "comment must be 1-140 characters"
    assert "\n" not in COMMENT, "comment must be a single line"
    output_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(COMMENT)
    except OSError:
        # Local run fallback: the sandbox always provides /output.
        os.makedirs("out", exist_ok=True)
        with open("out/entry.txt", "w", encoding="utf-8") as f:
            f.write(COMMENT)


if __name__ == "__main__":
    main()
