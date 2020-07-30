from tkinter import*
from tkinter import ttk


#self.root0


class Application:
    def __init__(self):
        ##fenêtre principale
        self.root0=Tk()
        self.cnv0=Canvas(self.root0,width=1300, height=850)
        self.cnv0.grid()
        self.root0.title('MDallages V-Alpha - Calcul des dallages industriels')
        self.root0.resizable('true','true')
        

    def ouvrir(self):
        self.fen=Toplevel(self.root0,width=400,height=200)
        self.fen.wm_resizable('false')
        self.fen.mainloop()

    def interfaces(self):
        ##titres lignes
        #self.charges
        self.charges=Label(self.root0,text='Qi',bd=1,relief=SOLID)
        self.charges.place(x=10,y=10)
        self.charges.configure(width=10)
        #xi
        self.position_xi=Label(self.root0,text='xi',bd=1,relief=SOLID)
        self.position_xi.place(x=83,y=10)
        self.position_xi.configure(width=10)
        #yi
        self.position_yi=Label(self.root0,text='yi',bd=1,relief=SOLID)
        self.position_yi.place(x=156,y=10)
        self.position_yi.configure(width=10)
        #cas de self.charges
        self.cas_de_charges=Label(self.root0,text='Cas de charges',bd=1,relief=SOLID)
        self.cas_de_charges.place(x=229,y=10)
        self.cas_de_charges.configure(width=20)
        #durée
        self.duree=Label(self.root0,text='Durée',bd=1,relief=SOLID)
        self.duree.place(x=372,y=10)
        self.duree.configure(width=20)

        #colonnes Q1
        #Q1
        self.charges_Q1=Label(self.root0,text='Q1',bd=1,relief=SOLID)
        self.charges_Q1.place(x=10,y=28)
        self.charges_Q1.configure(width=10,height=1)
        #x1
        self.position_x1=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_x1.place(x=83,y=28)
        self.position_x1.configure(width=12)
        #y1
        self.position_y1=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_y1.place(x=156,y=28)
        self.position_y1.configure(width=12)
        #cas de self.charges
        self.choice_cas_de_charges=['permanente','exploitation']
        self.cas_de_charges_Q1=ttk.Combobox(self.root0,values=self.choice_cas_de_charges)
        self.cas_de_charges_Q1.current('0')
        self.cas_de_charges_Q1.place(x=229,y=28)
        self.cas_de_charges_Q1.configure(width=20)
        self.cas_de_charges_Q1.configure(height=1)
        #durée
        self.choice_duree=['courte','longue']
        self.duree_Q1=ttk.Combobox(self.root0,values=self.choice_duree)
        self.duree_Q1.current('1')
        self.duree_Q1.place(x=372,y=28)
        self.duree_Q1.configure(width=20)
        self.duree_Q1.configure(height=1)

        #colonnes Q2
        #Q2
        self.charges_Q2=Label(self.root0,text='Q2',bd=1,relief=SOLID)
        self.charges_Q2.place(x=10,y=46)
        self.charges_Q2.configure(width=10,height=1)
        #x2
        self.position_x2=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_x2.place(x=83,y=46)
        self.position_x2.configure(width=12)
        #y2
        self.position_y2=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_y2.place(x=156,y=46)
        self.position_y2.configure(width=12)
        #cas de self.charges
        self.choice_cas_de_charges=['permanente','exploitation']
        self.cas_de_charges_Q2=ttk.Combobox(self.root0,values=self.choice_cas_de_charges)
        self.cas_de_charges_Q2.current('0')
        self.cas_de_charges_Q2.place(x=229,y=47)
        self.cas_de_charges_Q2.configure(width=20)
        self.cas_de_charges_Q2.configure(height=1)
        #durée
        self.choice_duree=['courte','longue']
        self.duree_Q2=ttk.Combobox(self.root0,values=self.choice_duree)
        self.duree_Q2.current('1')
        self.duree_Q2.place(x=372,y=46)
        self.duree_Q2.configure(width=20)
        self.duree_Q2.configure(height=1)

        #colonnes Q3
        #Q3
        self.charges_Q3=Label(self.root0,text='Q3',bd=1,relief=SOLID)
        self.charges_Q3.place(x=10,y=64)
        self.charges_Q3.configure(width=10,height=1)
        #x3
        self.position_x3=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_x3.place(x=83,y=64)
        self.position_x3.configure(width=12)
        #y3
        self.position_y3=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_y3.place(x=156,y=64)
        self.position_y3.configure(width=12)
        #cas de self.charges
        self.choice_cas_de_charges=['permanente','exploitation']
        self.cas_de_charges_Q3=ttk.Combobox(self.root0,values=self.choice_cas_de_charges)
        self.cas_de_charges_Q3.current('0')
        self.cas_de_charges_Q3.place(x=229,y=64)
        self.cas_de_charges_Q3.configure(width=20)
        self.cas_de_charges_Q3.configure(height=1)
        #durée
        self.choice_duree=['courte','longue']
        self.duree_Q3=ttk.Combobox(self.root0,values=self.choice_duree)
        self.duree_Q3.current('1')
        self.duree_Q3.place(x=372,y=64)
        self.duree_Q3.configure(width=20)
        self.duree_Q3.configure(height=1)

        #colonnes Q4
        #Q4
        self.charges_Q4=Label(self.root0,text='Q4',bd=1,relief=SOLID)
        self.charges_Q4.place(x=10,y=82)
        self.charges_Q4.configure(width=10,height=1)
        #x4
        self.position_x4=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_x4.place(x=83,y=82)
        self.position_x4.configure(width=12)
        #y4
        self.position_y4=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_y4.place(x=156,y=82)
        self.position_y4.configure(width=12)
        #cas de self.charges
        self.choice_cas_de_charges=['permanente','exploitation']
        self.cas_de_charges_Q4=ttk.Combobox(self.root0,values=self.choice_cas_de_charges)
        self.cas_de_charges_Q4.current('0')
        self.cas_de_charges_Q4.place(x=229,y=82)
        self.cas_de_charges_Q4.configure(width=20)
        self.cas_de_charges_Q4.configure(height=1)
        #durée
        self.choice_duree=['courte','longue']
        self.duree_Q4=ttk.Combobox(self.root0,values=self.choice_duree)
        self.duree_Q4.current('1')
        self.duree_Q4.place(x=372,y=82)
        self.duree_Q4.configure(width=20)
        self.duree_Q4.configure(height=1)

        #colonnes Q5
        #Q5
        self.charges_Q5=Label(self.root0,text='Q5',bd=1,relief=SOLID)
        self.charges_Q5.place(x=10,y=100)
        self.charges_Q5.configure(width=10,height=1)
        #x5
        self.position_x5=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_x5.place(x=83,y=100)
        self.position_x5.configure(width=12)
        #y5
        self.position_y5=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_y5.place(x=156,y=100)
        self.position_y5.configure(width=12)
        #cas de self.charges
        self.choice_cas_de_charges=['permanente','exploitation']
        self.cas_de_charges_Q5=ttk.Combobox(self.root0,values=self.choice_cas_de_charges)
        self.cas_de_charges_Q5.current('0')
        self.cas_de_charges_Q5.place(x=229,y=100)
        self.cas_de_charges_Q5.configure(width=20)
        self.cas_de_charges_Q5.configure(height=1)
        #durée
        self.choice_duree=['courte','longue']
        self.duree_Q5=ttk.Combobox(self.root0,values=self.choice_duree)
        self.duree_Q5.current('1')
        self.duree_Q5.place(x=372,y=100)
        self.duree_Q5.configure(width=20)
        self.duree_Q5.configure(height=1)


        #colonnes Q6
        #Q6
        self.charges_Q6=Label(self.root0,text='Q6',bd=1,relief=SOLID)
        self.charges_Q6.place(x=10,y=118)
        self.charges_Q6.configure(width=10,height=1)
        #x5
        self.position_x6=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_x6.place(x=83,y=118)
        self.position_x6.configure(width=12)
        #y5
        self.position_y6=Entry(self.root0,bd=1,relief=SOLID,fg='grey')
        self.position_y6.place(x=156,y=118)
        self.position_y6.configure(width=12)
        #cas de self.charges
        self.choice_cas_de_charges=['permanente','exploitation']
        self.cas_de_charges_Q6=ttk.Combobox(self.root0,values=self.choice_cas_de_charges)
        self.cas_de_charges_Q6.current('0')
        self.cas_de_charges_Q6.place(x=229,y=118)
        self.cas_de_charges_Q6.configure(width=20)
        self.cas_de_charges_Q6.configure(height=1)
        #durée
        self.choice_duree=['courte','longue']
        self.duree_Q6=ttk.Combobox(self.root0,values=self.choice_duree)
        self.duree_Q6.current('1')
        self.duree_Q6.place(x=372,y=118)
        self.duree_Q6.configure(width=20)
        self.duree_Q6.configure(height=1)


    def button(self):  
        self.button_Q=Button(self.root0,text='charges concentrées',command=self.ouvrir)
        self.button_Q.place(x=600,y=20)

        self.root0.mainloop()

