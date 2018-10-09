from tkinter import *
root = Tk()
root.geometry("330x400+50+50")
root.title("Calculator")
heading = Label(root, text="CALCULATE PROFIT MARK-UP & MARGIN", font=('calibri 13 bold'), fg="dark slate gray").pack()
entr_amt1 = Label(root, text="Enter the Cost of Sales:", font=('calibri 14 bold')).place(x=10, y=50)
cost = DoubleVar()
ent_box1 = Entry(root, width=25, textvariable=cost, font=('calibri 12 bold')).place(x=10, y=80)
entr_amt2 = Label(root, text="Enter % to be calculated: ", font=('calibri 14 bold')).place(x=10, y=110)
percent = DoubleVar()
ent_box2 = Entry(root, width=25, textvariable=percent, font=('calibri 12 bold')).place(x=10, y=140)


def mark_up():
    c = cost.get()
    p = percent.get()
    mup = c*p/100
    mark_up = round(mup, 2)
    s_p = c+(c*p/100)
    sell_p = round(s_p, 2)
    lab = Label(root, text=("Profit mark-up: "+str(mark_up)+"            "), font=('calibri 16 bold'), fg="dark slate gray").place(x=50, y=250)
    lab2 = Label(root, text=("Selling price: "+str(sell_p)+"            "), font=('calibri 16 bold'), fg="dark slate gray").place(x=50, y=280)


def margin():
    c = cost.get()
    p = percent.get()
    mn = p/(100-p)*c
    margin = round(mn, 2)
    s_p = 100*c/(100-p)
    sell_p = round(s_p, 2)
    lab = Label(root, text=("Profit margin: "+str(margin)+"           "), font=('calibri 16 bold'), fg="dark slate gray").place(x=50, y=310)
    lab2 = Label(root, text=("Selling price: "+str(sell_p)+"           "), font=('calibri 16 bold'), fg="dark slate gray").place(x=50, y=340)


btn1 = Button(root, text="Mark-up", font=('calibri 12 bold'), width=12, height=2, bg="dark sea green", command=mark_up).place(x=50, y=180)
btn2 = Button(root, text="Margin", font=('calibri 12 bold'), width=12, height=2, bg="dark sea green", command=margin).place(x=170, y=180)
root.mainloop()
