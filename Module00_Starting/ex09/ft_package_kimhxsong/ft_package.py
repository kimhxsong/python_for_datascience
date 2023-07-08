def count_in_list(items: list, target: object):
    count = 0
    for item in items:
        if item is target:
            count = count + 1
        else:
            pass

    return count * -1
