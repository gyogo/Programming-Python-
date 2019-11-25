#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버 웹툰> 유미의 세포 제목 가져오기
    data= urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=651673")
    soup = BeautifulSoup(data, "lxml")
    cartoon_titles = soup.find_all("td",attrs={"class":"title"})
    for cartoon_title in cartoon_titles:
        title = cartoon_title.find("a").text
        link = cartoon_title.find("a").get("href")
        link = "https://comic.naver.com"+link
        print(title)
        print(link)