from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

from load_csv import load


def format_y_tick(value, _):
    return f"{int(value)}M"


def main():
    df = load("../../02_life_expectancy_years.csv")
    countries = ['South Korea', 'Japan']
    df = df[df['country'].isin(countries)]

    df_transposed = df.transpose()
    new_column_names = df_transposed.iloc[0]
    df_transposed = df_transposed[1:]
    df_transposed.columns = new_column_names

    df_transposed.index = df_transposed.index.astype(int)
    df_filtered = df_transposed[(df_transposed.index >= 1800) & (df_transposed.index <= 2050)]
    df_filtered.plot()

    plt.legend(loc='lower right')

    plt.xlabel("Years")
    plt.ylabel("Populations")

    plt.xticks(range(1800, 2050, 40))
    formatter = FuncFormatter(format_y_tick)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.title("Population Projections")
    plt.show()


if __name__ == "__main__":
    main()
