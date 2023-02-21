import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def create_df(csv_file='Logs.csv') -> pd.core.frame.DataFrame:
    df = pd.read_csv(csv_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Calories'] = pd.to_numeric(df['Calories']).round(decimals=0)
    df['Distance'] = pd.to_numeric(df['Distance']).round(decimals=1)
    return df


def plot_df(df):
    date_array = df['Date']
    price_array = df['Distance']

    plt.xlabel('Date')
    plt.ylabel('Distance')

    plt.plot(date_array, price_array, linestyle='solid')
    plt.ylim(0, max(df['Distance'] + 0.5))
    plt.show()


def scatter_df(df):
    # create scatter plot
    plt.scatter(df.Date, df.Distance)

    plt.ylim(0, max(df['Distance'] + 0.5))

    # add horizontal line at mean value of y
    plt.axhline(y=np.nanmean(df.Distance))
    plt.show()



if __name__ == '__main__':
    DataFrame = create_df('Logs.csv')
    #plot_df(DataFrame)
    scatter_df(DataFrame)