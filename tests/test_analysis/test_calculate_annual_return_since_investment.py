"""
SUMMARY:
test_calculate_annual_return_since_investment.py is a test file that tests the function 
calculate_annual_return_since_investment in the analysis module. 
This function calculates the overall annual performance of a stock since the time it was invested in, 
expressed as a percentage.

Example:
Input:
stock_symbol: "AAPL"
shares_owned: 10
purchase_price: 100
current_price: 150

Output:
50% (since the investment of 1000€ has grown to 1500€ in the given time frame)
"""

import unittest
from lib.analysis.calculate_annual_return_since_investment 
import calculate_annual_return_since_investment

class TestCalculateAnnualReturnSinceInvestment(unittest.TestCase):
    def test_calculate_annual_return_since_investment(self):
        # Test with valid input
        stock_symbol = "AAPL"
        shares_owned = 10
        purchase_price = 100
        current_price = 150
        expected_output = 50.0
        self.assertEqual(calculate_annual_return_since_investment(stock_symbol, shares_owned, purchase_price, current_price), expected_output)

        # Test with zero shares owned
        stock_symbol = "AAPL"
        shares_owned = 0
        purchase_price = 100
        current_price = 150
        expected_output = 0.0
        self.assertEqual(calculate_annual_return_since_investment(stock_symbol, shares_owned, purchase_price, current_price), expected_output)

        # Test with negative shares owned
        stock_symbol = "AAPL"
        shares_owned = -10
        purchase_price = 100
        current_price = 150
        expected_output = None
        self.assertEqual(calculate_annual_return_since_investment(stock_symbol, shares_owned, purchase_price, current_price), expected_output)

        # Test with zero purchase price
        stock_symbol = "AAPL"
        shares_owned = 10
        purchase_price = 0
        current_price = 150
        expected_output = None
        self.assertEqual(calculate_annual_return_since_investment(stock_symbol, shares_owned, purchase_price, current_price), expected_output)

        # Test with negative purchase price
        stock_symbol = "AAPL"
        shares_owned = 10
        purchase_price = -100
        current_price = 150
        expected_output = None
        self.assertEqual(calculate_annual_return_since_investment(stock_symbol, shares_owned, purchase_price, current_price), expected_output)

if __name__ == '__main__':
    unittest.main()