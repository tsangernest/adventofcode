from sys import exit
from re import search, Match
from argparse import ArgumentParser, FileType

from pydantic import BaseModel, Field

from pprint import PrettyPrinter
pp = PrettyPrinter(2, 1)


class Category(BaseModel):
    id: int

    category_name: str

    destination: list
    source: list
    range: list




def get_file_data_from_args():
    data: list[Category] = []

    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("f",  type=FileType("r", encoding="utf-8"))
    arg_file = parser.parse_args().f

    seeds: list[int] = arg_file.readline().split(sep=":", maxsplit=1)[1]

    # skips first blank line because yeah
    arg_file.readline()

    # loop primers
    cat_id: int = 0
    dest: list = []
    src: list = []
    rng: list = []
    name: str = ""
    for raw_line in arg_file:
        line: str = raw_line.strip()

        is_title: Match = search(pattern=r"^([a-z]+-){2}[a-z]+ map:$", string=line)
        if is_title:
            name: str = is_title.string.split()[0].strip()
            # print(f"{name=}")

        location: Match = search(pattern=r"^(\d+) (\d+) (\d+)$", string=line)
        if location:
            # print(f"{location.group(1)} - {location.group(2)} - {location.group(3)}")
            dest.append(location.group(1))
            src.append(location.group(2))
            rng.append(location.group(3))

        if 0 == len(line):
            category = Category(
                id=cat_id,
                category_name=name,
                destination=dest,
                source=src,
                range=rng,
            )
            data.append(category)

            # loop vars
            cat_id += 1
            dest = []
            src = []
            rng = []

            continue
    pp.pprint(data)

    return seeds


def main():
    file_data = get_file_data_from_args()


    print(f"\n\n***End of Processing***\n")
    return exit(0)


if __name__ == "__main__":
    main()

