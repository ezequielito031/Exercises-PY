from assignment import calculate_profit, calculate_roi, portfolio_total, get_crypto_data


def test_profit_positive():
    assert calculate_profit(40000, 48000, 1) == 8000

def test_profit_multiple_units():
    assert calculate_profit(40000, 45000, 2) == 10000

def test_profit_loss():
    assert calculate_profit(48000, 40000, 1) == -8000

def test_profit_breakeven():
    assert calculate_profit(40000, 40000, 1) == 0


def test_roi_positive():
    assert calculate_roi(40000, 48000) == 20.0

def test_roi_loss():
    assert calculate_roi(48000, 40000) < 0

def test_roi_breakeven():
    assert calculate_roi(40000, 40000) == 0.0


def test_portfolio_total_basic():
    assert portfolio_total({"Bitcoin": 40000, "Ethereum": 2500}) == 42500

def test_portfolio_total_single():
    assert portfolio_total({"Bitcoin": 48000}) == 48000

def test_portfolio_total_empty():
    assert portfolio_total({}) == 0


def test_data_has_correct_columns():
    df = get_crypto_data()
    assert "Day" in df.columns
    assert "Bitcoin" in df.columns
    assert "Ethereum" in df.columns

def test_data_has_seven_rows():
    assert len(get_crypto_data()) == 7

def test_bitcoin_prices_positive():
    assert (get_crypto_data()["Bitcoin"] > 0).all()
