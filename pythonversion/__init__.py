import requests
from bs4 import BeautifulSoup


url = "https://www.python.org/downloads/"
link_download = "https://www.python.org"
link_notes = "https://docs.python.org"
req = requests.get(url)
print(req)


def get_relese_version():
    soup = BeautifulSoup(req.content, 'html.parser')
    release_versions = soup.find_all('span', 'release-number')
    for release_version in release_versions:
        print(release_version.text)


def get_relese_date():
    soup = BeautifulSoup(req.content, 'html.parser')
    release_dates = soup.find_all('span', 'release-date')
    for release_date in release_dates:
        print(release_date.text)


def get_link_download():
    soup = BeautifulSoup(req.content, 'html.parser')
    downloads = soup.find_all('span', 'release-download')

    for download in downloads:
        links = download.find_all('a')
        for links_tag in links:
            try:
                full_link = link_download+links_tag['href']
            except:
                full_link = "Link is not available"
            print(full_link)


def get_link_notes():
    soup = BeautifulSoup(req.content, 'html.parser')
    notes = soup.find_all('span', 'release-enhancements')

    for note in notes:
        links_notes = note.find_all('a')
        for links_tag_notes in links_notes:
            try:
                full_link_notes = link_notes+links_tag_notes['href']
            except:
                full_link_notes = "Link is not available"
            print(full_link_notes)


if __name__ == '__main__':
    get_relese_version()
    get_relese_date()
    get_link_download()
    get_link_notes()

    