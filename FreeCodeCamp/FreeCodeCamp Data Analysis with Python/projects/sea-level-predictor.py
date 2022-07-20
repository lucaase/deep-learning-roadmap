import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('FreeCodeCamp\FreeCodeCamp Data Analysis with Python\projects\epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df.iloc[:,1])


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], intercept + slope * df['Year'], 'r', label = 'Best Fit Line 1')

    # Create second line of best fit
    dummy = list(range(1880, 2050))
    x2 = list(range(1880, 2050))
    y2 = []
    for year in x2:
        y2.append(intercept + slope*year)

    plt.plot(x2, y2, 'y', label = 'Best Fit Line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()