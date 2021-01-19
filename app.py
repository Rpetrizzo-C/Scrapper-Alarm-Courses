import requests
from bs4 import BeautifulSoup
url = "https://allcoursefree.com/"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}


def check_status():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', attrs={"class":'site-title'}).get_text()
    courses = soup.find('p', attrs={"class":'woocommerce-result-count'}).get_text()
    print(title) 
    quantity = int(courses[-11:-8])
    print (quantity)
    if quantity != 13:
        print("idiot")
check_status()

  