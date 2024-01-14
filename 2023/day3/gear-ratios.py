from fileinput import (
    FileInput,
    input,
)
import sys
import re


def get_file_data():
    f: FileInput = input(
        files="part1-sample-input",
        mode="r",
        encoding="utf-8",
    )

    striped: list = [line.strip() for line in f]
    print(f"{striped=}")


def main() -> None:
    get_file_data()

    print(f"\n\n*******The End*******\n\n")
    sys.exit(1)


if __name__ == "__main__":
    main()

