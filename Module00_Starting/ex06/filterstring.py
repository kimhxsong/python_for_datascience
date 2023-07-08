import string
import sys

from ft_filter import ft_filter

sys.tracebacklimit = 0

if __name__ == "__main__":
    argc = len(sys.argv)
    try:
        assert argc == 3, "the argument are bad"

        s = str(sys.argv[1])
        n = int(sys.argv[2])

        for p in string.punctuation:
            s = s.replace(p, " ")

        words = s.split()
        filter_words = ft_filter(lambda word: len(word) > n, words)
        print(filter_words)

    except Exception as e:
        sys.stderr.write(f"AssertionError: {str(e)}\n")
