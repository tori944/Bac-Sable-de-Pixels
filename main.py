from Cellule import *

for i in range (NbRow):             # row
    for j in range (NbColumn):      # column
        Cellule(j*10, i*10, j)

#### frame du bas ####

frame1 = Frame(root, bg="light green")
frame1.grid(sticky=EW, padx=10, pady=10, column=0, row=1)

frame1.columnconfigure([0,1,2,3], weight=1)

btn1 = Button(frame1, text="1",font=("",15))
btn1.grid(column=0, row=0, pady=10)

btn2 = Button(frame1, text="2", font=("",15))
btn2.grid(column=1, row=0, pady=10)

btn3 = Button(frame1, text="3", font=("",15))
btn3.grid(column=2, row=0, pady=10)

btn4 = Button(frame1, text="4", font=("",15))
btn4.grid(column=3, row=0, pady=10)

#### frame du haut ####

frame2 = Frame(root, bg="light blue")
frame2.grid(sticky=NS, padx=10, pady=10, column=1, row=0) # , rowspan=2

frame2.rowconfigure([0,1,2,3], weight=1)

btn5 = Button(frame2, text="5",font=("",15))
btn5.grid(column=0, row=0, padx=10)

btn6 = Button(frame2, text="6", font=("",15))
btn6.grid(column=0, row=1, padx=10)

btn7 = Button(frame2, text="7", font=("",15))
btn7.grid(column=0, row=2, padx=10)

btn8 = Button(frame2, text="8", font=("",15))
btn8.grid(column=0, row=3, padx=10)


root.mainloop()