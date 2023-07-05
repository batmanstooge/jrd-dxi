import requests

from web_contents_to_match_processor import WebContentsToMatchProcessor


class WebsiteToMatchProcessor:
    def __init__(self, website_url):
        self.website_url = website_url

    def get_match_from_website(self):
        with requests.get(self.website_url) as response:
            response_text = response.text
        webcontents_to_match_processor = WebContentsToMatchProcessor()
        return webcontents_to_match_processor.get_match_from_web_contents(response_text)