import tkinter as tk
from PIL import Image, ImageTk

# Window Navigation
def openGameMenu(x, y):
    mainMenu.withdraw()
    gameMenu.geometry(f"+{x}+{y}")
    gameMenu.deiconify()
    
def openMainMenu(x, y):
    gameMenu.withdraw()
    mainMenu.geometry(f"+{x}+{y}")
    mainMenu.deiconify()

# Close all windows
def on_close():
    mainMenu.destroy()

# Update hangman image
def updateHangmanImg(value=None):
    img_path = f'img/hangman{sclHangman.get()}.png' 
    image = Image.open(img_path).resize((200, 200))    
    photo = ImageTk.PhotoImage(image)
    lblHangmanImg.config(image=photo)
    lblHangmanImg.image = photo 
    
# Main menu
mainMenu = tk.Tk()
mainMenu.title('The voices made me do this')
mainMenu.minsize(800, 600)
mainMenu.protocol("WM_DELETE_WINDOW", on_close)

lblTitle = tk.Label(mainMenu, text='H A N G M A N', font=('Courier', 30))
lblTitle.place(relx=0.5, rely = 0.5, y=-100, anchor='center')

btnGameMenu = tk.Button(mainMenu, text='start game', font=('Courier', 16), command=lambda: openGameMenu(mainMenu.winfo_x(), mainMenu.winfo_y()))
btnGameMenu.place(relx=0.5, rely = 0.5, y=0, anchor='center')

# Game menu
gameMenu = tk.Toplevel(mainMenu)
gameMenu.title('May Allah brought the worst for your family')
gameMenu.minsize(800, 600)
gameMenu.protocol("WM_DELETE_WINDOW", on_close)
gameMenu.bind("<Escape>", lambda event: openMainMenu(gameMenu.winfo_x(), gameMenu.winfo_y()))
gameMenu.withdraw()

sclHangman = tk.Scale(gameMenu, from_=0, to=7, orient='horizontal', command=updateHangmanImg, length=300)
sclHangman.place(relx=0.5, x=0, y=+300, anchor='center')

image = Image.open('img/hangman0.png').resize((200, 200))
photo = ImageTk.PhotoImage(image)
lblHangmanImg = tk.Label(gameMenu, image=photo)
lblHangmanImg.place(relx=0.5, x=0, y=+50, anchor='n')

mainMenu.mainloop()