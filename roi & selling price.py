from tkinter import *
from tkinter import Label, DoubleVar, Entry, Button
root = Tk()
root.geometry("400x240+50+50")
root.title("roi")
heading = Label(root, text="Return on Investment and Mark-up,   Enter data:", font=('calibri 13 bold'), fg="wheat4").pack()
entr_amt1 = Label(root, text="Full cost of a product pu:", font=('calibri 11 bold')).place(x=10, y=40)
cost_pu = DoubleVar()
ent_box1 = Entry(root, width=20, textvariable=cost_pu, font=('calibri 11 bold')).place(x=10, y=60)
entr_amt2 = Label(root, text="Total cost incurred: ", font=('calibri 11 bold')).place(x=10, y=80)
tcost = DoubleVar()
ent_box2 = Entry(root, width=20, textvariable=tcost, font=('calibri 11 bold')).place(x=10, y=100)
entr_amt3 = Label(root, text="Capital invested:", font=('calibri 11 bold')).place(x=10, y=120)
capital = DoubleVar()
ent_box3 = Entry(root, width=20, textvariable=capital, font=('calibri 11 bold')).place(x=10, y=140)
entr_amt4 = Label(root, text="Expected % ROI: ", font=('calibri 11 bold')).place(x=10, y=160)
perc_roi = DoubleVar()
ent_box4 = Entry(root, width=20, textvariable=perc_roi, font=('calibri 11 bold')).place(x=10, y=180)


def ret_roi():
    c = capital.get()
    p = perc_roi.get()
    ret = c*p/100
    ret_in = round(ret, 2)
    Label(root, text=("Required annual roi: "+str(ret_in)), font=('calibri 12 bold'), fg="gray26").place(x=180, y=80)


def roi_perc_cost():
    c = capital.get()
    p = perc_roi.get()
    t = tcost.get()
    rp = (c*p/100)/t
    roi_p = round(rp, 2)
    Label(root, text=("Roi as a % of total cost: "+str(roi_p)), font=('calibri 12 bold'), fg="gray26").place(x=180, y=100)


def mark_up():
    fc = cost_pu.get()
    c = capital.get()
    p = perc_roi.get()
    t = tcost.get()
    mp = ((c*p/100)/t)*fc
    mup = round(mp, 2)
    Label(root, text=("Profit Mark-up: "+str(mup)), font=('calibri 12 bold'), fg="gray26").place(x=180, y=180)


def s_price():
    fc = cost_pu.get()
    c = capital.get()
    p = perc_roi.get()
    t = tcost.get()
    s_pr = ((c*p/100)/t)*fc+fc
    sell_pr = round(s_pr, 2)
    Label(root, text=("Selling price: "+str(sell_pr)), font=('calibri 12 bold'), fg="gray26").place(x=180, y=200)


btn1 = Button(root, text="Expected ROI", font=('calibri 10 bold'), width=12, height=2, bg="sienna1", command=ret_roi).place(x=180, y=40)
btn2 = Button(root, text="ROI as a % \n of Total Cost", font=('calibri 10 bold'), width=12, height=2, bg="sienna1", command=roi_perc_cost).place(x=290, y=40)
btn3 = Button(root, text="Mark-up", font=('calibri 10 bold'), width=12, height=2, bg="sienna1", command=mark_up).place(x=180, y=140)
btn4 = Button(root, text="Selling price", font=('calibri 10 bold'), width=12, height=2, bg="sienna1", command=s_price).place(x=290, y=140)


root.mainloop()
