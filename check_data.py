from check_data_helper import *

current_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
start_date = datetime.strptime("2020-10-08", "%Y-%m-%d")
end_date = datetime.strptime("2020-10-08", "%Y-%m-%d")
day_count = (end_date - start_date).days + 1


def pass_args(date, table):
    pass_args = {
        'project': 'data_crawler',
        'query_date': date
    }
    for arg in table:
        pass_args[arg] = table[arg]

    return pass_args


# check table
print('Start crawling at: ' + current_datetime)
print('===========================')
for table in table_spider_dict:
    print("table: " + table)
    table = table_spider_dict[table]

    # ------- to be implement --------
    for single_date in [start_date + timedelta(n) for n in range(day_count)]:
        if (single_date.isoweekday() != 6 and single_date.isoweekday() != 7):
            single_date = strftime("%Y-%m-%d", single_date.timetuple())

            # query table to get lost date

            # if find lost date:
            pass_parameters = pass_args(single_date, table)
            print(pass_parameters)
            Crawldata(pass_parameters)
    # ------- to be implement --------
