from check_data_helper import *

current_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
start_date = datetime.strptime("2020-10-08", "%Y-%m-%d")
end_date = datetime.strptime("2020-10-08", "%Y-%m-%d")
day_count = (end_date - start_date).days + 1


def start_crawl_data(date, table):
    init_args = {
        'project': 'data_crawler',
        'spider': table['spider'],
        'query_date': date,
    }

    if 'serveral_args' in table:
        args = table['serveral_args']
        for arg in args:
            request_args = get_request_args(init_args, arg)
            print("request parameters: " + str(request_args))
            Crawldata(request_args)
    else:
        print("request parameters: " + str(init_args))
        Crawldata(init_args)


def get_request_args(pass_arg, arg):
    for a in arg:
        pass_arg[a] = arg[a]
    return pass_arg


if __name__ == '__main__':
    # check table
    print('Start crawling at: ' + current_datetime)
    print('===========================')
    for table in table_spider_dict:
        print("table: " + table)
        print('=======')
        table = table_spider_dict[table]
        # ------- to be implement --------
        for single_date in [start_date + timedelta(n) for n in range(day_count)]:
            if (single_date.isoweekday() != 6 and single_date.isoweekday() != 7):
                single_date = strftime("%Y-%m-%d", single_date.timetuple())

                # query table to get lost date

                # if find lost date:
                start_crawl_data(single_date, table)
        # ------- to be implement --------
