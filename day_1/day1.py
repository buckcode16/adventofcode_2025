import operator
from functools import reduce
from pathlib import Path

p = Path("input.txt")
if p.exists():
    content = p.read_text(encoding="utf-8")

# print(content)

# count of "0"

# start from 50, if evaluate is negative then +100, if evaluate is over 99 then -100
# accumulator that only add 0
# must remember the value
# splice command:distance

# if l then -, r then +


def operation(acc, item):
    value, count = acc

    ops = {"L": operator.sub, "R": operator.add}

    eval = ops[item[0]]

    calculate = eval(value, int(item[1:])) % 100

    if calculate == 0:
        count += 1

    return (calculate, count)


result = reduce(operation, content.splitlines(), (50, 0))

print(result)
