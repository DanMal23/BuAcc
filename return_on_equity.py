from tkinter import *
import time
import datetime

root = Tk()
root.geometry("360x400+50+50")
root.title("ROE")

heading = Label(root, text="Return on Equity,   Enter data:", font=('calibri 14 bold'), fg="wheat4").pack()
entr_amt1 = Label(root, text="Net income p.u.:", font=('calibri 11 bold')).place(x=10, y=40)
income = DoubleVar()
ent_box1 = Entry(root, width=20, textvariable=income, font=('calibri 11 bold')).place(x=10, y=60)
entr_amt2 = Label(root, text="Sales price: ", font=('calibri 11 bold')).place(x=10, y=80)
price = DoubleVar()
ent_box2 = Entry(root, width=20, textvariable=price, font=('calibri 11 bold')).place(x=10, y=100)
entr_amt3 = Label(root, text="Equity multiplier:", font=('calibri 11 bold')).place(x=10, y=120)
eq_multi = DoubleVar()
ent_box3 = Entry(root, width=20, textvariable=eq_multi, font=('calibri 11 bold')).place(x=10, y=140)
entr_amt4 = Label(root, text="Assets turnover: ", font=('calibri 11 bold')).place(x=10, y=160)
assets_turn = DoubleVar()
ent_box4 = Entry(root, width=20, textvariable=assets_turn, font=('calibri 11 bold')).place(x=10, y=180)
DateofOrder = StringVar()
dateheading = Label(root, text="Today is: ", font=('calibri 12 bold'), fg="black").place(x=10, y=240)
dateheading2 = Label(root, font=('calibri 12 bold'), textvariable=DateofOrder, fg="black").place(x=10, y=260)
DateofOrder.set(time.strftime("%d/%m/%Y"))


def tot_ass():
    s = price.get()
    at = assets_turn.get()
    tot = s/at
    tota = round(tot, 2)
    Label(root, text=("Total assets: "+str(tota)), font=('calibri 12 bold'), fg="wheat4").place(x=180, y=90)


def shs_equity():
    s = price.get()
    at = assets_turn.get()
    em = eq_multi.get()
    she = (s/at)/em
    sheq = round(she, 2)
    Label(root, text=("Owner's equity: "+str(sheq)), font=('calibri 12 bold'), fg="wheat4").place(x=180, y=170)


def roe():
    s = price.get()
    at = assets_turn.get()
    em = eq_multi.get()
    i = income.get()
    ret = int((i/(s/at/em))*100)
    Label(root, text=("ROE: "+str(ret)+'%'), font=('calibri 12 bold'), fg="wheat4").place(x=200, y=250)


def exit():
    exit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if exit > 0:
        root.destroy()
        return


def reset():
    income.set("0.0")
    price.set("0.0")
    eq_multi.set("0.0")
    assets_turn.set("0.0")


btn1 = Button(root, text="Total Assets", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=tot_ass).place(x=200, y=40)
btn2 = Button(root, text="Shareholder's \n equity", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=shs_equity).place(x=200, y=120)
btn3 = Button(root, text="ROE", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=roe).place(x=200, y=200)
btn4 = Button(root, text="Reset", font=('calibri 10 bold'), width=12, height=2, bg="white", command=reset).place(x=80, y=300)
btn5 = Button(root, text="Exit", font=('calibri 10 bold'), width=12, height=2, bg="white", command=exit).place(x=200, y=300)

root.mainloop()
