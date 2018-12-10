from tkinter import *

# Create a window
root = Tk()

# create two frames in our window, sets the GameBoard frame on the right, and the Notepad frame on the left
GameBoardframe = Frame(root, bg='blue', bd='10px')
GameBoardframe.pack(side=LEFT)


Notepadframe = Frame(root)
Notepadframe.pack(side=RIGHT)
board = GameBoardframe

# define each Suspect checkbox variable
def var_states():
    print("Miss Scarlett: %d,\nMr. Green: %d,\nCol. Mustard: %d,\nMrs. White: %d,\nProf. Plum: %d,\nMrs. Peacock: %d"
          % (varS1.get(), varS2.get(), varS3.get(), varS4.get(), varS5.get(), varS6.get()))


# set up each Suspect checkbox
Label(Notepadframe, text="Suspects:").grid(row=0, sticky=W)
varS1 = IntVar()
Checkbutton(Notepadframe, text="Miss Scarlett", variable=varS1).grid(row=1, sticky=W)
varS2 = IntVar()
Checkbutton(Notepadframe, text="Mr. Green", variable=varS2).grid(row=2, sticky=W)
varS3 = IntVar()
Checkbutton(Notepadframe, text="Col. Mustard", variable=varS3).grid(row=3, sticky=W)
varS4 = IntVar()
Checkbutton(Notepadframe, text="Mrs. White", variable=varS4).grid(row=4, sticky=W)
varS5 = IntVar()
Checkbutton(Notepadframe, text="Prof. Plum", variable=varS5).grid(row=5, sticky=W)
varS6 = IntVar()
Checkbutton(Notepadframe, text="Mrs. Peacock", variable=varS6).grid(row=6, sticky=W)


# define each WEapon checkbox variable
def var_states():
    print("Knife: %d,\nCandlestick: %d,\nRevolver: %d,\nRope: %d,\nLead Pipe: %d,\nWrench: %d"
          % (varW1.get(), varW2.get(), varW3.get(), varW4.get(), varW5.get(), varW6.get()))


# set up each Weapon checkbox in the Notepad
Label(Notepadframe, text="Weapons:").grid(row=8, sticky=W)
varW1 = IntVar()
Checkbutton(Notepadframe, text="Knife", variable=varW1).grid(row=9, sticky=W)
varW2 = IntVar()
Checkbutton(Notepadframe, text="Candlestick", variable=varW2).grid(row=10, sticky=W)
varW3 = IntVar()
Checkbutton(Notepadframe, text="Revolver", variable=varW3).grid(row=11, sticky=W)
varW4 = IntVar()
Checkbutton(Notepadframe, text="Rope", variable=varW4).grid(row=12, sticky=W)
varW5 = IntVar()
Checkbutton(Notepadframe, text="Lead Pipe", variable=varW5).grid(row=13, sticky=W)
varW6 = IntVar()
Checkbutton(Notepadframe, text="Wrench", variable=varW6).grid(row=14, sticky=W)


# define each Room checkbox variable
def var_states():
    print(
        "Hall: %d,\nLounge: %d,\nDining Room: %d,\nKitchen: %d,\nBallroom: %d,\nConservatory: %d,\nBilliard Room: %d,\nLibrary: %d,\nStudy: %d"
        % (varR1.get(), varR2.get(), varR3.get(), varR4.get(), varR5.get(), varR6.get(), varR7.get(), varR8.get(),
           varR9.get()))


# set up each Room checkbox in the Notepad
Label(Notepadframe, text="Rooms:").grid(row=16, sticky=W)
varR1 = IntVar()
Checkbutton(Notepadframe, text="Hall", variable=varR1).grid(row=17, sticky=W)
varR2 = IntVar()
Checkbutton(Notepadframe, text="Lounge", variable=varR2).grid(row=18, sticky=W)
varR3 = IntVar()
Checkbutton(Notepadframe, text="Dining Room", variable=varR3).grid(row=19, sticky=W)
varR4 = IntVar()
Checkbutton(Notepadframe, text="Kitchen", variable=varR4).grid(row=20, sticky=W)
varR5 = IntVar()
Checkbutton(Notepadframe, text="Ballroom", variable=varR5).grid(row=21, sticky=W)
varR6 = IntVar()
Checkbutton(Notepadframe, text="Conservatory", variable=varR6).grid(row=22, sticky=W)
varR7 = IntVar()
Checkbutton(Notepadframe, text="Billiard Room", variable=varR7).grid(row=23, sticky=W)
varR8 = IntVar()
Checkbutton(Notepadframe, text="Library", variable=varR8).grid(row=24, sticky=W)
varR9 = IntVar()
Checkbutton(Notepadframe, text="Study", variable=varR9).grid(row=25, sticky=W)

root.geometry('1000x1000')
board.grid_columnconfigure( 1, minsize='100')
board.grid_columnconfigure( 2, minsize='100')
board.grid_columnconfigure( 3, minsize='100')
board.grid_columnconfigure( 4, minsize='100')
board.grid_columnconfigure( 5, minsize='100')
board.grid_rowconfigure( 1, minsize='100')
board.grid_rowconfigure( 2, minsize='100')
board.grid_rowconfigure( 3, minsize='100')
board.grid_rowconfigure( 4, minsize='100')
board.grid_rowconfigure( 5, minsize='100')

Label(GameBoardframe, text="study").grid(row=1, column=1)
Label(GameBoardframe, text=" ").grid(row=1, column=2, sticky=W)
Label(GameBoardframe, text= 'Hall').grid(row=1, column=3, sticky=W)
Label(GameBoardframe, text=" ").grid(row=1, column=4, sticky=W)
Label(GameBoardframe, text = 'lounge').grid(row=1, column=5, sticky=W)
Label(GameBoardframe, text="  ").grid(row=2, column=1, sticky=W)
Label(GameBoardframe, text="//////").grid(row=2, column=2, sticky=W, rowspan=2)
Label(GameBoardframe, text="   ").grid(row=2, column=3, sticky=W)
Label(GameBoardframe, text="/////").grid(row=2, column=4, sticky=W, rowspan=2)
Label(GameBoardframe, text="   ").grid(row=2, column=5, sticky=W)
Label(GameBoardframe, text="Library").grid(row=3, column=1, sticky=W)
Label(GameBoardframe, text="  Billiard Room").grid(row=3, column=3, sticky=W)
Label(GameBoardframe, text="Dining Room").grid(row=3, column=5, sticky=W)
Label(GameBoardframe, text="  ").grid(row=4, column=1, sticky=W)
Label(GameBoardframe, text="//////").grid(row=4, column=2, sticky=W,rowspan=2)
Label(GameBoardframe, text="   ").grid(row=4, column=3, sticky=W)
Label(GameBoardframe, text="/////").grid(row=4, column=4, sticky=W,rowspan=2)
Label(GameBoardframe, text="   ").grid(row=4, column=5, sticky=W)
Label(GameBoardframe, text="Conservatory").grid(row=5, column=1, sticky=W)
Label(GameBoardframe, text="Ballroom").grid(row=5, column=3, sticky=W)
Label(GameBoardframe, text="Kitchen").grid(row=5, column=5, sticky=W)

root.mainloop()
