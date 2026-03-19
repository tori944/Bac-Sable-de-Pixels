from tkinter import *

NbRow = 50
NbColumn = 80

root = Tk()
root.title("Bac à sable")
# root.geometry("850x550") # 

#  800 + 25*2
#  500 + 25*2
# 


# root.columnconfigure((0,1), weight=1)
# root.rowconfigure((0,1), weight=1)

canvas = Canvas(root, width=800, height=500, bg="light yellow", highlightthickness=2, highlightbackground="black", bd=0)
canvas.grid(column=0,row=0, padx=25, pady=25)

