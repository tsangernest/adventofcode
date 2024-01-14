from sys import exit
from re import search
from argparse import ArgumentParser, FileType


def get_file_data_from_args():
    file_data: dict = {}

    parser: ArgumentParser = ArgumentParser(
        prog="Seed-a-Fertilizer",
        description="Grab seed info",
    )
    parser.add_argument("f",  type=FileType("r", encoding="utf-8"))
    arg_file = parser.parse_args().f

    seeds: list[int] = arg_file.readline().split(sep=":", maxsplit=1)[1]

    for raw_line in arg_file:
        line: str = raw_line.strip()

        is_title = search(pattern=r"^([a-z]+-){2}[a-z]+ map:$", string=line)
        if is_title:
            # If it's a title, we create a new 'key'
            print(is_title)



    return seeds


def main():
    file_data = get_file_data_from_args()


    print(f"\n\n***End of Processing***\n")
    return exit(0)


if __name__ == "__main__":
    main()

