from tkinter import *
from tkinter import Label, DoubleVar, Entry, Button, Tk
root = Tk()
root.geometry("350x360+50+50")
root.title("Costing")
heading = Label(root, text="*Reconciling marginal and absorption costing* \n Enter data:", font=('calibri 12 bold'), fg="dark green").pack()
entr_amt1 = Label(root, text="Opening inventory (in units):", font=('calibri 11 bold')).place(x=10, y=40)
op_inv = DoubleVar()
ent_box1 = Entry(root, width=25, textvariable=op_inv, font=('calibri 11 bold')).place(x=10, y=60)
entr_amt2 = Label(root, text="Closing inventory (in units): ", font=('calibri 11 bold')).place(x=10, y=80)
cl_inv = DoubleVar()
ent_box2 = Entry(root, width=25, textvariable=cl_inv, font=('calibri 11 bold')).place(x=10, y=100)
entr_amt3 = Label(root, text="Absorption costing Profit:", font=('calibri 11 bold')).place(x=10, y=120)
ab_c_prof = DoubleVar()
ent_box3 = Entry(root, width=25, textvariable=ab_c_prof, font=('calibri 11 bold')).place(x=10, y=140)
entr_amt4 = Label(root, text="OAR for fixed production costs/overhds: ", font=('calibri 11 bold')).place(x=10, y=160)
oar = DoubleVar()
ent_box4 = Entry(root, width=25, textvariable=oar, font=('calibri 11 bold')).place(x=10, y=180)
heading2 = Label(root, text=" Absorption costing Profit + change in Inv. * OAR \n = Marginal costing Profit", font=('calibri 11 bold'), fg="gray60").place(x=10, y=320)


def inv_change():
    oi = op_inv.get()
    ci = cl_inv.get()
    o = oar.get()
    ch = (oi-ci)*o
    chg = round(ch, 2)
    Label(root, text=("Change in Inventory * OAR: "+str(chg)), font=('calibri 12 bold'), fg="gray26").place(x=40, y=270)


def mgn_c_prof():
    ab = ab_c_prof.get()
    oi = op_inv.get()
    ci = cl_inv.get()
    o = oar.get()
    mgn = ab+((oi-ci)*o)
    mgn_p = round(mgn, 2)
    Label(root, text=("Marginal costing Profit: "+str(mgn_p)), font=('calibri 12 bold'), fg="gray26").place(x=40, y=290)


btn1 = Button(root, text="Change in \n Inventory * oar", font=('calibri 10 bold'), width=14, height=2, bg="DarkSeaGreen1", command=inv_change).place(x=20, y=220)
btn2 = Button(root, text="Marginal costing \n Profit", font=('calibri 10 bold'), width=14, height=2, bg="DarkSeaGreen1", command=mgn_c_prof).place(x=140, y=220)
root.mainloop()
