import time

rawSeconds = time.time()
formattedSeconds = f"{rawSeconds:,.4f}"
scientificSeconds = f"{rawSeconds:.2e}"


print(f"Seconds since January 1, 1970: {formattedSeconds} or {scientificSeconds} in scientific notation")

# Expected:
# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
# Oct 21 2022
