import requests
from bs4 import BeautifulSoup
import json

url = "https://www.irs.gov/newsroom/news-releases-for-current-month"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

data = []

for div in soup.find_all("div", class_="field_pup_media_document_teaser"):
    link = div.find("a")
    heading = link.find("span").get_text(strip=True)
    href = link["href"]
    
    content_div = div.find_next_sibling("div", class_="field--name-field-pup-description-abstract")
    if content_div:
        content = content_div.get_text(strip=True)
    else:
        content = "No content found"
    
    data.append({"heading": heading, "link": href, "content": content})

# Write the data to a JSON file
with open("irs_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data scraped and saved to irs_data.json")
