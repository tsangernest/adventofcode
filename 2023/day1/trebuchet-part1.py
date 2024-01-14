import re

from pprint import PrettyPrinter
pp = PrettyPrinter(2, 1)



"""
===================================================
The calibration values of these four lines are:
12, 38, 15, and 77. Adding these together produces 142.

answer = 55130
===================================================
"""



def get_file_data():
    with open("part1-input", "r", encoding="utf-8") as file:
        return {key: value.strip() for key, value in enumerate(file)}



def get_line_total(nums):
    if len(nums) == 1:
        return int(nums[0]*2)
    return int(nums[0] + nums[-1])



def main():
    input_file = get_file_data()

    running_total = 0
    for line in input_file.values():
        nums = re.findall(r"\d{1}", line)

        print(f"{nums=}")

        if nums is None:
            continue

        running_total += get_line_total(nums)

    print(f"{running_total=}")
    print(f"\n***In The End***\n")



if __name__ == "__main__":
    main()


