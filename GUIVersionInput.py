import customtkinter
from PIL import Image

random_img = r"C:\Users\zapata1498\Desktop\python\unknown-person-hidden-covered-masked-600nw-1552977773.png"
app = customtkinter.CTk()
userDraftInput = customtkinter.StringVar()
plrName= customtkinter.StringVar()
date_recent_game = customtkinter.StringVar()
team = customtkinter.StringVar()
opponent = customtkinter.StringVar()
winOrLose = customtkinter.StringVar()
score_ofRecentGame = customtkinter.StringVar()

def returnPlrInfo():
    draft_number = draftInput.get()
    
    print(draft_number)

    plr_info_file = open("plrinfo.txt", "r")
    for line in plr_info_file:
        if line.startswith(draft_number):
            player_name = line.split("\t")[1]
            draft_number = line.split("\t")[0]
            date_recent_game = line.split("\t")[2]
            team = line.split("\t")[3]
            opponent = line.split("\t")[4]
            winOrLose = line.split("\t")[5]
            score_ofRecentGame = line.split("\t")[6]
            
            plrName.set("Name: " + player_name + "\n")
            break


bubbleFont = ("Impact", 30)

app.title("NFL 2025 DRAFT APP")
app.geometry("900x500")
app.configure(fg_color="#333333")
app.grid_columnconfigure(5, weight=1)

topLabel = customtkinter.CTkLabel(app, text="NFL 2025 Draft App", font=bubbleFont, text_color="white")
topLabel.grid(row=0, column=4, padx=20, pady=(20, 10))


pil_image = Image.open(random_img)

randomImgUpload = customtkinter.CTkImage(light_image=pil_image, size=(150, 200))

profileLabel = customtkinter.CTkLabel(app, image=randomImgUpload, text="")
profileLabel.grid(row=1, column=0,pady=(100, 5), padx = 15, sticky="w")

askLabel = customtkinter.CTkLabel(app, text="Enter Draft Number:", font=("Impact", 20), text_color="white")
askLabel.grid(row=1, column=0, padx=20, pady=10, sticky="n")

draftInput = customtkinter.CTkEntry(app, width=150, height=40, font=("Impact", 20), textvariable=userDraftInput)
draftInput.grid(row=1, column=1, padx=20, pady=10, sticky="n")

findButton = customtkinter.CTkButton(app, text="Find Player", font=("Impact", 20), width=150, height=40, command=returnPlrInfo)
findButton.grid(row=1, column=2, padx=20, pady=10, sticky="n")

rookieLabel = customtkinter.CTkLabel(app, text="Rookie Name:", font=("Impact", 20), text_color="white")

plrNameLabel = customtkinter.CTkLabel(app, text=plrName.get(), font=("Impact", 20), text_color="white", textvariable=plrName)
plrNameLabel.grid(row=2, column=2, padx=20, pady=10, sticky="n")

draftNumberLabel = customtkinter.CTkLabel(app, text="Draft Number:", font=("Impact", 20), text_color="white")
draftNumberLabel.grid(row=2, column=1, padx=10, pady=0, sticky="n")

dateGameLabel = customtkinter.CTkLabel(app, text="Date of Recent Game:", font=("Impact", 20), text_color="white")
dateGameLabel.grid(row=3, column=0, padx=20, pady=10, sticky="n")

teamLabel = customtkinter.CTkLabel(app, text="Team:", font=("Impact", 20), text_color="white")
teamLabel.grid(row=4, column=0, padx=20, pady=10, sticky="n")

opponentLabel = customtkinter.CTkLabel(app, text="Opponent:", font=("Impact", 20), text_color="white")
opponentLabel.grid(row=5, column=0, padx=20, pady=10, sticky="n")

winOrLoseLabel = customtkinter.CTkLabel(app, text="W/L:", font=("Impact", 20), text_color="white")
winOrLoseLabel.grid(row=6, column=0, padx=20, pady=10, sticky="n")

scoreLabel = customtkinter.CTkLabel(app, text="Score of Recent Game:", font=("Impact", 20), text_color="white")
scoreLabel.grid(row=7, column=0, padx=20, pady=10, sticky="n")




app.mainloop()
