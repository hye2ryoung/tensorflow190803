from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsCrawler:
    def __init__(self, url):
        self.url = url

    # 외부에서 가져온 url을 보관해두고 추후 반복해서 사용하기 위함
    # 필요한 값만 가져옴

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'html.parser')
        n_artist = 0
        n_title = 0
        for i in soup.find_all(name='p', attrs=({'class':'artist'})):
            n_artist +=1
            print(str(n_artist)+ '위')
            print('아티스트: '+i.find('a').text)
        print('-------------')
        for i in soup.find_all(name='p', attrs=({'class':'title'})):
            n_title += 1
            print(str(n_title) + '위')
            print('음악: ' + i.text)

    # find('a') 추가여부는 'a'태그가 끼어있느냐 아니냐의 차이
