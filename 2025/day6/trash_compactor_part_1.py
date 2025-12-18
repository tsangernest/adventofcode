import math
import sys
from decorator import et


# Quickly glancing at data set, and sample data set.
# There's only appears to be positive numbers.


# Duration:  936.045020us
@et
def main():
    with open(sys.argv[1]) as f:
        matrix = [f.strip().split() for f in f.readlines()]
        transposed_matrix = [[int(x) if x.isdigit() else x for x in y] for y in zip(*matrix)]

        sub_total = []
        for line in transposed_matrix:
            operand = line.pop()
            if "*" == operand:
                sub_total.append(math.prod(line))
            else:   # "+" == operand
                sub_total.append(sum(line))

        print(sum(sub_total))


if __name__ == "__main__":
    main()

