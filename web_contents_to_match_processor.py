from bs4 import BeautifulSoup

from soup_match_processor import SoupToMatchProcessor


class WebContentsToMatchProcessor:
    def get_match_from_web_contents(self, web_contents):
        soup = BeautifulSoup(web_contents, "html.parser")
        if len(soup.findAll("span", string="No result")) == 1:
            return None
        soup_to_match_processor = SoupToMatchProcessor()
        return soup_to_match_processor.get_match_from_soup(soup)