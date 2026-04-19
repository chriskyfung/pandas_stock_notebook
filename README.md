# pandas stock notebook

![MADE WITH JYPYTER](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat&logo=Jupyter) ![MADE WITH JYPYTER](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat&logo=Python&logoColor=white) [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

使用 Pandas 和 yfinance 的查詢香港股票的 Jupyter Notebook 範例

👇 **親自試試看** 👨‍💻

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chriskyfung/pandas_stock_notebook/blob/main/pandas_hkstock_datareader.ipynb) [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://mybinder.org/v2/gh/chriskyfung/pandas_stock_notebook/main/?urlpath=lab)

* * *

## 安裝 Python Packages

```shell
pip install -r requirements.txt
```

## 用法

### 從 stocks.py 載入 `stock_profile` 類別

```py
from stocks import stock_profile

stocks = stock_profile()
```

### 從 JSON 文件讀入股票組合清單及股票名稱索引

```py
stocks.loadJsonProfile('./stocks.json')
```

### 從 Yahoo Finance 下載股票組合數據

```py
from datetime import date

tickers = ['0001.hk', '0941.hk','1810.hk']
start_date = date(2021, 9, 15)

stocks.cacheFromYfinance(tickers, start_date)
```

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
