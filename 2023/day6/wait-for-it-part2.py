import sys
from argparse import ArgumentParser, FileType
from dataclasses import dataclass

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2, width=1)


@dataclass
class Race:
    id: int

    time: int
    distance: int


def num_ways_to_win(data: Race) -> None:
    num_ways_win: int = 0

    for hold_time in range(1, data.time):
        remain_time: int = data.time - hold_time

        d: int = hold_time * remain_time
        if d > data.distance:
            num_ways_win += 1


def get_file_data() -> Race:
    parser = ArgumentParser()
    parser.add_argument("f", type=FileType(mode="r", encoding="UTF-8")),
    file = parser.parse_args().f

    input_line: list = file.readline().strip().split(sep=":", maxsplit=1)
    data_line: list = input_line[1].strip().split()

    time_str: str = ""
    for num in data_line:
        time_str += num

    input_line: list = file.readline().strip().split(sep=":", maxsplit=1)
    data_line: list = input_line[1].strip().split()

    distance_str: str = ""
    for num in data_line:
        distance_str += num

    race = Race(id=0, time=int(time_str), distance=int(distance_str))

    return race


def main() -> None:
    race: Race = get_file_data()
    # pp.pprint(object=data)
    pp.pprint(object=race)

    num_ways_to_win(race)

    print(f"\n\n*****End of processing*****\n")
    return sys.exit(0)


if __name__ == "__main__":
    main()

