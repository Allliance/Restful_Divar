from urllib.request import urlopen
from bs4 import BeautifulSoup


class AdItem:

    def __init__(self, link):
        page = urlopen(link)
        self.soup = BeautifulSoup(page, 'html.parser')

    def get_ad_details(self):
        title = self.soup.find('h1', 'kt-page-title__title kt-page-title__title--responsive-sized').text.strip()
        subtitle = self.soup.find('div',
                                  'kt-page-title__subtitle kt-page-title__subtitle--responsive-sized').text.strip()
        state = self.soup.find('p', 'kt-unexpandable-row__value').text.strip()
        details = self.soup.find('p',
                                 'kt-description-row__text post-description kt-description-row__text--primary').text.strip()
        result = "Title: " + title + "\n"
        result += "Subtitle: " + subtitle + "\n"
        result += "State: " + state + "\n"
        result += "Details: " + details + "\n"
        return result
