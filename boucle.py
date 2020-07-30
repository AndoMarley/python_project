import tkinter.filedialog
import tkinter.font as tkFont
from functools import partial
from tkinter import*
from tkinter import ttk

#root0
root0=Tk()
cnv0=Canvas(root0,width=1300, height=850)
cnv0.grid()
root0.title('MDallages V-Alpha - Calcul des dallages industriels')
root0.resizable('true','true')

def calculer ():
    dmax=spinbox_dmax.get()
    coef=IntVar()
    if dmax=='20':
        coef.set(7)
    else:
        if dmax=='25':
            coef.set(1)
        else:
            if dmax=='15':
                coef.set(13)
            else:
                if dmax=='10':
                    coef.set(30)
    print(dmax, coef.get())

spinbox_dmax=DoubleVar()
label_dmax= Label(root0, text="Dmax (granulats)=")
choice_dmax=[25,20,15,10]
spinbox_dmax= ttk.Combobox(root0,values=choice_dmax)
spinbox_dmax.current('0')
label_unite_dmax= Label(root0,text="mm  (DTU 13.3 C.3.2.1.1)")
label_dmax.place(x=10,y=10)
spinbox_dmax.place(x=150,y=10)
spinbox_dmax.configure(width=6)
label_unite_dmax.place(x=220,y=10)

button=Button(root0, text='calculer',command=calculer)
button.place(x=30,y=30)


root0.mainloop()