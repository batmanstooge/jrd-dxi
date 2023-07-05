import requests
from bs4 import BeautifulSoup

from models.match import Match
from pandas_processor import PandasProcessor
from website_to_match_processor import WebsiteToMatchProcessor

WEB_SITE_URLS = [
    "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/derbyshire-vs-lancashire-north-group-1347569/full-scorecard"
]

pandas_processor = PandasProcessor()

for website_url in WEB_SITE_URLS:
    website_to_match_processor = WebsiteToMatchProcessor(website_url)
    match = website_to_match_processor.get_match_from_website()
    pandas_processor.add_match(match)

