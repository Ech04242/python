def give_bmi(height: list[int | float], weight: list[int | float])\
            -> list[int | float]:
    """_summary_
        this fonction take 2 list, height and weight
        calcul bmi with list donate
    Returns:
        list with bmi
    Error : None if not same len of params
    """
    try:
        if (len(height) != len(weight)):
            raise ValueError("list len doesn't match")
        final = []
        for index in range(len(height)):
            if not isinstance(weight[index], (int, float))\
                    or not isinstance(height[index], (int, float)):
                raise TypeError("bad type detect on list")
            if weight[index] <= 0 or height[index] <= 0:
                raise ValueError("number positif only")
            final.append((weight[index] / (height[index] ** 2)))
        return final
    except Exception as error:
        print("error : ", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """_summary_
    send list with true / false if limits was exceed
    Args:
        bmi (list[int  |  float]): bmi of users
        limit (int): value to exceded
    Returns:
        list[bool]: user > limit return true else false
    """
    try:
        if not isinstance(limit, int):
            raise ValueError("limit is not integer")
        if limit <= 0:
            raise ValueError("limit need to be positif only")
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("value other of int / float detect")
        return [i > limit for i in bmi]
    except Exception as error:
        print("error: ", error)
        return []
