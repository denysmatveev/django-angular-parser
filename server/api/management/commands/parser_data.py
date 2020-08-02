from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import lxml.html
from lxml import etree

from django.core.management.base import BaseCommand
from api.models import DataList


class GoogParser:
    """Scrape balance sheet of GOOGLE"""

    def __init__(self):
        self.url = 'https://finance.yahoo.com/quote/GOOG/balance-sheet?p=GOOG'

    def get_html_page(self):
        """Getting html page from url"""

        chrome_path = './chromedriver'
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        browser = webdriver.Chrome(ChromeDriverManager().install(),
                                   options=chrome_options)

        browser.get(self.url)

        browser.set_window_size(1366, 768)
        browser.find_elements_by_xpath('//*[@id="Col1-1-Financials-Proxy"]\
                                        /section/div[2]/button')[0].click()
        html_page = browser.page_source
        browser.quit()
        return html_page

    def append_to_list(self, page_text):
        data = []
        for value in page_text:
            data.append(value.get_text())
        return data

    def arrange_data(self, data_breakdown, data_one_three, data_two_four):
        final_data = []
        for i in range(len(data_breakdown)):
            final_data.append({
                'title': data_breakdown.pop(0),
                'date_12_30_2019': data_one_three.pop(0),
                'date_12_30_2018': data_two_four.pop(0),
                'date_12_30_2017': data_one_three.pop(0),
                'date_12_30_2016': data_two_four.pop(0)
            })
        return final_data

    def soup_parser(self):
        """Scraping Balance Sheet in html page"""

        html_page = self.get_html_page()
        if html_page:
            soup = BeautifulSoup(html_page, 'lxml')

            # get Breakdown column of the table
            column_breakdown = soup.find_all('span', class_='Va(m)')
            data_breakdown = self.append_to_list(column_breakdown)

            for _ in range(3):
                del data_breakdown[0]

            # get the first and third column of the table
            column_one_three = soup.find_all('div', class_='Ta(c) Py(6px) '
                                             'Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) '
                                             'Miw(140px)--pnclg D(tbc)')

            data_one_three = self.append_to_list(column_one_three)

            # get the second and fourth column of the table
            column_two_four = soup.find_all('div', class_='Ta(c) Py(6px) Bxz(bb) '
                                            'BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg '
                                            'Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)')

            data_two_four = self.append_to_list(column_two_four)

            final_list = self.arrange_data(
                data_breakdown, data_one_three, data_two_four)

            return final_list


class Command(BaseCommand):
    help = 'Парсинг https://finance.yahoo.com/quote/GOOG/balance-sheet?p=GOOG'

    def handle(self, *args, **kwargs):
        finance = GoogParser()
        data = finance.soup_parser()

        for value in data:
            p = DataList(
                title=value['title'],
                date_2019=value['date_12_30_2019'],
                date_2018=value['date_12_30_2018'],
                date_2017=value['date_12_30_2017'],
                date_2016=value['date_12_30_2016']
            ).save()
