import requests
from bs4 import BeautifulSoup, Comment
import time

infosheet = open("plrinfo.txt", "w") #file where player info will be stored
infosheet.write("#DRAFT" + "\t" + "NAME" + "\t" + "DATE OF RECENT GAME" + "\t" + "TEAM" + "\t" + "OPP" + "\t" + "W/L" + "\n") # header of the file
url = 'https://www.pro-football-reference.com/years/2025/draft.htm' # url of my football site to scrape

response = requests.get(url) # get the page html data
soup = BeautifulSoup(response.content, 'html.parser') # parse the html data with BeautifulSoup
draftNum = 1 # draft pick number starting from 1
table = soup.find('table', class_="sortable stats_table now_sortable sticky_table eq2 eq4 re4 le2", id='drafts') # find the draft table by its class and id


if table is None: # if the table is not found directly
    table = soup.find('table', id='drafts') #find it by id only

if table is None: # if still not found, it might be in comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        if 'id = "drafts"' in comment:
            comment_soup = BeautifulSoup(comment, 'html.parser')
            table = comment_soup.find('table', id='drafts')
            if table:
                break


       

for td in table.find_all('td', attrs={'data-stat': 'player'})[:10]: # loop through each td with data-stat="player"
    a_tag = td.find('a')  # find the <a> inside the <td>
    if a_tag: #if a tag exist
        name = a_tag.text.strip()  # get the visible player name
       
         #print draft and number in terminal
         # main string to write to file
    
        base = 'https://www.pro-football-reference.com' # base url for player pages
        url_player = base + a_tag['href']  # get the href attribute, EX: "/players/W/WardCa00.htm"
        time.sleep(3)  # Be polite and avoid overwhelming the server
        plrResponse = requests.get(url_player) # get the html data for each player
        soupPlr = BeautifulSoup(plrResponse.content, 'html.parser') # parse the html for each player
        plrTable = soupPlr.find('table', id='last5') # find the player table by id 'last5' for last 5 games, WILL NEED AN UPDATE EVERY WEEK MOST LIKELY
        if plrTable:
            lastGameRow = plrTable.find('tr', attrs={'data-row': '7'}) # find the first row which is the most recent game
            if lastGameRow:
                date_td = lastGameRow.find('th', attrs={'data-stat': 'date'}) #find the date of the most recent game within the td
                dateA = date_td.find('a')
                if dateA:
                    date = dateA.text.strip()
                else:
                    date = date_td.text.strip()
                team_td = lastGameRow.find('td', attrs={'data-stat': 'team_name_abbr'}) #find the team name within the td
                opp_td = lastGameRow.find('td', attrs={'data-stat': 'opp_name'}) #find the opponent name within the td
                result_td = lastGameRow.find('td', attrs={'data-stat': 'game_result'}) #find the result within the td
                
                
                team = team_td.text.strip() if team_td else "N/A"
                opp = opp_td.text.strip() if opp_td else "N/A"
                result = result_td.text.strip() if result_td else "N/A"
                
                mainStr = str(draftNum) + "\t" + name + "\t" + date + "\t" + team + "\t" + opp + "\t" + result + "\n" #concantinate all the info into mainStr
                infosheet.write(mainStr)# write it into the infosheet
                print(mainStr) #print the main str in terminal
         
        draftNum += 1 # increment draft number
        
