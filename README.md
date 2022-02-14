[![Flake8 Lint](https://github.com/sanggi-wjg/my_stock/actions/workflows/flake8_lint.yml/badge.svg)](https://github.com/sanggi-wjg/my_stock/actions/workflows/flake8_lint.yml)

# My Stock


## Usage
만약 미국도 하고 싶다면 constants.py 에 추가 하면 됨
```shell
http://localhost:8080/admin/stocks/market/
market 에 KOSPI, KOSDAQ 등록

python manage.py register_stocks KOSPI
python manage.py register_stocks KOSDAQ
```
