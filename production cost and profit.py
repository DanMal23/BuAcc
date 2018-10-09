from tkinter import *
from tkinter import Label, DoubleVar, Entry, Button
root = Tk()
root.geometry("370x480+50+50")
root.title("Production Cost n Profit")
heading = Label(root, text="*CALCULATOR*   Enter data:", font=('calibri 12 bold'), fg="dark slate gray").pack()
entr_amt1 = Label(root, text="Volume of Production in units:", font=('calibri 11 bold')).place(x=10, y=40)
volume = DoubleVar()
ent_box1 = Entry(root, width=40, textvariable=volume, font=('calibri 11 bold')).place(x=10, y=60)
entr_amt2 = Label(root, text="Direct <prime> cost: ", font=('calibri 11 bold')).place(x=10, y=80)
dir_cost = DoubleVar()
ent_box2 = Entry(root, width=40, textvariable=dir_cost, font=('calibri 11 bold')).place(x=10, y=100)
entr_amt3 = Label(root, text="Selling price:", font=('calibri 11 bold')).place(x=10, y=120)
price = DoubleVar()
ent_box3 = Entry(root, width=40, textvariable=price, font=('calibri 11 bold')).place(x=10, y=140)
entr_amt4 = Label(root, text="OAR: ", font=('calibri 11 bold')).place(x=10, y=160)
oar = DoubleVar()
ent_box4 = Entry(root, width=40, textvariable=oar, font=('calibri 11 bold')).place(x=10, y=180)
entr_amt5 = Label(root, text="Fixed production overheads: ", font=('calibri 11 bold')).place(x=10, y=200)
fixed_ov = DoubleVar()
ent_box5 = Entry(root, width=40, textvariable=fixed_ov, font=('calibri 11 bold')).place(x=10, y=220)


def total_cost():
    dc = dir_cost.get()
    o = oar.get()
    v = volume.get()
    tc = (dc+o)*v
    t_cost = round(tc, 2)
    Label(root, text=("Total Cost: "+str(t_cost)), font=('calibri 12 bold'), fg="azure4").place(x=40, y=350)


def total_unit_cost():
    dc = dir_cost.get()
    o = oar.get()
    tc_pu = dc+o
    t_cost_pu = round(tc_pu, 2)
    Label(root, text=("Total unit cost: "+str(t_cost_pu)), font=('calibri 12 bold'), fg="azure4").place(x=40, y=370)


def total_profit():
    dc = dir_cost.get()
    o = oar.get()
    v = volume.get()
    p = price.get()
    tp = (p-(dc+o))*v
    tot_prof = round(tp, 2)
    Label(root, text=("Total Profit: "+str(tot_prof)), font=('calibri 12 bold'), fg="azure4").place(x=40, y=390)


def profit_pu():
    dc = dir_cost.get()
    o = oar.get()
    p = price.get()
    p_pu = p-(dc+o)
    prof_pu = round(p_pu, 2)
    Label(root, text=("Profit p.u.: "+str(prof_pu)), font=('calibri 12 bold'), fg="azure4").place(x=40, y=410)


def ov_ab_rate():
    v = volume.get()
    fo = fixed_ov.get()
    o = fo/v
    oarate = round(o, 2)
    Label(root, text=("OAR: "+str(oarate)), font=('calibri 12 bold'), fg="azure4").place(x=40, y=430)


btn1 = Button(root, text="Total Cost", font=('calibri 10 bold'), width=14, height=2, bg="goldenrod2", command=total_cost).place(x=10, y=250)
btn2 = Button(root, text="Total \n Unit Cost", font=('calibri 10 bold'), width=14, height=2, bg="goldenrod2", command=total_unit_cost).place(x=130, y=250)
btn3 = Button(root, text="Total Profit", font=('calibri 10 bold'), width=14, height=2, bg="goldenrod2", command=total_profit).place(x=250, y=250)
btn4 = Button(root, text="Profit p.u.", font=('calibri 10 bold'), width=14, height=2, bg="goldenrod2", command=profit_pu).place(x=60, y=300)
btn5 = Button(root, text="OAR", font=('calibri 10 bold'), width=14, height=2, bg="goldenrod2", command=ov_ab_rate).place(x=180, y=300)
root.mainloop()
