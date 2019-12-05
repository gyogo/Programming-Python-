from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

if __name__ == '__main__':
    #다음웹툰 > 취향저격 그녀 제목을 가져오자
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
        j = json.loads(data.read())      #httpResponse -> json
    #     ctrl + y 하면 한 line지우기  # ctrl + d 하면 한줄 복사
    html = "<html><head><meta charset='utf-8'></head></body>"
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]  # data.webtoon.webtoonEpisodes
    for cartoon_title in cartoon_titles:
        title = cartoon_title['title']
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/"+str(url)
        html += "<a href='{}'><img src='{}'/>{}</a>".format(url,thumbnail,title)
    html += "</body></html>"

    outputSoup = BeautifulSoup(html,"lxml")                # 내가생성한 html 문자열을 soup 객체로 만들자
    prettyHtml = str(outputSoup.prettify())                 # 예쁘게 html 코드로 만들자
    with open("취향저격 그녀.html","w",encoding="utf-8") as f:        #html 파일 만들자
        f.write(prettyHtml)



    # # cartoon_titles = soup.find_all("strong",attrs={"class : ": "tit_wt"})
    # cartoon_titles = soup.find_all("li")
    # for cartoon_titles in cartoon_titles:
    #     print(cartoon_titles)
    # print(soup)
    # html = "<html><head><meta charset='utf-8'></head><body>"
    # cartoon_titles = soup.find_all("td", attrs={"class":"title"})   #<td class="title">...</td>
    # for cartoon_titles in cartoon_titles:                   # cartoon_titles[:2]를 해서 원하는 화까지 정할수 있음
    #                                                         #가장 최신화하려면
    #     title = cartoon_titles.find("a").text                   #텍스트 가져오기.<a>text</a>
    #     link = cartoon_titles.find("a").get("href")             #태그의 속성값 가져오기.<a href="">text</a>
    #     link = "https://comic.naver.com" + link
    #     print(title)
    #     print(link)
    #     html += "<a html='{}'> {} </a><br>".format(link,title)      #<a href='Link'>title</a>
    # html += "</body></html>"
    # # print(html)
    # outputSoup = BeautifulSoup(html,"lxml")                # 내가생성한 html 문자열을 soup 객체로 만들자
    # prettyHtml = str(outputSoup.prettify())                 # 예쁘게 html 코드로 만들자
    # with open("원수를 사랑하라.html","w",encoding="utf-8") as f:        #html 파일 만들자
    #     f.write(prettyHtml)

