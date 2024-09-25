import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original data')

    # Create first line of best fit (for the entire dataset)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create years from 1880 to 2050
    years_extended = pd.Series(range(1880, 2051))
    sea_level_extended = intercept + slope * years_extended
    
    # Plot the first line of best fit
    plt.plot(years_extended, sea_level_extended, 'r', label='Fitted line (1880-2050)')
    
    # Create second line of best fit (from 2000 onwards)
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    
    # Create years from 2000 to 2050 for the second line of best fit
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_level_recent_extended = intercept_recent + slope_recent * years_recent_extended
    
    # Plot the second line of best fit
    plt.plot(years_recent_extended, sea_level_recent_extended, 'g', label='Fitted line (2000-2050)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()