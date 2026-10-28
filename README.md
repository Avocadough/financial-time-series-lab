<div align="center">

# Financial Time Series Lab

**Exploring forecasting, signal processing and technical indicators.**

![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?logo=python&logoColor=white)
![Notebooks](https://img.shields.io/badge/Jupyter-Experiments-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Research%20Prototype-5A6472)

[Overview](#overview) · [Project files](#what-is-here) · [Run](#run-the-extracted-indicator-functions) · [Limitations](#interpreting-the-historical-notebooks)

</div>

## Overview

A collection of historical notebooks exploring financial time-series analysis, digital signal processing and forecasting methods. The experiments include autoregression/ARIMA, Fourier transforms, Kalman smoothing, LSTMs and technical indicators. These are research explorations, not a validated trading system or evidence of profitable trading.

## What is here

| Path | Contents |
| --- | --- |
| [`Financial_Time_Series_Forecasting_using_DSP.ipynb`](Financial_Time_Series_Forecasting_using_DSP.ipynb) | Historical experiments and saved outputs across several stock and crypto examples. |
| [`beta_modeling.ipynb`](beta_modeling.ipynb) | Additional autoregression, Kalman and Fourier experiments. |
| [`financial_dsp/indicators.py`](financial_dsp/indicators.py) | Small, independently runnable extraction of the notebook's EMA, RSI, MACD line and OBV definitions. |
| [`tests/`](tests/) | Numerical checks for the extracted indicator formulas. |

## Run the extracted indicator functions

The following uses only the dependencies in `requirements.txt` and does not download market data:

```bash
python -m pip install -r requirements.txt
python -c "import pandas as pd; from financial_dsp.indicators import ema; print(ema(pd.Series([1.0, 2.0, 3.0]), period=2))"
```

To run the checks, install `pytest` and use `python -m pytest -q`. The RSI is the notebook's rolling-mean variant, not necessarily the Wilder-smoothed version used elsewhere. The MACD function returns the MACD **line**, not its signal line or histogram. Input prices and volume are supplied by the caller.

## Interpreting the historical notebooks

- Saved outputs reflect the original runtime and datasets; they are not a current, independently reproduced evaluation. Some cells depend on Google Colab, downloaded market data or files not included in this repository, and use dependencies beyond the lightweight indicator requirements.
- `beta_modeling.ipynb` labels the square of lag-one correlation as `R²`. It is **not** an out-of-sample forecast R². Some experiments use full-series Fourier transforms or Kalman smoothing, which can include information from later observations; they should not be treated as leakage-free forward forecasts.
- A proper forecasting study needs a frozen dataset, time-ordered evaluation, leakage checks, explicit baselines and a separate assessment of trading costs and execution. None is established by the saved notebook outputs alone.
- A historical ngrok token was removed from the current notebook. Older Git history may still contain it; the credential owner must revoke or rotate it. Set your own token through a secure local environment if you choose to revisit the web-app experiment.
