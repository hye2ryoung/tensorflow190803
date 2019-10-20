from bs4 import BeautifulSoup
from selenium import webdriver

class NaverMovie:
    def __init__(self, url):
        self.driver = webdriver.Chrome(executable_path='C:/Users/HyeRyoung Kim/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        self.driver.get(url)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def scrap(self):
        html = self.soup.prettify()
        # print(html)
        all_divs = self.soup.find_all('div', attrs={'class':'tit3'})
        print(all_divs)
        arr = [div.a.string for div in all_divs]
        # html 구조 확인. div.a. 트리구조에서 내려오는 것. string으로 씀
        for i in arr:
            print(i)
        self.driver.close()