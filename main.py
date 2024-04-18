import tkinter as tk
from PIL import Image, ImageTk

# Window Navigation
def openGameMenu():
    mainMenu.withdraw()
    gameMenu.deiconify()
    
def openMainMenu(event=None):
    gameMenu.withdraw()
    mainMenu.deiconify()

# Close all windows
def on_close():
    mainMenu.destroy()

# Main menu
mainMenu = tk.Tk()
mainMenu.title('The voices made me do this')
mainMenu.minsize(800, 600)
mainMenu.protocol("WM_DELETE_WINDOW", on_close)

lblTitle = tk.Label(mainMenu, text='H A N G M A N', font=('Courier', 30)).place(relx=0.5, rely = 0.5, y=-100, anchor='center')
btnGameMenu = tk.Button(mainMenu, text='start game', font=('Courier', 16), command=openGameMenu).place(relx=0.5, rely = 0.5, y=0, anchor='center')

# Game menu
gameMenu = tk.Toplevel(mainMenu)
gameMenu.title('May Allah brought the worst for your family')
gameMenu.minsize(800, 600)
gameMenu.protocol("WM_DELETE_WINDOW", on_close)
gameMenu.bind("<Escape>", openMainMenu)
gameMenu.withdraw()

mainMenu.mainloop()