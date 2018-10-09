from tkinter import *
from tkinter import Label, DoubleVar, Entry, Button
root = Tk()
root.geometry("400x440+50+50")
root.title("Pricing")
heading = Label(root, text="Return on Investment,   Enter data:", font=('calibri 14 bold'), fg="wheat4").pack()
entr_amt1 = Label(root, text="Volume of production:", font=('calibri 11 bold')).place(x=10, y=40)
volume = DoubleVar()
ent_box1 = Entry(root, width=20, textvariable=volume, font=('calibri 11 bold')).place(x=10, y=60)
entr_amt2 = Label(root, text="Capital invested: ", font=('calibri 11 bold')).place(x=10, y=80)
capital = DoubleVar()
ent_box2 = Entry(root, width=20, textvariable=capital, font=('calibri 11 bold')).place(x=10, y=100)
entr_amt3 = Label(root, text="Expected % ROI:", font=('calibri 11 bold')).place(x=10, y=120)
percent = DoubleVar()
ent_box3 = Entry(root, width=20, textvariable=percent, font=('calibri 11 bold')).place(x=10, y=140)
entr_amt4 = Label(root, text="Fixed oar p.hr: ", font=('calibri 11 bold')).place(x=10, y=160)
fxd_oar = DoubleVar()
ent_box4 = Entry(root, width=20, textvariable=fxd_oar, font=('calibri 11 bold')).place(x=10, y=180)
entr_amt5 = Label(root, text="Direct mat. pu", font=('calibri 11 bold')).place(x=10, y=200)
dir_mat = DoubleVar()
ent_box5 = Entry(root, width=20, textvariable=dir_mat, font=('calibri 11 bold')).place(x=10, y=220)
entr_amt6 = Label(root, text="Direct labour pu: ", font=('calibri 11 bold')).place(x=10, y=240)
dir_lab = DoubleVar()
ent_box6 = Entry(root, width=20, textvariable=dir_lab, font=('calibri 11 bold')).place(x=10, y=260)
entr_amt7 = Label(root, text="Variable overhd pu: ", font=('calibri 11 bold')).place(x=10, y=280)
var_ovh = DoubleVar()
ent_box7 = Entry(root, width=20, textvariable=var_ovh, font=('calibri 11 bold')).place(x=10, y=300)
entr_amt8 = Label(root, text="Machine hrs pu: ", font=('calibri 11 bold')).place(x=10, y=320)
mach_hrs = DoubleVar()
ent_box8 = Entry(root, width=20, textvariable=mach_hrs, font=('calibri 11 bold')).place(x=10, y=340)


def ret_on_inv():
    c = capital.get()
    p = percent.get()
    ret = c*p/100
    ret_in = round(ret, 2)
    Label(root, text=("Return on investment: "+str(ret_in)), font=('calibri 12 bold'), fg="wheat4").place(x=180, y=90)


def variable_cost():
    dm = dir_mat.get()
    dl = dir_lab.get()
    v = var_ovh.get()
    var = dm+dl+v
    var_cost_pu = round(var, 2)
    Label(root, text=("Marginal cost pu: "+str(var_cost_pu)), font=('calibri 12 bold'), fg="wheat4").place(x=180, y=170)


def full_cost():
    dm = dir_mat.get()
    dl = dir_lab.get()
    v = var_ovh.get()
    oar = fxd_oar.get()
    m = mach_hrs.get()
    cost = (dm+dl+v)+m*oar
    fcost = round(cost, 2)
    Label(root, text=("Full cost of prod. pu: "+str(fcost)), font=('calibri 12 bold'), fg="wheat4").place(x=180, y=250)


def mark_up():
    dm = dir_mat.get()
    dl = dir_lab.get()
    v = var_ovh.get()
    oar = fxd_oar.get()
    m = mach_hrs.get()
    p = percent.get()
    mp = ((dm+dl+v)+m*oar)*p/100
    mup = round(mp, 2)
    Label(root, text=("Profit Mark-up: "+str(mup)), font=('calibri 12 bold'), fg="wheat4").place(x=180, y=330)


def s_price():
    dm = dir_mat.get()
    dl = dir_lab.get()
    v = var_ovh.get()
    oar = fxd_oar.get()
    m = mach_hrs.get()
    p = percent.get()
    s_pr = ((dm+dl+v)+m*oar)+((dm+dl+v)+m*oar)*p/100
    sell_pr = round(s_pr, 2)
    Label(root, text=("Selling price: "+str(sell_pr)), font=('calibri 12 bold'), fg="wheat4").place(x=180, y=410)


btn1 = Button(root, text="ROI", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=ret_on_inv).place(x=200, y=40)
btn2 = Button(root, text="Variable cost \n pu", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=variable_cost).place(x=200, y=120)
btn3 = Button(root, text="Full cost \n pu", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=full_cost).place(x=200, y=200)
btn4 = Button(root, text="Mark-up", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=mark_up).place(x=200, y=280)
btn5 = Button(root, text="Selling price", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=s_price).place(x=200, y=360)

root.mainloop()
