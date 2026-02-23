import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# It will take URL from command line
url = sys.argv[1]

response = requests.get(url)

# It will create soup of texts using html parser
soup = BeautifulSoup(response.text, "html.parser")

print(f"PAGE TITLE WITHOUT ANY HTML TAG:{soup.title.text} \n")
print()

print("PAGE BODY TEXT IN LOWERCASE:")
Sentence_Body=(soup.get_text()).split()
Sentence_Body_lowercase=[]
for i in Sentence_Body:
  Sentence_Body_lowercase.append(i.lower())
print(Sentence_Body_lowercase)
print()
print()
print()

print("ALL THE URLS THAT THE PAGE POINTS TO: \n")

for link in soup.find_all("a"):
    href = link.get("href")
    
    if href:
        full_url = urljoin(url, href)
        print(full_url)
