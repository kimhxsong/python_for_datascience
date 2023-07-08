def ft_filter(func, iter):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if func is not None :
        return [item for item in iter if func(item)]
    else:
        return [item for item in iter if item]
