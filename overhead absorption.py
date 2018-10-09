from tkinter import *
root = Tk()
root.geometry("400x380+50+50")
root.title("OAR")
heading = Label(root, text="CALCULATE OVERHEAD ABSORPTION", font=('arial 12 bold'), fg="dark slate gray").pack()
entr_amt1 = Label(root, text="Budgeted cost centre Overhead:", font=('arial 11 bold')).place(x=10, y=40)
budg_ov = DoubleVar()
ent_box1 = Entry(root, width=40, textvariable=budg_ov, font=('arial 11 bold')).place(x=10, y=60)
entr_amt2 = Label(root, text="Actual cost centre Overhead: ", font=('arial 11 bold')).place(x=10, y=80)
act_ov = DoubleVar()
ent_box2 = Entry(root, width=40, textvariable=act_ov, font=('arial 11 bold')).place(x=10, y=100)
entr_amt3 = Label(root, text="Budgeted machine/labour hours:", font=('arial 11 bold')).place(x=10, y=120)
budg_hrs = DoubleVar()
ent_box3 = Entry(root, width=40, textvariable=budg_hrs, font=('arial 11 bold')).place(x=10, y=140)
entr_amt4 = Label(root, text="Actual machine/labour hours: ", font=('arial 11 bold')).place(x=10, y=160)
act_hrs = DoubleVar()
ent_box4 = Entry(root, width=40, textvariable=act_hrs, font=('arial 11 bold')).place(x=10, y=180)


def absorbed():
    bo = budg_ov.get()
    bhr = budg_hrs.get()
    ov_ab = bo/bhr
    over_abs = round(ov_ab, 2)
    lab1 = Label(root, text=("Overhead absorbed: "+str(over_abs)), font=('arial 12 bold'), fg="dark slate gray").place(x=50, y=280)


def actual_incurred():
    bo = budg_ov.get()
    bhr = budg_hrs.get()
    ahr = act_hrs.get()
    a_i = bo/bhr*ahr
    act_incur = round(a_i, 2)
    lab2 = Label(root, text=("Actual overhead incurred: "+str(act_incur)), font=('arial 12 bold'), fg="dark slate gray").place(x=50, y=300)


def und_over_abs():
    bo = budg_ov.get()
    bhr = budg_hrs.get()
    ahr = act_hrs.get()
    ao = act_ov.get()
    und_over = (bo/bhr*ahr)-ao
    und_over_abs = round(und_over, 2)
    lab3 = Label(root, text=("Overhead under/over absorbed: "+str(und_over_abs)), font=('arial 12 bold'), fg="dark slate gray").place(x=50, y=320)


btn1 = Button(root, text="Overhead \n absorbed", font=('tahoma 9 bold'), width=14, height=2, bg="DarkSeaGreen1", command=absorbed).place(x=10, y=220)
btn2 = Button(root, text="Actual incurred", font=('tahoma 9 bold'), width=14, height=2, bg="DarkSeaGreen1", command=actual_incurred).place(x=140, y=220)
btn3 = Button(root, text="Under/over \n absorbed", font=('tahoma 9 bold'), width=14, height=2, bg="DarkSeaGreen1", command=und_over_abs).place(x=270, y=220)
root.mainloop()
