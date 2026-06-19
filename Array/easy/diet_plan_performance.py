from typing import List

def diet_plan_performance(calories: List[int], k: int,
                          lower: int, upper: int) -> int:

    points = 0

    for i in range(len(calories) - k + 1):

        total = 0

        for j in range(i, i + k):
            total += calories[j]

        if total < lower:
            points -= 1

        elif total > upper:
            points += 1

    return points