import requests
from urlextract import URLExtract
from bs4 import BeautifulSoup
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", required=True)
args = parser.parse_args()
company = args.target


def main():
    url = 'https://www.reversewhois.io/?searchterm=' + company
    Path("/home/kali/DNS/" + company).mkdir(parents=True, exist_ok=True)
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    extractor = URLExtract()
    urls = extractor.find_urls(str(soup.find_all("table")))
    strlist = '\n'.join(urls)
    with open("/home/kali/DNS/" + company + "/reverse_whois.txt", "w") as text_file:
        text_file.write(strlist)

if __name__ == "__main__":
    main()
