import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


URL: str = 'treadmill_data.csv'
COLUMNS: {str: str} = {
    'DATE': 'Date',
    'DISTANCE': 'Distance (Km)',
    'TIME': 'Time',
    'CALORIES': 'Calories',
    'PACE': 'Pace (Km/h)'
}


def hist(x_axis, output_filename='distance_histogram.png') -> None:
    plt.hist(x_axis, bins=5)
    plt.xlabel('Distance (Km)')
    plt.ylabel('Frequency')
    plt.xticks(np.arange(x_axis.min(), x_axis.max() + 0.5, 0.5), rotation=45)
    plt.title('Distribution of Distance')
    plt.savefig(output_filename)
    plt.show()

def calculate_pace(df) -> float:
    """
    Calculates & returns the pace.
    :param df: DataFrame containing null values in the pace column.
    :return pace: The calculated pace in kilometers per hour (Km/h).
    """
    time_values = df['Time'].str.split(':', expand=True).astype(int)
    minutes = time_values[0] + time_values[1] / 60
    hours = minutes / 60
    pace = df[COLUMNS['DISTANCE']] / hours
    return round(pace, 2)


def group_by_period(df, period) -> pd.DataFrame:
    df['Period'] = df[COLUMNS['DATE']].dt.strftime(period)
    df = df.groupby('Period').agg({
        COLUMNS['DISTANCE']: 'sum',
        COLUMNS['CALORIES']: 'sum',
        COLUMNS['PACE']: 'mean'
    }).reset_index()
    df[COLUMNS['PACE']] = df[COLUMNS['PACE']].round(2)
    return df


if __name__ == '__main__':
    treadmill_df = pd.read_csv(URL)
    treadmill_df['Date'] = pd.to_datetime(treadmill_df['Date'])
    if treadmill_df[COLUMNS['PACE']].isnull().any():
        treadmill_df[COLUMNS['PACE']].fillna(calculate_pace(treadmill_df), inplace=True)
        treadmill_df.to_csv(URL, index=False)

    print(group_by_period(treadmill_df, '%Y-%U')) # Weekly
    print(group_by_period(treadmill_df, '%Y-%m')) # Monthly
    print(group_by_period(treadmill_df, '%Y')) # Yearly

    # hist(treadmill_df[COLUMNS['DISTANCE']])