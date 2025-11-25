import customtkinter
from PIL import Image

random_img = r"C:\Users\zapata1498\Desktop\python\unknown-person-hidden-covered-masked-600nw-1552977773.png"
app = customtkinter.CTk()
userDraftInput = customtkinter.StringVar()
plrName= customtkinter.StringVar()
date_recent_gameA = customtkinter.StringVar()
teamA = customtkinter.StringVar()
opponentA = customtkinter.StringVar()
winOrLoseA = customtkinter.StringVar()
score_ofRecentGameA = customtkinter.StringVar()
globalDraftNumberVariable = customtkinter.StringVar()
imgSlot = customtkinter.StringVar()
imgSlot.set(random_img)
def changeImg():
    print("image changed")
    
    
    

def returnPlrInfo():
    changeImg()
    draft_number = draftInput.get()
    
    print(draft_number)

    plr_info_file = open("plrinfo.txt", "r")
    for line in plr_info_file:
        if line.startswith(draft_number):
            player_name = line.split("\t")[1]
            draftN = line.split("\t")[0]
            date_recent_game = line.split("\t")[2]
            team = line.split("\t")[3]
            opponent = line.split("\t")[4]
            winOrLose = line.split("\t")[5]
            score_ofRecentGame = line.split("\t")[6]
            print( player_name)
            print(draft_number)
            print(date_recent_game)
            print(team)
            print(opponent)
            print(winOrLose)
            print(score_ofRecentGame)
            plrName.set("Name: " + player_name + "\n")
            globalDraftNumberVariable.set("Draft Number: " + draftN + "\n")
            date_recent_gameA.set("Date of Recent Game: " + date_recent_game + "\n")
            teamA.set("Team: " + team + "\n")
            opponentA.set("Opponent: " + opponent + "\n")    
            winOrLoseA.set("W/L: " + winOrLose + "\n")
            score_ofRecentGameA.set("Score of Recent Game: " + score_ofRecentGame + "\n")
            break


bubbleFont = ("Impact", 30)

app.title("NFL 2025 DRAFT APP")
app.geometry("900x700")
app.configure(fg_color="#333333")
app.rowconfigure((0,1), weight=0)
app.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=0)

topLabel = customtkinter.CTkLabel(app, text="NFL 2025 Draft App", font=bubbleFont, text_color="white",
fg_color="#222222",
corner_radius=15
)



pil_image = Image.open(random_img) #base image opened

randomImgUpload = customtkinter.CTkImage(light_image=pil_image, size=(150, 200)) #resize image for CTk

profileLabel = customtkinter.CTkLabel(app, image=imgSlot, text="") #image label


askLabel = customtkinter.CTkLabel(app, text="Enter Draft Number:", font=("Impact", 20), text_color="white")


draftInput = customtkinter.CTkEntry(app, width=150, height=40, font=("Impact", 20), textvariable=userDraftInput)


findButton = customtkinter.CTkButton(app, text="Find Player", font=("Impact", 20), width=150, height=40, command=returnPlrInfo)


rookieLabel = customtkinter.CTkLabel(app, text="Rookie Name:", font=("Impact", 20), text_color="white")

plrNameLabel = customtkinter.CTkLabel(app, text=plrName.get(), font=("Impact", 20), text_color="white", textvariable=plrName)


draftNumberLabel = customtkinter.CTkLabel(app, text=globalDraftNumberVariable.get(), font=("Impact", 20), text_color="white", textvariable=globalDraftNumberVariable)


dateGameLabel = customtkinter.CTkLabel(app, text=date_recent_gameA.get(), font=("Impact", 20), text_color="white", textvariable = date_recent_gameA)


teamLabel = customtkinter.CTkLabel(app, text=teamA.get(), font=("Impact", 20), text_color="white", textvariable=teamA)


opponentLabel = customtkinter.CTkLabel(app, text=opponentA.get(), font=("Impact", 20), text_color="white", textvariable=opponentA)


winOrLoseLabel = customtkinter.CTkLabel(app, text=winOrLoseA.get(), font=("Impact", 20), text_color="white", textvariable=winOrLoseA)


scoreLabel = customtkinter.CTkLabel(app, text=score_ofRecentGameA.get(), font=("Impact", 20), text_color="white", textvariable = score_ofRecentGameA)

topLabel.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

askLabel.grid(row=1, column=0, padx=20, pady=20, sticky="w")
draftInput.grid(row=1, column=1, padx=20, pady=20, sticky="w")
findButton.grid(row=1, column=2, padx=20, pady=20, sticky="w")

profileLabel.grid(row=3, column=0, rowspan=6,  padx=20, pady=20, sticky="nsew") #image label grid

rookieLabel.grid(row=3, column=1, padx=20, pady=20, sticky="w")
plrNameLabel.grid(row=3, column=1, padx=20, pady=20, sticky="nw")
draftNumberLabel.grid(row=4, column=1, padx=20, pady=20, sticky="nw")
dateGameLabel.grid(row=5, column=1, padx=20, pady=20, sticky="nw")
teamLabel.grid(row=7, column=1, padx=20, pady=20, sticky="nw")
opponentLabel.grid(row=7, column=1, padx=20, pady=20, sticky="nw")
winOrLoseLabel.grid(row=8, column=1, padx=20, pady=20, sticky="nw")
scoreLabel.grid(row=9, column=1, padx=20, pady=20, sticky="nw")



app.mainloop()
