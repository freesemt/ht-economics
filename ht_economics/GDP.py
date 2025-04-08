"""
GDP.py
"""

import pandas as pd

def get_gdp_data(file_path):
    """
    Load GDP data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file containing GDP data.
    
    Returns:
    DataFrame: A pandas DataFrame containing the GDP data.
    """
    names = [
        "Year",                 # Calendar Year
        "GDP",                  # GDP(Expenditure Approach)
        "PrivateCons",          # Private Consumption
        "HouseholdsCons",       # Consumption of Households
    ]
    usecols = [0, 1, 2, 3]
    # Load the GDP data from the CSV file
    gdp_data = pd.read_csv(file_path, encoding="shift_jis", header=7, names=names, usecols=usecols, nrows=30)
    
    # Convert the 'Year' column to datetime format
    gdp_data['Year'] = [pd.to_datetime(str(s).replace('/1-12.', ''), format='%Y') for s in gdp_data['Year'].values]
    # gdp_data['Year'] = [int(str(s).replace('/1-12.', '')) for s in gdp_data['Year'].values]
    # gdp_data['Year'] = pd.to_datetime(gdp_data['Year'], format='%Y')
    
    return gdp_data
 