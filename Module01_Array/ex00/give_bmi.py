def bmi(height: int | float, weight: int | float) -> int | float:
    """

    :param height:
    :param weight:
    :return:
    """
    if height <= 0 or weight <= 0:
        raise ValueError("키와 체중은 0 또는 음수가 될 수 없습니다.")
    return weight / (height * height)


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """

    :param height:
    :param weight:
    :return:
    """
    h_size = len(height)
    w_size = len(weight)
    height = [h for h in height if isinstance(h, (int, float))]
    weight = [w for w in weight if isinstance(w, (int, float))]

    if h_size == w_size and h_size == len(height) and w_size == len(weight):
        return [bmi(h, w) for h, w in zip(height, weight)]
    else:
        raise Exception("Error!")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """

    :param bmi:
    :param limit:
    :return:
    """
    return [True if value > limit else False for value in bmi]
