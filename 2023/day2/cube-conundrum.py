from dataclasses import (
    dataclass,
    field,
)
from fileinput import (
    FileInput,
    input,
)
import sys
import re



@dataclass(frozen=True)
class ValidBag:
    red: int = field(init=False, default=12)
    green: int = field(init=False, default=13)
    blue: int = field(init=False, default=14)


@dataclass(repr=True)
class ConundrumGame:
    game_id: int

    red: int = field(default=0)
    green: int = field(default=0)
    blue: int = field(default=0)


def process_match(match: str) -> int:
    match_data: list[str] = match.split(sep=":", maxsplit=1)

    match_id: int = int(
        re
        .search(pattern=r"\d+", string=match_data[0].strip())
        .group()
    )
    match_info = match_data[1].strip()

    game: ConundrumGame = ConundrumGame(game_id=match_id)
    if game.game_id is None:    # yikes
        return 0

    colour_info: list[str] = re.findall(pattern=r"(\d+) (\w+)", string=match_info)

    # Should probably check if each hand is legal
    for count, colour in colour_info:
        if colour == "red":
            game.red = max(game.red, int(count))
        if colour == "green":
            game.green = max(game.green, int(count))
        if colour == "blue":
            game.blue = max(game.blue, int(count))

    return (
        game.red
        * game.green
        * game.blue
    )


def get_input_data() -> None:
    f: FileInput = input(
        files="part1-input",
        mode="r",
        encoding="utf-8",
    )

    power_level: int = 0
    for match in f:
        match_power: int = process_match(match=match)

        power_level += match_power


def main() -> None:
    get_input_data()

    print(f"\n\n*******Exit********")
    sys.exit(1)


if __name__ == "__main__":
    main()

