from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
from ad_item import AdItem
import json
import requests


def write_to_ads_file(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()


last_post_date = '672725508589394'
ads_data = ""
for i in range(5):
    post_data = '{"json_schema":{"category":{"value":"stationery"}},"last-post-date":' + last_post_date + ' }'
    response = requests.post('https://api.divar.ir/v8/search/3/stationery', post_data)
    json_data = json.loads(response.text.encode('utf-8').decode('unicode_escape'))
    json_items = json_data['widget_list']
    ads_data += '\n'.join([item['data']['title'] for item in json_items])
    last_post_date = str(json_data['last_post_date'])
write_to_ads_file('divaradds.txt', ads_data)


if __name__ == "__main__":
    url = input()
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    item_links = soup.find_all('a', 'kt-post-card kt-post-card--outlined kt-post-card--has-chat')
    data = ""
    for item_link in item_links:
        item = AdItem('http://divar.ir' + quote(item_link.get('href')))
        data += item.get_ad_details() + "------------------------\n"
    result_file = open('result.txt', 'w')
    result_file.write(data)
    result_file.close()
