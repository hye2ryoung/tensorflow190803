from textmining.model import SamsungReport

if __name__ == '__main__':

    sam = SamsungReport()
    # sam.download()
    # nltk(자연어토큰) 다운로드를 위한 명령문
    # nltk 다운 완료된 이후 활성화해서 실행(nltk 다운로드 완료 전까지는 비활성화로 진행)
    print(sam.extract_noun())
    print(sam.read_stopword())
    print(sam.remove_stopword())
    print(sam.find_freq())
    print(sam.draw_wordcloud())