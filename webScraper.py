import requests
from bs4 import BeautifulSoup
infosheet = open("plrinfo.txt", "w")
infosheet.write("#DRAFT" + "\t" + "NAME" + "\t" + "DATE OF RECENT GAME" + "\t" + "TEAM" + "\t" + "OPP" + "\t" + "W/L" + "\n")
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
        mainStr = str(draftNum) + "." + "\t" + name + "\n"
        

        url_player = url + a_tag['href']  # get the href attribute, e.g., "/players/W/WardCa00.htm"
        plrResponse = requests.get(url_player)
        soupPlr = BeautifulSoup(plrResponse.content, 'html.parser')
        plrTable = soupPlr.find('table', id='last5')
        if plrTable:
            lastGameRow = plrTable.find('tr')
            if lastGameRow:
                date_td = lastGameRow.find('td', attrs={'data-stat': 'date'})
                team_td = lastGameRow.find('td', attrs={'data-stat': 'team_name_abbr'})
                opp_td = lastGameRow.find('td', attrs={'data-stat': 'opp_name_abbr'})
                result_td = lastGameRow.find('td', attrs={'data-stat': 'game_result'})
                
                date = date_td.text.strip() if date_td else "N/A"
                team = team_td.text.strip() if team_td else "N/A"
                opp = opp_td.text.strip() if opp_td else "N/A"
                result = result_td.text.strip() if result_td else "N/A"
                
                mainStr = str(draftNum) + "\t" + name + "\t" + date + "\t" + team + "\t" + opp + "\t" + result + "\n"
        infosheet.write(mainStr)
        draftNum += 1

