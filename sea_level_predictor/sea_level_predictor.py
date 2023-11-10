import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import scipy

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    df_until_2050 = df[df['Year'] <= 2050]
    res = scipy.stats.linregress(df_until_2050['Year'], df_until_2050['CSIRO Adjusted Sea Level'])
    plt.plot(df_until_2050['Year'], res.intercept + res.slope*df_until_2050['Year'], 'r', label='fitted line 1')

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] == 2000]
    res_2 = scipy.stats.linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])
    
    plt.plot(df['Year'], res.intercept + res.slope*df['Year'], 'r', label='fitted line 1')

    plt.plot(df_2000['Year'], res_2.intercept + res_2.slope*df_2000['Year'], 'g', label='fitted line 2')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()