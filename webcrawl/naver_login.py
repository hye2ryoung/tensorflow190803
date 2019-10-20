from bs4 import BeautifulSoup
from selenium import webdriver
class NaverLogin:
    def __init__(self, url):
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/HyeRyoung Kim/PycharmProjects/tensorflow190803/webcrawl/data/chromedriver')
        self.driver.implicitly_wait(3)
        self.driver.get(url)

    def auto_login(self):
        self.driver.find_element_by_name('id').send_keys('****')
        self.driver.find_element_by_name('pw').send_keys('****')
        self.driver.implicitly_wait(3)
        # html 화면에서 form id= 으로 시작하는 formtag를 잡음. id="frmNIDLogin"
        # * : 무엇이 있건간에, 뒤에 있는 것이 []에 있는 값이면 실행
        self.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(3)

        self.driver.get('https://order.pay.naver.com/home')
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        notices = soup.select('div.p_inr > div.p_info > a > span')

        for i in notices:
            print(i.text.strip())