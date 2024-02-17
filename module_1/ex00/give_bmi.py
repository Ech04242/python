def give_bmi(height: list[int | float], weight: list[int | float])\
            -> list[int | float]:
    if (len(height) != len(weight)):
        print("list len doesn't match")
        return None
    final = []
    for index in range(len(height)):
        final.append((weight[index] / (height[index] ** 2)))
    return final


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return [i < limit for i in bmi]
