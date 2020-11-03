# initlalize and set everything of check_data.py
from tool import Logger
from crawl import Crawldata
import sys
from datetime import datetime, timedelta
from time import strftime

# save to log file
sys.stdout = Logger()

# key:table, value:spider
table_spider_dict = {
  "taifex_big3_futures_table": {
    "spider": "TAIFEX_get_big3_futures",
    "serveral_args": [
        {"commodity_id": "TXF"},
        {"commodity_id": "MXF"},
        {"commodity_id": "FXF"},
        {"commodity_id": "EXF"},
    ]
  },
  "taifex_large_trader_futures_table": {
    "spider": "TAIFEX_get_large_trader_futures",
    "serveral_args": [
        {"contract_id": "TX"}
    ]

  },
  "taifex_futures_price_table": {
    "spider": "TAIFEX_get_futures_price",
    "serveral_args": [
        {"commodity_id": "TX", "query_type": 2, "market_code": 0},
        {"commodity_id": "MTX", "query_type": 2, "market_code": 0},
        {"commodity_id": "TX", "query_type": 2, "market_code": 1},
    ]
  },
  "taifex_big3_options_table": {
    "spider": "TAIFEX_get_big3_options",
    "serveral_args": [
        {"query_type": 1, "do_query": 1, "commodity_id": "TXO"}
    ]
  },
  "taifex_large_trader_options_table": {
    "spider": "TAIFEX_get_large_trader_options",
    "serveral_args": [
        {"contract_id": "TXO"}
    ]
  },
  "taifex_options_price_table": {
    "spider": "TAIFEX_get_options_price",
    "serveral_args": [
        {"query_type": 2, "market_code": 0, "commodity_id": "TXO"},
        {"query_type": 2, "market_code": 1, "commodity_id": "TXO"}
    ]
  },
  "twse_taiex_table": {
    "spider": "TWSE_get_taiex",
  },
  "twse_efi_table": {
    "spider": "TWSE_get_efi"
  },
  "twse_stock_table": {
    "spider": "TWSE_get_stock"
  },
  "twse_big3_stock_table": {
    "spider": "TWSE_get_big3_stock"
  },
  "twse_big3_trading_value_table": {
    "spider": "TWSE_get_big3_trading_value"
  },
  "twse_stock_daily_ratio": {
    "spider": "TWSE_get_stock_ratio",
  },
  "twse_stock_oddlot": {
    "spider": "TWSE_get_oddlot"
  },
  "twse_get_margin_trading": {
    "spider": "TWSE_get_margin_trading"
  },
  "tpex_stock_table": {
    "spider": "TPEX_get_stock",
  },
  "tpex_big3_trading_value_table": {
    "spider": "TPEX_get_big3_trading_value",
  },
  "tpex_big3_trading_value_table2": {
    "spider": "TPEX_get_big3_trading_value2"
  }
}
