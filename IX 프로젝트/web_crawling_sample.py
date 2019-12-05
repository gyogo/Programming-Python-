
from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    url =""
    data=""
    with requests.post(url, data) as response:
        soup = BeautifulSoup(response.text,"lxml")
    print(soup)