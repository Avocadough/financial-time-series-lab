"""Technical-indicator definitions extracted from the historical notebook."""

import numpy as np


def ema(close, period=20):
    return close.ewm(span=period, adjust=False).mean()


def rsi(close, period=14):
    delta = close.diff()
    gain, loss = delta.copy(), delta.copy()
    gain[gain < 0] = 0
    loss[loss > 0] = 0
    avg_gain = gain.rolling(period).mean()
    avg_loss = abs(loss.rolling(period).mean())
    return 100.0 - (100.0 / (1.0 + avg_gain / avg_loss))


def macd_line(close, fast_period=12, slow_period=26):
    return ema(close, fast_period) - ema(close, slow_period)


def obv(close, volume):
    return np.where(close > close.shift(), volume, np.where(close < close.shift(), -volume, 0)).cumsum()
