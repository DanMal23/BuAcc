from tkinter import *
import time
import datetime

root = Tk()
root.geometry("360x300+50+50")
root.title("ROE")

DateofOrder = StringVar()
dateheading = Label(root, text="Today is", font=('calibri 10'), fg="dark slate gray").place(x=6, y=10)
dateheading2 = Label(root, font=('calibri 11'), textvariable=DateofOrder, fg="dark slate gray").place(x=65, y=10)
DateofOrder.set(time.strftime("%d/%m/%Y"))
heading = Label(root, text="Enter data:", font=('calibri 13 bold'), fg="dark slate gray").place(x=10, y=35)
heading = Label(root, text="II level coverage ratio \n or net working capital \n calculation", font=('calibri 15 bold'), fg="blue").place(x=150, y=5)
entr_amt1 = Label(root, text="Non-Current Assets:", font=('calibri 11 bold')).place(x=10, y=70)
NCA = DoubleVar()
ent_box1 = Entry(root, width=17, textvariable=NCA, font=('calibri 11 bold')).place(x=10, y=90)
entr_amt2 = Label(root, text="Coverage Ratio: ", font=('calibri 11 bold')).place(x=10, y=110)
c_ratio = DoubleVar()
ent_box2 = Entry(root, width=17, textvariable=c_ratio, font=('calibri 11 bold')).place(x=10, y=130)
entr_amt3 = Label(root, text="Net Working Capital:", font=('calibri 11 bold')).place(x=10, y=150)
NWC = DoubleVar()
ent_box3 = Entry(root, width=17, textvariable=NWC, font=('calibri 11 bold')).place(x=10, y=170)



def nw_capital():
    na = NCA.get()
    r = c_ratio.get()
    cap = (na*r)-na
    capital = round(cap, 2)
    Label(root, text=(str(capital)+'   '), font=('calibri 15 bold'), fg="dark slate gray").place(x=270, y=100)


def ratio():
    na = NCA.get()
    c = NWC.get()
    r = (na+c)/na
    rat = round(r, 2)
    Label(root, text=(str(rat)+'   '), font=('calibri 15 bold'), fg="dark slate gray").place(x=270, y=150)



def exit():
    exit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if exit > 0:
        root.destroy()
        return


def reset():
    NCA.set(" ")
    c_ratio.set(" ")
    NWC.set(" ")


btn1 = Button(root, text="Net Working \n Capital", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=nw_capital).place(x=160, y=90)
btn2 = Button(root, text="II level \n coverage Ratio", font=('calibri 10 bold'), width=12, height=2, bg="ivory3", command=ratio).place(x=160, y=140)
btn3 = Button(root, text="Reset", font=('calibri 10 bold'), width=12, height=2, bg="white", command=reset).place(x=160, y=190)
btn4 = Button(root, text="Exit", font=('calibri 10 bold'), width=12, height=2, bg="white", command=exit).place(x=160, y=240)

root.mainloop()
