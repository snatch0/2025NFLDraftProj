import requests
from bs4 import BeautifulSoup

url = 'https://www.pro-football-reference.com/years/2025/draft.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
draftNum = 1
table = soup.find('table', id='drafts')
for td in table.find_all('td', attrs={'class': 'left', 'data-stat': 'player'}):
    a_tag = td.find('a')  # find the <a> inside the <td>
    if a_tag:
        name = a_tag.text.strip()  # get the visible player name, e.g., "Cam Ward"
        print(str(draftNum) + ". " + name)
        draftNum += 1
