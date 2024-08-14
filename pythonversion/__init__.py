import requests
from bs4 import BeautifulSoup

def extract_data():
    global python_release
    try:
        url = 'https://www.python.org/downloads/'
        content=requests.get(url)
    except Exception:
        return None

    if content.status_code == 200:
        soup=BeautifulSoup(content.text, 'html.parser')

        result=soup.find('div', {'class': 'row download-list-widget'})
        result=result.findChildren('li')

        i = 1
        for res in result:
            #print(i, res.text)

def show_data(result):  # mendefinisikan fungsi tampilkan data
    if result is None:
        print("Tidak bisa menemukan data")
    print (result)