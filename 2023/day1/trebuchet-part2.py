"""
===================================================
In this example, the calibration values are:
29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

answer = ?
===================================================
"""
from pprint import PrettyPrinter
from re import Pattern
import re

pp = PrettyPrinter(indent=2, width=1)


nums: list[str] = [
    "zero", "one", "two", "three",
    "four", "five", "six", "seven",
    "eight", "nine",
]
nums_re: Pattern = re.compile(r"(?=(\d|%s))" % nums)




with open(file=f"part2-input",
          mode="r",
          encoding="utf-8") as f:
    total: int = 0

    for line in f:
        digits: list = []

        for num in nums_re.findall(line):
            if num in nums:
                num: str = str(nums.index(num) + 1)

            digits.append(num)

        total += int(digits[0] + digits[-1])

    pp.pprint(object=total)

