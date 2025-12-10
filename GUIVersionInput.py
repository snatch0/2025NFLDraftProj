import requests
import customtkinter
from PIL import Image, ImageTk
import tempfile
import os
import io

topImagePath = r"C:\Users\zapata1498\Downloads\NFL-logo.png" #top image path
topImagePath2 = r"C:\Users\zapata1498\Downloads\2025_NFL_Draft_logo.png"#top image path 2
random_img = r"C:\Users\zapata1498\Desktop\python\unknown-person-hidden-covered-masked-600nw-1552977773.png"
app = customtkinter.CTk() #main app window
userDraftInput = customtkinter.StringVar() #user input variable
plrName= customtkinter.StringVar() # player name variable
date_recent_gameA = customtkinter.StringVar() #date of recent game variable
teamA = customtkinter.StringVar() # team variable 
opponentA = customtkinter.StringVar()# opponent variable
winOrLoseA = customtkinter.StringVar()# win or lose variable
score_ofRecentGameA = customtkinter.StringVar()# score of recent game variable
globalDraftNumberVariable = customtkinter.StringVar()# draft number variable
imgSlot = customtkinter.StringVar()# image slot variable
imgSlot.set(random_img) # set default image path

flexImg = None# global image variable
def changeImg():# function to change image
    global flexImg
    draftNumber = draftInput.get()# get draft number from input
    
    plr_info_file = open("imgsources.txt", "r")# open image sources file
    img_url = None# initialize image url variable   
    for line in plr_info_file:# loop through lines in file
        field = line.split("\t")# split line into fields
        if field[0] == draftNumber:# check if draft number matches
            img_url = field[1].strip()# get image url
            break# break loop
    print(img_url)
    if img_url == "N/A":# if image url is N/A
        img_url = random_img# set image url to default image path
        flexImg = customtkinter.CTkImage(light_image=Image.open(img_url), size=(150, 200))# Resize the image for CTk
        profileLabel.configure(image=flexImg)# Update the profile label with the new image
        profileLabel.image = flexImg
    else: # if image url is found
        try:
            response = requests.get(img_url, stream=True, timeout=6) # Download the image
            image_data = response.content# Get the image data
            pil_image = Image.open(io.BytesIO(image_data))# Open the image with PIL
            flexImg = customtkinter.CTkImage(light_image=pil_image, size=(150, 200))#q Resize the image for CTk
            profileLabel.configure(image=flexImg)# Update the profile label with the new image
            profileLabel.image = flexImg
        except Exception as e:
            # fallback to default local image if download fails
            try:
                flexImg = customtkinter.CTkImage(light_image=Image.open(random_img), size=(150, 200))
                profileLabel.configure(image=flexImg)
                profileLabel.image = flexImg
            except Exception:
                print("Failed to load image:", e)
    
    

def returnPlrInfo():# function to return player info
    changeImg()# change image based on draft number
    draft_number = draftInput.get()# get draft number from input
    
    print(draft_number)# print draft number to console

    plr_info_file = open("plrinfo.txt", "r")# open player info file
    for line in plr_info_file:# loop through lines in file
        if line.startswith(draft_number):# check if line starts with draft number
            player_name = line.split("\t")[1]# get player name
            draftN = line.split("\t")[0]# get draft number
            date_recent_game = line.split("\t")[2]# get date of recent game
            team = line.split("\t")[3]# get team
            opponent = line.split("\t")[4]# get opponent
            winOrLose = line.split("\t")[5]# get win or lose
            score_ofRecentGame = line.split("\t")[6]# get score of recent game
            print( player_name)
            print(draft_number)
            print(date_recent_game)
            print(team)
            print(opponent)
            print(winOrLose)
            print(score_ofRecentGame)#print all values to console
            plrName.set(player_name)
            globalDraftNumberVariable.set("Draft Number: " + draftN)
            date_recent_gameA.set("Date of Recent Game: " + date_recent_game)
            teamA.set("Team: " + team)
            opponentA.set("Opponent: " + opponent)    
            winOrLoseA.set("W/L: " + winOrLose)
            score_ofRecentGameA.set("Score of Recent Game: " + score_ofRecentGame)# set all variables for labels
            break


generalFont = ("Roboto", 30, "bold") #general font for app

app.title("NFL 2025 DRAFT APP")
app.geometry("900x700")
app.configure(fg_color="#333333")



topLabel = customtkinter.CTkLabel(app, text="NFL 2025 Draft App", font=generalFont, text_color="white",
fg_color="#222222",
corner_radius=15
)
#frame in progress

      

cardFrame = customtkinter.CTkFrame(app, width=600, height=700, corner_radius=15, fg_color="#222222")

