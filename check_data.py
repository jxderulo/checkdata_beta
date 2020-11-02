# FOR　所有scrapy
# x=可拿到對應的ˊtable 名稱 >> ME
#
# 抓漏日期的程式(輸入table名稱) > 輸出缺的日期[list]
# for DATE IN 缺的日期[LIST]  >> ME
#  payload輸入<x.DATE
from tool import Logger
from crawl_data import Crawldata
import sys
from datetime import datetime, timedelta
from time import strftime
import time

#save to log file
sys.stdout = Logger()
current_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
start_date = datetime.strptime("2020-10-08", "%Y-%m-%d")
end_date = datetime.strptime("2020-10-09", "%Y-%m-%d")
day_count = (end_date - start_date).days + 1

table_spider_dict = {
    'taifex_big3_futures_table' : 'get_big3_futures',
    'taifex_large_trader_futures_table' : 'get_futures_price'
    # to be extended
}
table_parameter_dict = {

}

# check table
print('Start crawling at: ' + current_datetime)
print('===========================')
for table in table_spider_dict:
    spider = table_spider_dict[table]
    lost_dates = []
    print("table: " + table)
    print("spider: " + spider)

    #------- to be implement --------
    for single_date in [start_date + timedelta(n) for n in range(day_count)]:
        if (single_date.isoweekday() != 6 and single_date.isoweekday() != 7):
            single_date = strftime("%Y-%m-%d", single_date.timetuple())

            # query table to get lost date
            # test data
            lost_dates.append(single_date)

            # test data
            # date = {'date' : single_date, 'commodity_id' : 'TXF'}
            # lost_dates.append(date)
    #------- to be implement --------

    for date in lost_dates:
        # print(date)
        Crawldata(spider, date)
