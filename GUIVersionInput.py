import customtkinter
from PIL import Image

app = customtkinter.CTk()
bubbleFont = ("Impact", 30)

app.title("NFL 2025 DRAFT APP")
app.geometry("400x300")
app.configure(fg_color="#333333")
app.grid_columnconfigure(0, weight=1)

topLabel = customtkinter.CTkLabel(app, text="NFL 2025 Draft App", font=bubbleFont, text_color="white")
topLabel.grid(row=0, column=0, padx=20, pady=(20, 10))

pil_image = Image.open("https://www.shutterstock.com/image-vector/unknown-person-hidden-covered-masked-600nw-1552977773.jpg")



app.mainloop()