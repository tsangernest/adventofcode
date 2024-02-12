import sys
import re
import argparse
from pydantic import BaseModel

from pprint import PrettyPrinter
pp = PrettyPrinter(2, 1)


class Category(BaseModel):
    id: int

    category_name: str

    destination: list
    source: list
    range: list

    @property
    def calc_new_d(self) -> list:
        rc: list[int] = []

        for new_d in self.destination:
            for range in self.range:
                rc.append((int(new_d) + int(range)))
        return rc



def get_file_data_from_args():
    data: list[Category] = []

    parser = argparse.ArgumentParser()
    parser.add_argument("f",  type=argparse.FileType("r", encoding="utf-8"))
    arg_file = parser.parse_args().f

    seeds: list[int] = (
        arg_file
        .readline()
        .split(sep=":", maxsplit=1)[1]
        .split()
    )

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

        is_title = re.search(pattern=r"^([a-z]+-){2}[a-z]+ map:$",
                             string=line)
        if is_title:
            name: str = (
                is_title
                .string
                .split()[0]
                .strip()
            )

        location = re.search(pattern=r"^(\d+) (\d+) (\d+)$",
                             string=line)
        if location:
            dest.append(location.group(1))
            src.append(location.group(2))
            rng.append(location.group(3))

        if 0 == len(line):
            category = Category(id=cat_id,
                                category_name=name,
                                destination=dest,
                                source=src,
                                range=rng)
            data.append(category)

            # loop vars
            cat_id += 1
            dest = []
            src = []
            rng = []
    data.append(Category(id=cat_id,
                         category_name=name,
                         destination=dest,
                         source=src,
                         range=rng))

    return seeds, data


def main():
    seeds, data = get_file_data_from_args()
    # pp.pprint(seeds)
    # pp.pprint(data)

    for d in data:
        print(d.calc_new_d)

    print(f"\n\n***End of Processing***\n")
    return sys.exit(0)


if __name__ == "__main__":
    main()

