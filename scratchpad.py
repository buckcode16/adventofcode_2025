# def check(x, y, z):
#     result = (x + y) % z

#     print(
#         f"{x} start position || {y} move, final position =",
#         abs(result),
#     )


def check(x, y, z):
    start = x
    end = x + y

    # 1. Determine the range of movement
    lower = min(start, end)
    upper = max(start, end)

    # 2. Calculate boundaries crossed strictly between start and end
    # Formula: (Count of multiples up to upper-1) - (Count of multiples up to lower)
    zero_past = ((upper - 1) // z) - (lower // z)

    # 3. Standard modulo for position
    final_position = end % z

    if final_position == 0:
        zero_past += 1

    print(
        f"{x} start position || {y} move, zero_past = {zero_past}, final_position = {final_position}",
    )


# --- Verification ---
print("--- Your Test Cases ---")
check(0, 6, 6)  # Expect: 0
check(0, -6, 6)  # Expect: 0
check(3, 6, 6)  # Expect: 1
check(3, -6, 6)  # Expect: 1
check(0, 27, 6)  # Expect: 4
check(0, -27, 6)  # Expect: 4
check(3, 27, 6)  # Expect: 4
check(3, -27, 6)  # Expect: 4
