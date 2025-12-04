import operator
from functools import reduce
from pathlib import Path

p = Path("../day_1/input.txt")
if p.exists():
    content = p.read_text(encoding="utf-8")

# print(content)


# consider also rotation


def operation(acc, item):
    start_number, count = acc

    ops = {"L": operator.sub, "R": operator.add}

    operator_function = ops[item[0]]

    evaluation = operator_function(start_number, int(item[1:]))

    lower = min(start_number, evaluation)

    upper = max(start_number, evaluation)

    zero_past = ((upper - 1) // 100) - (lower // 100)

    end_number = evaluation % 100

    count = count + zero_past
    if end_number == 0:
        count += 1

    return (end_number, count)


result = reduce(operation, content.splitlines(), (50, 0))

print(result)
