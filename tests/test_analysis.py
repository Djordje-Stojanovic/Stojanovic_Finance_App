import pytest

def test_calculate_performance():
    # Set up test data
    portfolio = [
        {"symbol": "AAPL", "shares": 100, "price": 200},
        {"symbol": "GOOG", "shares": 50, "price": 150},
        {"symbol": "MSFT", "shares": 75, "price": 100},
    ]
    expected_result = {"AAPL": 20000, "GOOG": 7500, "MSFT": 7500}
    
    # Test the function
    result = calculate_performance(portfolio)
    assert result == expected_result
    
def test_calculate_suggestions():
    # Set up test data
    portfolio = [
        {"symbol": "AAPL", "shares": 100, "price": 200},
        {"symbol": "GOOG", "shares": 50, "price": 150},
        {"symbol": "MSFT", "shares": 75, "price": 100},
    ]
    expected_result = ["AAPL", "GOOG"]
    
    # Test the function
    result = calculate_suggestions(portfolio)
    assert result == expected_result
