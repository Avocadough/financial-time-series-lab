import numpy as np
import pandas as pd

from financial_dsp.indicators import ema, macd_line, obv, rsi


def test_ema_matches_the_notebooks_nonadjusted_definition():
    result = ema(pd.Series([1.0, 2.0, 3.0]), period=2)
    np.testing.assert_allclose(result, [1.0, 5 / 3, 23 / 9])


def test_rsi_uses_the_notebooks_rolling_mean():
    result = rsi(pd.Series([1.0, 2.0, 1.0, 3.0]), period=2)
    assert result.iloc[:2].isna().all()
    np.testing.assert_allclose(result.iloc[2:], [50, 100 - 100 / 3])


def test_macd_returns_only_the_difference_between_two_emas():
    prices = pd.Series([1.0, 2.0, 3.0])
    result = macd_line(prices, fast_period=2, slow_period=3)
    np.testing.assert_allclose(result, [0, 1 / 6, 11 / 36])


def test_obv_handles_up_flat_and_down_days():
    result = obv(pd.Series([1, 2, 2, 1]), pd.Series([100, 200, 300, 400]))
    np.testing.assert_array_equal(result, [0, 200, 200, -200])
