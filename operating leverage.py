from tkinter import *
import time
import datetime

root = Tk()
root.geometry("350x260+50+50")
imgbg = PhotoImage(file="C:/Users/DANUTA/Pictures/buttons/skyg.png")
background_label = Label(root, image=imgbg)
background_label.place(x=0,y=0)
root.title("$ Sales for BE")

DateofOrder = StringVar()
dateheading = Label(root, text="Today is", font=('calibri 11'), fg="dark slate gray").place(x=6, y=8)
dateheading2 = Label(root, font=('calibri 11'), textvariable=DateofOrder, fg="dark slate gray").place(x=63, y=8)
DateofOrder.set(time.strftime("%A, %B %d, %Y."))
heading = Label(root, text="Enter data:", font=('calibri 13 bold'), fg="black").place(x=9, y=37)
# heading = Label(root, text="", font=('calibri 15 bold'), fg="blue").place(x=150, y=5)
entr_amt1 = Label(root, text="Sales Price pu:", font=('calibri 11 bold')).place(x=10, y=70)
price = DoubleVar()
ent_box1 = Entry(root, width=17, textvariable=price, font=('calibri 11 bold')).place(x=10, y=90)
entr_amt2 = Label(root, text="Variable cost pu: ", font=('calibri 11 bold')).place(x=10, y=110)
var_c = DoubleVar()
ent_box2 = Entry(root, width=17, textvariable=var_c, font=('calibri 11 bold')).place(x=10, y=130)
entr_amt3 = Label(root, text="Prod. volume:", font=('calibri 11 bold')).place(x=10, y=150)
volume = IntVar()
ent_box3 = Entry(root, width=17, textvariable=volume, font=('calibri 11 bold')).place(x=10, y=170)
entr_amt4 = Label(root, text="Fxd costs p.month:", font=('calibri 11 bold')).place(x=10, y=190)
fxd_c = DoubleVar()
ent_box4 = Entry(root, width=17, textvariable=fxd_c, font=('calibri 11 bold')).place(x=10, y=210)


def fxd_pu():
    f = fxd_c.get()
    i = volume.get()
    pu = f/i
    fpu = round(pu, 2)
    Label(root, text=(str(fpu)+'   '), font=('calibri 14 bold'), fg="dark slate gray").place(x=260, y=80)


def oper_lev():
    p = price.get()
    v = var_c.get()
    f = fxd_c.get()
    i = volume.get()
    pu = f/i
    ol = (p-v)/(p-v-pu)
    oplev = round(ol, 2)
    Label(root, text=(str(oplev)+' '), font=('calibri 14 bold'), fg="dark slate gray").place(x=260, y=130)


def reset():
    price.set(" ")
    var_c.set(" ")
    volume.set(" ")
    fxd_c.set(" ")


# def exit():
    # exit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if exit > 0:
        root.destroy()
        return


btn1 = Button(root, text="Fixed \n cost pu", font=('calibri 10 bold'), width=12, height=2, bg="CadetBlue3", command=fxd_pu).place(x=160, y=70)
btn2 = Button(root, text="Operating \n Leverage", font=('calibri 10 bold'), width=12, height=2, bg="burlywood3", command=oper_lev).place(x=160, y=120)
btn3 = Button(root, text="Reset", font=('calibri 10 bold'), width=12, height=2, bg="white", command=reset).place(x=160, y=170)
# btn6 = Button(root, text="Exit", font=('calibri 10 bold'), width=12, height=2, bg="white", command=exit).place(x=160, y=240)

root.mainloop()
