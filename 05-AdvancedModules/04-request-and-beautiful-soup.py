# pip3 install requests
# pip3 install beautifulsoup4

# https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number

import requests
from bs4 import BeautifulSoup

url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

# print(soup.prettify())

table = soup.find_all("table")[1]
table_body = table.find("tbody")

# rows = table_body.find_all('tr', attrs={'style': 'background:#FFF'})
rows = table_body.find_all('tr')
rowsTitle = []

for row in rows:
    all_th = row.find_all('th')
    all_td = row.find_all('td')

    pokemonData = []

    for td in all_td:
        if not str.strip(td.text):
            pokemonData.append('-')
        else:
            pokemonData.append(str.strip(td.text))

    for th in all_th:
        img = th.find("img")
        if img and 'src' in img.attrs:
            src = img.get('src')
            pokemonData.insert(2, src)
        else:
            rowsTitle.append(str.strip(th.text))

    print(pokemonData)


print(rowsTitle)