# make the cardFrame layout smoother: dedicated two columns (image + info)
cardFrame.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
#cardFrame.grid_columnconfigure(0, weight=1)  # image column
#cardFrame.grid_columnconfigure(1, weight=1)  # info column
    

pil_image = Image.open(random_img) #base image opened

topImage1 = Image.open(topImagePath) #top image 1 opened

topImage2 = Image.open(topImagePath2) #top image 2 opened



randomImgUpload = customtkinter.CTkImage(light_image=pil_image, size=(150, 200)) #resize image for CTk

nflLogo = customtkinter.CTkImage(light_image=topImage1, size=(120, 100)) #resize top image 1 for CTk
nflDraftLogo = customtkinter.CTkImage(light_image=topImage2, size=(100, 100)) #resize top image 2 for CTk

topImageLabel1 = customtkinter.CTkLabel(app, image=nflLogo, text="") #top image 1 label
topImageLabel2 = customtkinter.CTkLabel(app, image=nflDraftLogo, text="") #top image 2 label

profileLabel = customtkinter.CTkLabel(cardFrame, image=randomImgUpload, text="") #image label
profileLabel.image = randomImgUpload

askLabel = customtkinter.CTkLabel(app, text="Enter Draft Number:", font=("Roboto", 30, "bold"), text_color="white") #ask label


draftInput = customtkinter.CTkEntry(app, width=150, height=40, font=("Roboto", 20), textvariable=userDraftInput) #draft input entry


findButton = customtkinter.CTkButton(app, text="Find Player", font=("Roboto", 20), width=150, height=40, command=returnPlrInfo) #find button

cardFrame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
rookieLabel = customtkinter.CTkLabel(cardFrame, text="", font=("Roboto", 10), text_color="white")# rookie label
plrNameLabel = customtkinter.CTkLabel(cardFrame, text=plrName.get(), font=("Roboto", 10), text_color="white", textvariable=plrName)# player name label
draftNumberLabel = customtkinter.CTkLabel(cardFrame, text=globalDraftNumberVariable.get(), font=("Roboto", 10), text_color="white", textvariable=globalDraftNumberVariable)# draft number label
dateGameLabel = customtkinter.CTkLabel(cardFrame, text=date_recent_gameA.get(), font=("Roboto", 10), text_color="white", textvariable = date_recent_gameA)# date of game label
teamLabel = customtkinter.CTkLabel(cardFrame, text=teamA.get(), font=("Roboto", 10), text_color="white", textvariable=teamA)# team label
opponentLabel = customtkinter.CTkLabel(cardFrame, text=opponentA.get(), font=("Roboto", 10), text_color="white", textvariable=opponentA)# opponent label
winOrLoseLabel = customtkinter.CTkLabel(cardFrame, text=winOrLoseA.get(), font=("Roboto", 10), text_color="white", textvariable=winOrLoseA)# win or lose label
scoreLabel = customtkinter.CTkLabel(cardFrame, text=score_ofRecentGameA.get(), font=("Roboto", 10), text_color="white", textvariable = score_ofRecentGameA)# score label
# This makes the middle columns expand to fill available space

  # allow the card area to expand vertically

topLabel.grid(row=0, column=1, padx=20, pady=20, sticky="ew")       # Center label
topImageLabel1.grid(row=0, column=0, padx=20, pady=20, sticky="w")  # Left image
topImageLabel2.grid(row=0, column=4, padx=20, pady=20, sticky="e")  # Right image

askLabel.grid(row=1, column=0, padx=20, pady=10, sticky="w")# ask label grid
draftInput.grid(row=1, column=1, padx=20, pady=10, sticky="w")# draft input grid
findButton.grid(row=1, column=2, padx=20, pady=10, sticky="w")# find button grid

# smoother card layout: image on left, info stacked on right
profileLabel.grid(row=0, column=0, rowspan=8,  padx=20, pady=20, sticky="n") #image label grid

# place info labels in the info column (col 1) with consistent spacing
rookieLabel.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")# rookie label grid
plrNameLabel.grid(row=1, column=1, padx=10, pady=(2, 5), sticky="w")# player name label grid
draftNumberLabel.grid(row=2, column=1, padx=10, pady=(2, 5), sticky="w")# draft number label grid
dateGameLabel.grid(row=3, column=1, padx=10, pady=(2, 5), sticky="w")# date of game label grid
teamLabel.grid(row=4, column=1, padx=10, pady=(2, 5), sticky="w")# team label grid
opponentLabel.grid(row=5, column=1, padx=10, pady=(2, 5), sticky="w")# opponent label grid
winOrLoseLabel.grid(row=6, column=1, padx=10, pady=(2, 5), sticky="w")# win/lose label grid
scoreLabel.grid(row=7, column=1, padx=10, pady=(2, 20), sticky="w")# score label grid




app.mainloop()
#FIX NOTES

#make the layout like a "card"
