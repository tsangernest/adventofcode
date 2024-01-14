from math import prod
import sys

from argparse import (
    ArgumentParser,
    FileType,
)

from dataclasses import dataclass


from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2, width=1)


@dataclass
class Race:
    id: int

    time: int
    distance: int


def get_holding_numbs(data: list[Race]):
    record_breakers: list = []

    for race in data:

        num_ways_to_win: int = 0
        for hold_time in range(1, race.time):
            remain_time: int = race.time - hold_time

            d: int = hold_time * remain_time
            if d > race.distance:
                num_ways_to_win += 1
        record_breakers.append(num_ways_to_win)

    print(f"{prod(record_breakers)=}")


def get_file_data() -> list[Race]:
    parser = ArgumentParser()
    parser.add_argument("f", type=FileType(mode="r", encoding="UTF-8")),
    file = parser.parse_args().f

    input_line: list = file.readline().split(sep=":", maxsplit=1)
    data_line: list = input_line[1].strip().split()

    all_games: list[Race] = []
    counter: int = 0
    for time in data_line:
        all_games.append(Race(id=counter, time=int(time), distance=0))
        counter += 1

    input_line: list = file.readline().split(":", 1)
    distances: list = input_line[1].strip().split()

    counter: int = 0
    for race in all_games:
        race.distance = int(distances[counter])
        counter += 1

    return all_games


def main() -> None:
    data: list[Race] = get_file_data()
    # pp.pprint(object=data)

    get_holding_numbs(data=data)


    print(f"\n\n*****End of processing*****\n")
    return sys.exit(0)


if __name__ == "__main__":
    main()

