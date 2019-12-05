#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    data= urlopen("https://www.youtube.com/feed/trending")
    soup = BeautifulSoup(data, "lxml")
    data.close()
    html="<html><head><meta charset='utf-8'></head><body>"
    youtube_titles = soup.find_all("dismissable",attrs={"class":"style-scope ytd-video-renderer"})
    for youtube_title in youtube_titles[:]:
        title = youtube_title.find("a").text
        link = youtube_title.find("a").get("href")
        link = "https://www.youtube.com/"+link
        print(title)
        print(link)
        html+="<a href='{}'>{}</a><br />".format(link,title)
    html=="</body></html>"
    outputSoup = BeautifulSoup(html,"lxml")
    prettyHtml = str(outputSoup.prettify())
    with open("유튜브인기급상승.html","w",encoding="utf-8") as f:
        f.write(prettyHtml)

        # from bs4 import BeautifulSoup
        # import requests
        # import lxml
        #
        #
        # def get_true_video_link(target_url):
        #     response = requests.get(target_url)
        #     soup = BeautifulSoup(response.text, "lxml")
        #     lis = soup.find_all('li', {'class': 'channels-content-item yt-shelf-grid-item'})
        #     for li in lis:
        #         title = li.find('a', {'title': True})['title']
        #         video_link = 'https://www.youtube.com' + li.find('a', {'href': True})['href']
        #         img_link = li.find('img', {'src': True})['src']
        #         play_time = li.find('span', {'class': 'video-time'}).text
        #         hits = li.find_all('li')[2].text
        #         updated_time = li.find_all('li')[3].text
        #         true_video_info = title, video_link, img_link, play_time, hits, updated_time
        #         print(true_video_info)
        #     return true_video_info
        #
        #
        # target_url = 'https://www.youtube.com/user/yootruebeutyroom/videos'
        # get_true_video_link(target_url)