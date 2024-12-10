import re
import json
import requests
import datetime
import csv
from tqdm import tqdm
from bs4 import BeautifulSoup
from collections import defaultdict
from urllib.parse import urlparse

submission = defaultdict(list)
src_url = "https://www.moneycontrol.com/news/business/"

# Get next page links and call scrap() on each link
def setup(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        response = requests.get(url)
    else:
        print("Invalid URL")

    nextlinks = []
    src_page = requests.get(url).text
    src = BeautifulSoup(src_page, 'lxml')

    # Ignore <a> with void js as href
    anchors = src.find("div", attrs={"class": "pagenation"}).findAll(
        'a', {'href': re.compile('^((?!void).)*$')}
    )
    nextlinks = [i.attrs['href'] for i in anchors]

    for idx, link in enumerate(tqdm(nextlinks)):
        scrap(link, idx)

# Scrapes passed page URL
def scrap(url, idx):
    src_page = requests.get(url).text
    src = BeautifulSoup(src_page, 'lxml')

    img = src.find("ul", {"id": "cagetory"}).findAll('img')
    # <img> has alt text attr set as heading of news, therefore get img link and heading from same tag
    imgs = [i.attrs['data-src'] for i in img]
    titles = [i.attrs['alt'] for i in img]

    # List of dicts as values and indexed by page number
    for title, img_src in zip(titles, imgs):
        submission[str(idx)].append({'title': title, 'img_src': img_src})

# Save data as JSON named by current date
def json_dump(data):
    date = datetime.date.today().strftime("%B_%d_%Y")
    with open(f'output/moneycontrol_{date}.json', 'w') as outfile:
        json.dump(data, outfile)

# Save data into a CSV file
def save_to_csv(data):
    date = datetime.date.today().strftime("%B_%d_%Y")
    csv_file = f'output/moneycontrol_{date}.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Page", "Title", "Image Source"])

        for page, articles in data.items():
            for article in articles:
                writer.writerow([page, article['title'], article['img_src']])

setup(src_url)
json_dump(submission)
save_to_csv(submission)