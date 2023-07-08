import matplotlib.pyplot as plt

from load_csv import load


def main():
    df = load("../../02_life_expectancy_years.csv")

    south_korea_life_expectancy = df[df['country'] == 'South Korea'].iloc[:, 1:].values.flatten()

    years = df.columns[1:]
    years = list(map(int, years))

    plt.plot(years, south_korea_life_expectancy)
    plt.title("South Korea Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.xticks(range(1800, 2100, 40))
    plt.show()


main()
