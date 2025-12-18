import sys
from decorator import et


# Duration: 505.458971us
@et
def main():
    with open(sys.argv[1]) as f:
        data = [i.strip() for i in f.readlines()]
        freshness = data[:data.index("")]
        sorted_fresh = sorted([[*map(int, f.split("-", 1))] for f in freshness])

        pairs: list = []
        for low, high in sorted_fresh:
            if not pairs or pairs[-1][1] < low:
                pairs.append([low, high])
            else:
                pairs[-1][1] = max(pairs[-1][1], high)

        total = 0
        for low, high in pairs:
            total += high - low + 1


if __name__ == "__main__":
    main()
