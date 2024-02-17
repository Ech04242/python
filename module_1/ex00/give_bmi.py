def give_bmi(height: list[int | float], weight: list[int | float])\
            -> list[int | float]:
    """_summary_
        this fonction take 2 list, height and weight
        calcul bmi with list donate
    Returns:
        list with bmi
    Error : None if not same len of params
    """
    if (len(height) != len(weight)):
        print("list len doesn't match")
        return None
    final = []
    for index in range(len(height)):
        final.append((weight[index] / (height[index] ** 2)))
    return final


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """_summary_
    send list with true / false if limits was exceed
    Args:
        bmi (list[int  |  float]): bmi of users
        limit (int): value to exceded
    Returns:
        list[bool]: user > limit return true else false
    """
    return [i < limit for i in bmi]
