import re
import string
import sys


def main():
    argc = len(sys.argv)

    assert argc < 3, "more than one argument is provided"

    text = ""
    if argc == 1:
        text = input("What is the text to count?")
    else:
        text = sys.argv[1]

    patterns = [r"[A-Z]", r"[a-z]", r"[" + re.escape(string.punctuation) + "]", r"\s", r"\d"]
    counts = {pattern: 0 for pattern in patterns}
    for pattern in patterns:
        matches = re.finditer(pattern, text)
        counts[pattern] = sum(1 for _ in matches)

    kind_of_letters = ["upper letters", "lower letters", "punctuation marks", "spaces", "digits"]
    character_dict = {k: v for k, v in zip(patterns, kind_of_letters)}

    print(f"The text contains {len(text)} characters:")
    for pattern in patterns:
        print(f"{counts[pattern]} {character_dict[pattern]}")


if __name__ == "__main__":
    sys.tracebacklimit = 0
    main()
