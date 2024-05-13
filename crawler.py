import requests
from bs4 import BeautifulSoup

def crawl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            with open("irs_domain.txt", "w") as file:
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href and href.startswith('/'):
                        file.write(href + "\n")
        else:
            print("Failed to retrieve webpage. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # URL of the website to crawl
    # url = input("Enter the URL of the website to crawl: ")
    url = 'https://www.irs.gov';
    crawl(url)
