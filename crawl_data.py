from datetime import datetime, timedelta
from time import strftime
import time
import requests
import json
import sys


class Logger(object):  # save output to file
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("log.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass


sys.stdout = Logger()

start_date = datetime.strptime("2020-10-08", "%Y-%m-%d")
end_date = datetime.strptime("2020-10-09", "%Y-%m-%d")
day_count = (end_date - start_date).days + 1
current_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

request_parameters = {
    'project': 'data_crawler',
    'spider': 'TAIFEX_get_big3_futures',
    'commodity_id': 'FXF',
    'query_date': ''
}

print('Start crawling at: ' + current_datetime)
print('spider:get_big3_futures')
print('=======================')
for single_date in [start_date + timedelta(n) for n in range(day_count)]:
    if (single_date.isoweekday() != 6 and single_date.isoweekday() != 7):
        single_date = strftime("%Y-%m-%d", single_date.timetuple())
        request_parameters['query_date'] = single_date

        # Crawling data
        response = requests.post('http://localhost:6800/schedule.json', request_parameters)
        jobid = json.loads(response.text)['jobid']
        print('Crawling on date: ' + single_date)

        # check job finished
        response = requests.get('http://localhost:6800/jobs')
        while response.text.find(jobid) < response.text.find('Finished'):
            time.sleep(1)
            response = requests.get('http://localhost:6800/jobs')

        # check Published or not
        check_result_url = 'http://localhost:6800/logs/data_crawler/TAIFEX_get_big3_futures/' + jobid + '.log'
        response = requests.get(check_result_url)
        response.encoding = 'utf8'
        print(check_result_url)
        if 'Publish' in response.text:
            print('Published')
        elif '查無資料' in response.text:
            print('No data today')
        else:
            print('Unknown Error')

        print()
