import sys

from math import sqrt
from pprint import PrettyPrinter

from decorator import et


pp = PrettyPrinter(2, 1)


@et
def main():
    with open(sys.argv[1]) as f:
        data = [[*map(int, i.split(",", 2))] for i in f.readlines()]

        distances = []
        for a, (x1, y1, z1) in enumerate(data):
            for b, (x2, y2, z2) in enumerate(data):
                squares = pow(x1-x2, 2), pow(y1-y2, 2), pow(z1-z2, 2)
                distances.append(sqrt(sum(squares)))
        # Do I then sort, and then throw it into a set?

if __name__ == "__main__":
    main()
    sys.exit(0)

