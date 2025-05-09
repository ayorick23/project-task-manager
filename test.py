# A basic example of overlapping image and button
import customtkinter
from PIL import Image
import pywinstyles

HEIGHT = 500
WIDTH = 500

app = customtkinter.CTk()
app.title("example")
app.geometry((f"{WIDTH}x{HEIGHT}"))
app.resizable(False, False)

Label1 = customtkinter.CTkLabel(master=app, text="", image=customtkinter.CTkImage(Image.open('src/assets/fondo_light_mode.png'), size=(500,500)),
                                width=500, height=500)
Label1.place(x=0, y=0)

Button1 = customtkinter.CTkButton(master=app, width=255, height=172, corner_radius=48,
                                  text='BUTTON', bg_color="#000001") 
Button1.place(x=120, y=57)

#pywinstyles.set_opacity(Button1, color="#000001") # just add this line
#pywinstyles.set_opacity(Button1, value=0.5, color="#000001") # color is not necessary in all cases
pywinstyles.set_opacity(Button1, value=0.5, color="white")

app.mainloop()