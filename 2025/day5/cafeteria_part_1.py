import sys
from decorator import et


def is_in_range(low, high, num):
    if low <= num <= high:
        return True
    return False


# Duration:  20.653298ms
@et
def main():
    with open(sys.argv[1]) as f:
        data = [i.strip() for i in f.readlines()]
        seperator_idx = data.index("")
        freshness = data[:seperator_idx]
        ingredients = {int(i): False for i in data[seperator_idx + 1:]}

        for ing in ingredients.keys():
            for fresh in freshness:
                low, high = fresh.split("-", 1)
                if is_in_range(int(low), int(high), ing):
                    ingredients[ing] = True
                    break

        print(sum(ingredients.values()))


if __name__ == "__main__":
    main()

