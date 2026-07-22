import os
import urllib.request
from bs4 import BeautifulSoup


os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)


PAGE = "https://hotcakex.github.io/Official-IANA-IP-blocks/"


print("Reading page...")

html = urllib.request.urlopen(PAGE).read()

soup = BeautifulSoup(html, "html.parser")


url = None

for a in soup.find_all("a"):
    text = a.text.strip()

    if text == "TXT":
        href = a.get("href")

        if href and "IR" in href:
            url = href
            break


if not url:
    print("Iran TXT link not found")
    exit(1)


print("Downloading:")
print(url)


urllib.request.urlretrieve(
    url,
    "data/current.txt"
)


print("Download OK")
