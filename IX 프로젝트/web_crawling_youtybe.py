from bs4 import BeautifulSoup
# from urllib.request import urlopen
import requests
if __name__ == '__main__':
    url ="https://www.youtube.com/feed/trending"
    with requests.post(url) as response: #request.get도 있어 결과는 같음
        soup = BeautifulSoup(response.text, "lxml")
    # print(soup)
    # youtube_titles = soup.find_all("a",attrs={"class":"yt-uix-tile-link"}) #a태그중에 이 속성을 찾아라!
    youtube_titles = soup.select("a.yt-uix-tile-link") #<a class="yt-iix-tile-link"></a>
    for youtube_title in youtube_titles:
        print(youtube_title.text)