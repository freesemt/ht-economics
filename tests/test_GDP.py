"""
Test the GDP class
This file contains unit tests for the GDP class, which is part of the gdp module.
"""
import sys
sys.path.insert(0, "..")

from ht_economics.GDP import get_gdp_data

url_j = "https://www.esri.cao.go.jp/jp/sna/data/data_list/sokuhou/files/2024/qe244_2/tables/ritu-jcy2442.csv" # 年次GDP成長率（実質）

def test_get_gdp_data():
    """
    Test the get_gdp_data function.
    """
    # Test with a valid URL
    gdp_data = get_gdp_data(url_j)
    assert gdp_data is not None, "Failed to load GDP data from the URL."
    assert not gdp_data.empty, "Loaded GDP data is empty."
    assert 'Year' in gdp_data.columns, "'Year' column is missing in the loaded data."
    assert 'GDP' in gdp_data.columns, "'GDP' column is missing in the loaded data."
    assert 'PrivateCons' in gdp_data.columns, "'PrivateCons' column is missing in the loaded data."
    assert 'HouseholdsCons' in gdp_data.columns, "'HouseholdsCons' column is missing in the loaded data."