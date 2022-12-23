import pytest
import os

from importlib import reload

import lib.import as imp

def test_import_pdf():
    # Test importing a valid PDF file
    portfolio = imp.import_pdf("test_data/valid.pdf")
    assert isinstance(portfolio, dict)
    assert "assets" in portfolio
    assert "total_value" in portfolio
    
    # Test importing an invalid PDF file
    with pytest.raises(ValueError):
        imp.import_pdf("test_data/invalid.pdf")
        
    # Test importing a non-existent file
    with pytest.raises(FileNotFoundError):
        imp.import_pdf("test_data/nonexistent.pdf")

def test_parse_pdf_data():
    # Test parsing valid data
    data = {
        "assets": [
            {"name": "Apple Inc.", "ticker": "AAPL", "shares": 10, "price": 100},
            {"name": "Microsoft Corporation", "ticker": "MSFT", "shares": 20, "price": 50}
        ],
        "total_value": 1500
    }
    portfolio = imp.parse_pdf_data(data)
    assert isinstance(portfolio, dict)
    assert "assets" in portfolio
    assert "total_value" in portfolio
    assert len(portfolio["assets"]) == 2
    assert portfolio["total_value"] == 1500
    
    # Test parsing invalid data
    with pytest.raises(ValueError):
        imp.parse_pdf_data({})

def test_reload():
    # Test reloading the module
    reload(imp)
