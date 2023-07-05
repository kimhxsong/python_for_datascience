import sys


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count

            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                sys.stderr.write(f"Error: {function} call too many times\n")

        return limit_function

    return callLimiter
