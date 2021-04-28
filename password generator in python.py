import tkinter
import random
from tkinter.messagebox import showinfo
#Defining Tkinter Window
window=tkinter.Tk()
window.title("Password generator")
window.geometry("400x400")
A_Z="QWERTYUIOPASDFGHJKLZXCVBNM"
a_z="qwertyuiopasdfghjklzxcvbnm"
symbol="!@#$%^&*_."
numbers="0123456789"

def clicked():
    inp_str=""
    try:
        str_len=int(inp_1.get())
        inp_str+=a_z
       # print(typeint(inp_1.get())))
        if(CheckVar1.get()):
            inp_str+=A_Z
        if(CheckVar3.get()):
            inp_str+=symbol
        if(CheckVar4.get()):
            inp_str+=numbers

        #print(inp_str)
        res="".join(random.sample(inp_str,str_len))
        lbl_2.configure(state=tkinter.NORMAL)
        lbl_2.insert(0,res)
    except Exception as e:
        #print(e)
        showinfo("Window", "Please Fill details")



#creating frame
top=tkinter.Frame(window,height=100)
top.pack(fill="x")

main=tkinter.Frame(window,height=200)
main.pack(fill="x")

bottom=tkinter.Frame(window,height=200)
bottom.pack(fill="x")


# gui for accepting values from user
head=lbl_1=tkinter.Label(top,text="RANDOM PASSOWRD GENERATOR",height=5,justify=tkinter.CENTER,relief=tkinter.RAISED,bg="red")
lbl_1.pack()

lbl_1=tkinter.Label(main,text="LENGTH OF PASSWORD:",height=5)
lbl_1.pack(side="left")

inp_1=tkinter.Entry(main,width=15)
inp_1.pack(side="left")

CheckVar1 =tkinter.IntVar()
CheckVar2 =tkinter.IntVar(value=1)
CheckVar3 =tkinter.IntVar()
CheckVar4 =tkinter.IntVar()
c1 = tkinter.Checkbutton(bottom, text = "A-Z", variable = CheckVar1,onvalue = 1, offvalue = 0,width = 20)
c2 = tkinter.Checkbutton(bottom, text = "a-z",state=tkinter.DISABLED, variable = CheckVar2, onvalue = 1, offvalue = 0,width = 20)

c3 = tkinter.Checkbutton(bottom, text = "special symbols(!@#$%^&*.)", variable = CheckVar3,onvalue = 1, offvalue = 0,width = 20)
c4 = tkinter.Checkbutton(bottom, text = "NUMBERS", variable = CheckVar4, onvalue = 1, offvalue = 0,width = 20)
c1.pack()
c2.pack()
c3.pack()
c4.pack()

bt1=tkinter.Button(bottom,text="GENERATE PASSWORD",command=clicked)
bt1.pack(pady="10")
lbl_3=tkinter.Label(bottom,text="YOUR PASSOWRD IS",height=5)
lbl_3.pack(side="left",padx="25")
lbl_2=tkinter.Entry(bottom,width=30,state=tkinter.DISABLED)
lbl_2.pack(side="left")
