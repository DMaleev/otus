import requests
import json
from bs4 import BeautifulSoup
import re


def Search(query):
    url = "https://www.googleapis.com/customsearch/v1"

    querystring = {"key": "AIzaSyBb5--FfYlMHo9YaUyBtqFXHeHDM6vWsYk",
                   "q": query, "cx": "016824827695669141744:9y9pzmyysvi"}

    response = requests.request("GET", url, params=querystring)

    return response.text


def Parse(res, count):
    items = json.loads(res)
    results = []
    for item in items['items']:
        results.append(item['link'])
    return results[:count]


def recursion(link):
    html_page = requests.get(link)
    soup = BeautifulSoup(html_page.text, features="html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        if link.get('href'):
            print(link.get('href'))


q = input("Your Query: ")
count = int(input("Count: "))
result = Parse(Search(q), count)
rec = input("Recursion? (Y/N): ")
for link in result:
    print("Google link: " + link)
    if(rec == "Y"):
        print("Recursion results: ")
        print(recursion(link))
        print('')
