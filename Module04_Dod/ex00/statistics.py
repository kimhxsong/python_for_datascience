import math
import sys
from collections import Counter


def calculate_mean(data):
    return sum(data) / len(data)


def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        mid = n // 2
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[n // 2]


def calculate_quartile(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1_index = n // 4
    q3_index = q1_index * 3

    if n % 2 == 0:
        q1 = float(sorted_data[q1_index - 1] + sorted_data[q1_index]) / 2
        q3 = float(sorted_data[q3_index - 1] + sorted_data[q3_index]) / 2
    else:
        q1 = float(sorted_data[q1_index])
        q3 = float(sorted_data[q3_index])

    return [q1, q3]


def calculate_variance(data):
    mean = calculate_mean(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    return variance


def calculate_std_deviation(data):
    variance = calculate_variance(data)
    std_deviation = math.sqrt(variance)
    return std_deviation


def ft_statistics(*args: any, **kwargs: any) -> None:
    nums = [item for item in args if isinstance(item, (int, float))]
    commands = list(Counter(kwargs.values()))

    statistics_map = {
        "mean": lambda data: print(f"mean: {calculate_mean(data)}"),
        "median": lambda data: print(f"median: {calculate_median(data)}"),
        "quartile": lambda data: print(f"quartile: {calculate_quartile(data)}"),
        "std": lambda data: print(f"std: {calculate_std_deviation(data)}"),
        "var": lambda data: print(f"var: {calculate_variance(data)}"),
    }

    for command in commands:
        if command in statistics_map:
            try:
                statistics_map[command](nums)
            except:
                sys.stderr.write("ERROR\n")
