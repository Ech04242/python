from load_csv import load
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":
    data = load("../assets/life_expectancy_years.csv")
    Paris = data[data['country'] == "France"]
    plt.plot(Paris.columns[1:], Paris.values[0][1:], label='France')
    plt.xlabel('Year')
    plt.title('France life expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xticks(Paris.columns[1::40])
    plt.legend()
    plt.show()
