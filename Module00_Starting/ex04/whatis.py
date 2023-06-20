import re
import sys


# sys.tracebacklimit = 0


def ft_is_integer(string: str) -> bool:
    pattern = r"^-?\d+$"
    return re.match(pattern, string) is not None


try:
    argv = sys.argv
    argc = len(argv)

    assert argc < 3, "more than one argument is provided\n"

    if argc == 1:
        exit(0)

    assert ft_is_integer(argv[1]), "argument is not an integer\n"
    num = int(argv[1])
    print(f"I'm {'Even.' if num % 2 == 0 else 'Odd.'}")

except AssertionError as e:
    sys.stderr.write(f"AssertionError: {str(e)}")
