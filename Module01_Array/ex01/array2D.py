def slice_me(family: list, start: int, end: int) -> list:
    col_size = len(family[0])
    row_size = len(family)

    if any(len(child) != col_size for child in family):
        raise ValueError("Error!")

    print(f"My shape is : ({row_size}, {col_size})")

    pos_start = start if start >= 0 else start + row_size
    pos_end = end if end >= 0 else end + row_size
    new_row_size = max(0, pos_end - pos_start)
    new_col_size = col_size if new_row_size > 0 else 0
    print(f"My new shape is : ({new_row_size}, {new_col_size})")

    return family[start:end]
