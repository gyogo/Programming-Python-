#복지로 > 복지서비스 > 한눈에 보는 복지정보 > 아동 청소년 > 100개씩 보기
#post방식으로 숨겨져있는 것들을 변수를 넘겨줘서 원하는 값뽑기
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    url ="http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data={"searchIntClId":"03", "pageUnit":"100"}
    with requests.post(url, data) as response:
        soup = BeautifulSoup(response.text,"lxml")
    # print(soup)
    titles = soup.select("dt.tit > a") #<dt class="title"><a></a></dt>
    for title in titles:
        print(title.text)