from matplotlib import pyplot as plt

from load_csv import load


def format_x_ticks(x, _):
    if x >= 1000:
        return f"{int(x / 1000)}k"
    return x


def main():
    life_df = load("../../02_life_expectancy_years.csv")
    income_df = load("../../02_income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    life = life_df['1900']
    income = income_df['1900']
    plt.scatter(income, life)

    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")

    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])

    plt.title("1900")
    plt.show()


if __name__ == "__main__":
    main()
