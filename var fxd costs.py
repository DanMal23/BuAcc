from tkinter import *
import time
import datetime

root = Tk()
root.geometry("350x340+50+50")
imgbg = PhotoImage(file="C:/Users/DANUTA/Pictures/buttons/sky1.png")
background_label = Label(root, image=imgbg)
background_label.place(x=0,y=0)
root.title("Variable and Fixed Cost per unit Calculator")

DateofOrder = StringVar()
dateheading = Label(root, text="Today is", font=('calibri 11'), fg="dark slate gray").place(x=6, y=8)
dateheading2 = Label(root, font=('calibri 11'), textvariable=DateofOrder, fg="dark slate gray").place(x=63, y=8)
DateofOrder.set(time.strftime("%A, %B %d, %Y."))
heading = Label(root, text="Enter data:", font=('calibri 13 bold'), fg="dark slate gray").place(x=9, y=37)
# heading = Label(root, text="II level coverage ratio \n or net working capital \n calculation", font=('calibri 15 bold'), fg="blue").place(x=150, y=5)
entr_amt1 = Label(root, text="Volume of prod.:", font=('calibri 11 bold')).place(x=10, y=70)
volume = DoubleVar()
ent_box1 = Entry(root, width=17, textvariable=volume, font=('calibri 11 bold')).place(x=10, y=90)
entr_amt2 = Label(root, text="Direct materials: ", font=('calibri 11 bold')).place(x=10, y=110)
dir_mat = DoubleVar()
ent_box2 = Entry(root, width=17, textvariable=dir_mat, font=('calibri 11 bold')).place(x=10, y=130)
entr_amt3 = Label(root, text="Direct labour:", font=('calibri 11 bold')).place(x=10, y=150)
dir_lab = DoubleVar()
ent_box3 = Entry(root, width=17, textvariable=dir_lab, font=('calibri 11 bold')).place(x=10, y=170)
entr_amt4 = Label(root, text="Dep'n (str. line):", font=('calibri 11 bold')).place(x=10, y=190)
depn = DoubleVar()
ent_box4 = Entry(root, width=17, textvariable=depn, font=('calibri 11 bold')).place(x=10, y=210)
entr_amt5 = Label(root, text="Rent: ", font=('calibri 11 bold')).place(x=10, y=230)
rent = DoubleVar()
ent_box5 = Entry(root, width=17, textvariable=rent, font=('calibri 11 bold')).place(x=10, y=250)
entr_amt6 = Label(root, text="Fixed costs:", font=('calibri 11 bold')).place(x=10, y=270)
fxd = DoubleVar()
ent_box6 = Entry(root, width=17, textvariable=fxd, font=('calibri 11 bold')).place(x=10, y=290)



def tot_fxd_c():
    d = depn.get()
    r = rent.get()
    f = fxd.get()
    tfc = d+r+f
    tot_fc = round(tfc, 2)
    Label(root, text=(str(tot_fc)+'   '), font=('calibri 15 bold'), fg="dark slate gray").place(x=270, y=100)


def fxd_pu():
    d = depn.get()
    r = rent.get()
    f = fxd.get()
    v = volume.get()
    fxed = (d+r+f)/v
    fxd_u = round(fxed, 2)
    Label(root, text=(str(fxd_u)+'   '), font=('calibri 15 bold'), fg="dark slate gray").place(x=270, y=150)


def tot_var_c():
    m = dir_mat.get()
    l = dir_lab.get()
    tv = m+l
    tot_var = round(tv, 2)
    Label(root, text=(str(tot_var)+'   '), font=('calibri 15 bold'), fg="dark slate gray").place(x=270, y=200)


def var_pu():
    m = dir_mat.get()
    l = dir_lab.get()
    v = volume.get()
    vpu = (m+l)/v
    varpu = round(vpu, 2)
    Label(root, text=(str(varpu)+'   '), font=('calibri 15 bold'), fg="dark slate gray").place(x=270, y=250)


def reset():
    volume.set(" ")
    dir_mat.set(" ")
    dir_lab.set(" ")
    depn.set(" ")
    rent.set(" ")
    fxd.set(" ")

# def exit():
    # exit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if exit > 0:
        root.destroy()
        return

btn1 = Button(root, text="Total fxd \n Costs", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=tot_fxd_c).place(x=160, y=90)
btn2 = Button(root, text="Fxd costs \n p.u.", font=('calibri 10 bold'), width=12, height=2, bg="goldenrod", command=fxd_pu).place(x=160, y=140)
btn3 = Button(root, text="Total var. \n Costs", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=tot_var_c).place(x=160, y=190)
btn4 = Button(root, text="Variable \n Cost p.u.", font=('calibri 10 bold'), width=12, height=2, bg="goldenrod", command=var_pu).place(x=160, y=240)
btn5 = Button(root, text="Reset", font=('calibri 10 bold'), width=12, height=2, bg="white", command=reset).place(x=160, y=290)
# btn6 = Button(root, text="Exit", font=('calibri 10 bold'), width=12, height=2, bg="white", command=exit).place(x=160, y=240)

root.mainloop()
