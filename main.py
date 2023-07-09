import requests
from bs4 import BeautifulSoup

from models.match import Match
from pandas_processor import PandasProcessor
from website_to_match_processor import WebsiteToMatchProcessor

WEB_SITE_URLS = [
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/derbyshire-vs-lancashire-north-group-1347569/full-scorecard",
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/birmingham-bears-vs-yorkshire-north-group-1347568/full-scorecard",
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/northamptonshire-vs-worcestershire-north-group-1347571/full-scorecard",
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/kent-vs-gloucestershire-south-group-1347572/full-scorecard",
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/somerset-vs-hampshire-south-group-1347570/full-scorecard",
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/lancashire-vs-leicestershire-north-group-1347573/full-scorecard",
    "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/middlesex-vs-surrey-south-group-1347574/live-cricket-score",
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/worcestershire-vs-yorkshire-north-group-1347582/full-scorecard",
    # "https://www.espncricinfo.com/series/vitality-blast-2023-1347399/surrey-vs-kent-south-group-1347575/full-scorecard",
]

pandas_processor = PandasProcessor()

for website_url in WEB_SITE_URLS:
    print(website_url)
    website_to_match_processor = WebsiteToMatchProcessor(website_url)
    match = website_to_match_processor.get_match_from_website()
    if match is not None:
        pandas_processor.add_match(match)

pandas_processor.save_dataframe_to_file()

