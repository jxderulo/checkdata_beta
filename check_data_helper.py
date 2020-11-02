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
  # "taifex_big3_futures_table": {
  #   "spider": "TAIFEX_get_big3_futures",
  #   "commodity_id": ["TXF", "MXF", "FXF", "EXF"]
  # },
  # "taifex_large_trader_futures_table": {
  #   "spider": "TAIFEX_get_large_trader_futures",
  #   "contract_id": []
  # },
  # "taifex_futures_price_table": {
  #   "spider": "TAIFEX_get_futures_price"
  #   "query_type": [],
  #   "market_code": [],
  #   "commodity_id": []
  # },
  # "taifex_big3_options_table": {
  #   "spider": "TAIFEX_get_big3_options",
  #   "query_type": [],
  #   "do_query": [],
  #   "commodity_id": []
  # },
  # "taifex_large_trader_options_table": {
  #   "spider": "TAIFEX_get_large_trader_options",
  #   "contract_id": []
  # },
  # "taifex_options_price_table": {
  #   "spider": "TAIFEX_get_options_price",
  #   "query_type": [],
  #   "market_code": [],
  #   "commodity_id": []
  # },
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
    "spider": "TPEX_get_big3_trading_value"
  }
}
