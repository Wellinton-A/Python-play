from tkinter import *

cachorro = Tk()
cachorro.configure()
cachorro.geometry('1440x720')
cachorro.title('Minesweeper')
cachorro.resizable(False, False)

top_frame = Frame(
    cachorro,
    bg='red',
    width=1440,
    height=180
)

top_frame.place(x=0, y=0)
midle_frame = Frame(
    cachorro,
    bg='black',
    width=1440,
    height=180
)

midle_frame.place(x=0, y=360)


cachorro.mainloop()
