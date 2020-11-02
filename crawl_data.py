import requests
import json

request_parameters = {
    'project': 'data_crawler',
    'spider': '',
    'commodity_id': '',
    'query_date': ''
}

def Crawldata(spider, single_date):
    request_parameters['spider'] = spider
    request_parameters['query_date'] = single_date
    request_parameters['commodity_id'] = 'TXF'

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
