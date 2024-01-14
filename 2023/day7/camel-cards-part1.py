import sys

from argparse import (
    ArgumentParser,
    FileType,
)

from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2, width=1)


_FACE_CARDS: dict[str, int] = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


_COMBOS: list[str] = []




def _get_input_data() -> list[dict]:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("f", type=FileType("r", encoding="utf-8"))
    file_data = parser.parse_args().f

    hands_list: list[dict] = []
    for line in file_data:
        k, v = line.strip().split(maxsplit=1)

        hands_list.append({
            "bid": v.strip(),
            "hand": k.strip(),
        })

    file_data.close()
    return hands_list


def main() -> None:
    hands: list[dict] = _get_input_data()
    pp.pprint(object=hands)



    print("\n\n***End of Processing***")
    sys.exit(0)


if __name__ == "__main__":
    main()

