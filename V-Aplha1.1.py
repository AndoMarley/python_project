import tkinter.filedialog
import tkinter.font as tkFont
from functools import partial
from tkinter import *
from tkinter import ttk

#root0
root0=Tk()
cnv0=Canvas(root0,width=1150, height=650)
cnv0.grid()
root0.title('MDallages V-Alpha - Calcul des dallages industriels')
root0.resizable('false','false')

italique1=tkFont.Font(slant='italic',size=8)

def ouvrir():
    open=tkinter.filedialog.askopenfilename(title="Ouvrir un fichier",filetypes=[('CSV files','.csv')])
    print (open)
def enregistrer_sous():
    save=tkinter.filedialog.asksaveasfile(title="Enregistrer sous",filetypes=[('CSV files','.csv')])
    print(save)
def quitter():
    quit()

entry_fck=DoubleVar()
entry_Es1=IntVar()
entry_H=DoubleVar()
entry_Ecm=DoubleVar()
entry_ec_eff=DoubleVar()
entry_Deq_c=DoubleVar()
entry_Deq_l=DoubleVar()
entry_KDeq_c=DoubleVar()
entry_KDeq_l=DoubleVar()
entry_wlim=DoubleVar()
entry_w_part_courante=DoubleVar()
entry_Q=DoubleVar()
entry_q_rep=DoubleVar()
entry_Q1=DoubleVar()
entry_Q2=DoubleVar()
entry_gamma_beton_arme=DoubleVar()
entry_gamma_beton_non_arme=DoubleVar()
entry_vs1=DoubleVar()
entry_retrait=DoubleVar()
spinbox_e=DoubleVar()
entry_retrait_diff=DoubleVar()
entry_grad_retrait=DoubleVar()
entry_lsb=DoubleVar()
entry_wsb=DoubleVar()
entry_a=DoubleVar()
entry_b=DoubleVar()
entry_c=DoubleVar()
entry_coef_Qels=DoubleVar()

def calculs(label,event):

    #déclarations de variables
    fck=entry_fck.get()
    Es1=entry_Es1.get()
    H = entry_H.get()
    fcm=float(fck) +8
    print(fcm)
    Lx=entry_lx.get()
    Ly=entry_ly.get()
    q_rep = entry_q_rep.get()
    Q=entry_Q.get()
    Q1=entry_Q1.get()
    Q2=entry_Q2.get()
    vs1 = entry_vs1.get()
    gamma_ba=entry_gamma_beton_arme.get()
    gamma_b=entry_gamma_beton_non_arme.get()
    dmax=float(spinbox_dmax.get())
    e=float(spinbox_e.get())
    a=entry_a.get()
    b=entry_b.get()
    c=entry_c.get()
    coef_Q_els=entry_coef_Qels.get()


    ecm=int(22000*(((fcm)/10)**(0.3)))
    ec_eff=int(ecm/3)
    #Calculs de Deq
    Deq_i=round(float(1.97*float(H)*((ecm/float(Es1))**(1/3))),2)
    Deq_v=round(float(1.97*float(H)*((ec_eff/float(Es1))**(1/3))),2)
    #Calculs de KDeq
    Kdeq_i=round(float(0.58*(float(Es1)/float(H))*((float(Es1)/float(ecm))**(1/3))),2)
    Kdeq_v=round(float(0.58*(float(Es1)/float(H))*((float(Es1)/float(ec_eff))**(1/3))),2)
    #déformations limites
    wlim=round((min(float(Lx),float(Ly))*(10**(-3))/2000)+10,2)
    #déformations en partie courante
    if var_type=='N':
        g=float(float(gamma_b)*float(H)) #kN/m²
    else:
        g=float(float(gamma_ba)*float(H))  #kN/m²
    #charge répartie
    if q_rep == '':
        w_q=0
    else:
        w_q=(float(q_rep))*(1-(float(vs1)**2))*float(Deq_v)/float(Es1)
    #charge permanente
    w_g=float(g)*(1-(float(vs1)**2))*float(Deq_v)/float(Es1)
    #charge ponctuelle
    if Q == '':
        w_Q=0
    else:
        w_Q=float(4*float(Q)/(3.14*float(Deq_v)*float(Deq_v)*float(Kdeq_v)))
    #essieu
    if Q1=='' and Q2=='':
        w_essieu=0
    else:
        w_essieu=float((4*float(Q1)/(3.14*float(Deq_i)*float(Deq_i)*float(Kdeq_i)))+(4*float(Q2)/(3.14*float(Deq_i)*float(Deq_i)*float(Kdeq_i))))
    w_partie_courante = round(float(w_q)+float(w_g)+float(w_Q)+float(w_essieu),1)
    print(w_q)
    print(w_g)
    print(w_Q)
    print(w_essieu)
    #retrait linéaire
    if dmax==20:
        er=round(float(0.4+(0.4*7/100)),3)
    if dmax==15:
        er=round(float(0.4+(0.4*13/100)),3)
    if dmax==10:
        er=round(float(0.4+(0.4*30/100)),3)
    #retrait différentiel
    if float(e) == 0:
        er_diff=round(float(er),3)
    else:
        er_diff=round(float(float(er)*(1+(1/(1+(0.5*float(H)/float(e)))))),3)
    #retrait_gradient_thermique
    C=DoubleVar()
    if var_type1 =='A':
        C=20
    else :
        C=70
    er_grad=round(float(float(er)+ 1.1*float(C)*float(H)*0.0001),3)
    # DEFORMATIONS EN BORDURE DE DALLE 
    #calculs de Lsb
    if var_type=='N':
        ga_=float(gamma_b)*(10**(-3))
    else:
        ga_=float(gamma_ba)*(10**(-3))
    Lsb=round(float((0.0375*float(er_grad*10**-3)*float(ec_eff)*float(H)/float(ga_))**(0.5)),2)
    #calculs de wsb
    U=float(2.26*float(Lsb)/float(Deq_v))
    Esq=float(7.645*float(ec_eff)*((float(H)/float(Deq_v))**3))
    part1=float(0.067*((float(er_grad)*10**(-3))**2)*float(ec_eff)/float(ga_))
    part2=float(1.975*float(ga_)*float(H)*float(Lsb)/float(Esq))
    part3=float(2+(3*float(U))+2*(float(U)**2))
    wsb=round(float(float(part1)-(float(part2)*float(part3)))*(10**3),3)
    
    #calculs de Qe(els)
    #Deq/8
    Deq_8=float(float(Deq_i)/8)
    print("Deq/8=", Deq_8)
    #surface d'impact
    s_deq=float(float(Deq_8)*float(Deq_8))
    #cas 1: essieu parallèle au joint, les 2 charges
    #d1 et d2
    d1_1=float(min(float(b),float(c))/2)
    Q1_els=float(float(Q1)*float(coef_Q_els)*0.001)
    Q2_els=float(float(Q2)*float(coef_Q_els)*0.001)
    print("Q1_els=", Q1_els)
    print("Q2_els=", Q2_els)
    somme_1=float((float(Q1_els)*(1-(float(d1_1)/float(Lsb))))+(float(Q2_els)*(1-(float(d1_1)/float(Lsb)))))
    print("somme1=",somme_1)
    bord_1=float(6*float(H)/(float(a)+(6*float(H))))
    print("bord=",bord_1)
    prod_1=float(somme_1)*float(bord_1)
    if var_joint1=='B':
        k1=0.15
    if var_joint1 == 'A':
        k1=0
    if var_joint1 == 'C':
        k1=0
    print(k1)


    entry_Ecm.configure(text=ecm)
    entry_Ec_eff.configure(text=ec_eff)
    entry_Deq_c.configure(text=Deq_i)
    entry_Deq_l.configure(text=Deq_v)
    entry_Deq_l.configure(text=Deq_v)
    entry_KDeq_c.configure(text=Kdeq_i)
    entry_KDeq_l.configure(text=Kdeq_v)
    entry_wlim.configure(text=wlim)
    entry_w_part_courante.configure(text=w_partie_courante)
    entry_retrait.configure(text=er)
    entry_retrait_diff.configure(text=er_diff)
    entry_grad_retrait.configure(text=er_grad)
    entry_lsb.configure(text=Lsb)
    entry_wsb.configure(text=wsb)


def afficher_fen_deformations():
    top_level_deformations.deiconify()

    
def afficher_fen_sollicitations():
    top_level_sollicitations.deiconify()





#menu
menubar=Menu(root0)
root0.config(menu=menubar)

menufichier=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier",menu=menufichier)

menufichier.add_command(label="Ouvrir",command=ouvrir)
menufichier.add_separator
menufichier.add_command(label="Enregistrer")
menufichier.add_command(label="Enregister sous",command=enregistrer_sous)
menufichier.add_separator
menufichier.add_command(label="Quitter",command=quitter)













#titre
label_titre= Label(root0,text='Titre')
label_titre.place(x=10,y=20)

entry_titre= Entry(root0)
entry_titre.place(x=50,y=20)
entry_titre.config(width=70)

#règlement
label_reglement= Label(root0,text='Règlement')
label_reglement.place(x=10,y=50)

choice_reglement=['DTU 13.3 - Mars 2005']
entry_reglement= ttk.Combobox(root0,values=choice_reglement)
entry_reglement.place(x=80,y=50)
entry_reglement.config(width=70)
entry_reglement.current('0')

#type de dallage
type_B=ttk.Panedwindow(root0,orient=HORIZONTAL)
typeb=ttk.Labelframe(type_B,text='type de dallage',width=300,height=50)
type_B.add(typeb)
type_B.place(x=30,y=100)

values= ['N','O']
var_type=StringVar()
for i in range(2):
    type1=ttk.Radiobutton(typeb,text='dallage non armé',variable=var_type,value='N')
    type2=ttk.Radiobutton(typeb,text='dallage armé',variable=var_type,value='O')
type1.place(x=10,y=10)
type2.place(x=150,y=10)

#exposition du dallage
expo=ttk.Panedwindow(root0,orient=HORIZONTAL)
expo0=ttk.Labelframe(expo,width=300,height=50)
expo.add(expo0)
expo.place(x=380,y=100)

values= ['A','N']
var_type1=StringVar()
for i in range(2):
    expo1=ttk.Radiobutton(expo0,text='dallage abrité',variable=var_type1,value='A')
    expo2=ttk.Radiobutton(expo0,text='dallage non abrité',variable=var_type1,value='N')
expo1.place(x=10,y=10)
expo2.place(x=150,y=10)







style = ttk.Style(root0)
style.configure("lefttab.TNotebook")

notebook = ttk.Notebook(root0, style="lefttab.TNotebook")







#GEOMETRIE
frame_geometrie=Frame(notebook,width=500,height=400, relief=GROOVE,bd=4 )

#Epaisseur H
label_H= Label(frame_geometrie, text="Epaisseur du dallage: H =")
entry_H= Entry(frame_geometrie)
label_unite_H=Label(frame_geometrie,text='m')
label_H.place(x=10,y=20)
entry_H.place(x=180,y=20)
entry_H.configure(width=8)
label_unite_H.place(x=230,y=20)

#Chape e
label_e= Label(frame_geometrie, text="Epaisseur de chape: e =")
choice_e=[0,1,2,3,4,5]
spinbox_e= ttk.Combobox(frame_geometrie,value=choice_e)
label_unite_e=Label(frame_geometrie,text='m')
label_e.place(x=10,y=48)
spinbox_e.place(x=180,y=48)
spinbox_e.configure(width=4)
spinbox_e.current('0')
label_unite_e.place(x=230,y=48)

#rectangle panneau
panneau=Canvas(frame_geometrie)
panneau.create_rectangle((10,10),(300,200),width=2,outline='green')
panneau.place(x=150,y=110)

#joint1
label_joint1= Label(frame_geometrie,text="Joint 1",fg='red')
label_joint1.place(x=165,y=190)


#joint2
label_joint2= Label(frame_geometrie,text="Joint 2",fg='red')
label_joint2.place(x=405,y=190)


#joint3
label_joint3= Label(frame_geometrie,text="Joint 3",fg='red')
label_joint3.place(x=280,y=125)


#joint4
label_joint4= Label(frame_geometrie,text="Joint 4",fg='red')
label_joint4.place(x=280,y=285)


#ly
label_ly=Label(frame_geometrie,text="Ly= ")
entry_ly=Entry(frame_geometrie)
label_unite_ly=Label(frame_geometrie,text='m')
label_ly.place(x=40,y=190)
entry_ly.place(x=80,y=190)
entry_ly.configure(width=6)
label_unite_ly.place(x=120,y=190)

#ly
label_lx=Label(frame_geometrie,text="Lx= ")
entry_lx=Entry(frame_geometrie)
label_unite_lx=Label(frame_geometrie,text='m')
label_lx.place(x=235,y=325)
entry_lx.place(x=265,y=325)
entry_lx.configure(width=6)
label_unite_lx.place(x=305,y=325)

#repère


p=ttk.PanedWindow(frame_geometrie,orient=VERTICAL)
f1=ttk.Labelframe(p,text='Joint 1',width=90, height=90)
f2=ttk.Labelframe(p,text='Joint 2',width=90, height=90)
f3=ttk.Labelframe(p,text='Joint 3',width=90, height=90)
f4=ttk.Labelframe(p,text='Joint 4',width=90, height=90)
p.add(f1)
p.add(f2)
p.add(f3)
p.add(f4)
p.place(x=500,y=5)

#radiobutton
values=['A','B','C']
var_joint1=StringVar()
for i in range(3):
    joint1_0=ttk.Radiobutton(f1,text='libre',variable=var_joint1,value='A')
    joint1_1=ttk.Radiobutton(f1,text='conjugué',variable=var_joint1,value='B')
    joint1_2=ttk.Radiobutton(f1,text='bloqué',variable=var_joint1,value='C')
joint1_0.place(x=10,y=5)
joint1_1.place(x=10,y=25)
joint1_2.place(x=10,y=45)

values=['A','B','C']
var_joint2=StringVar()
for i in range(3):
    joint2_0=ttk.Radiobutton(f2,text='libre',variable=var_joint2,value='A')
    joint2_1=ttk.Radiobutton(f2,text='conjugué',variable=var_joint2,value='B')
    joint2_2=ttk.Radiobutton(f2,text='bloqué',variable=var_joint2,value='C')
joint2_0.place(x=10,y=5)
joint2_1.place(x=10,y=25)
joint2_2.place(x=10,y=45)

values=['A','B','C']
var_joint3=StringVar()
for i in range(3):
    joint3_0=ttk.Radiobutton(f3,text='libre',variable=var_joint3,value='A')
    joint3_1=ttk.Radiobutton(f3,text='conjugué',variable=var_joint3,value='B')
    joint3_2=ttk.Radiobutton(f3,text='bloqué',variable=var_joint3,value='C')
joint3_0.place(x=10,y=5)
joint3_1.place(x=10,y=25)
joint3_2.place(x=10,y=45)

values=['A','B','C']
var_joint4=StringVar()
for i in range(3):
    joint4_0=ttk.Radiobutton(f4,text='libre',variable=var_joint4,value='A')
    joint4_1=ttk.Radiobutton(f4,text='conjugué',variable=var_joint4,value='B')
    joint4_2=ttk.Radiobutton(f4,text='bloqué',variable=var_joint4,value='C')
joint4_0.place(x=10,y=5)
joint4_1.place(x=10,y=25)
joint4_2.place(x=10,y=45)








#ICONE BETON
frame_beton=Frame(notebook,width=350, height=300,bd=4, relief=GROOVE)
frame_beton.place(x=10,y=90)

#fck
label_fck= Label(frame_beton, text="fck=")
choice_fck=[25,30,35,40]
entry_fck= ttk.Combobox(frame_beton, values=choice_fck)
entry_fck.current('0')
label_unite_fck=Label(frame_beton,text="MPa")
label_fck.place(x=10,y=10)
entry_fck.place(x=40,y=10)
entry_fck.configure(width=10)
label_unite_fck.place(x=150,y=10)
#gamma_beton_armé
label_gamma_beton_arme= Label(frame_beton, text="ϒ béton armé=")
choice_gamma_beton_arme=[25]
entry_gamma_beton_arme= ttk.Combobox(frame_beton,values=choice_gamma_beton_arme)
entry_gamma_beton_arme.current('0')
label_unite_gamma_beton_arme=Label(frame_beton,text="kN/m3")
label_gamma_beton_arme.place(x=10,y=50)
entry_gamma_beton_arme.place(x=120,y=50)
entry_gamma_beton_arme.configure(width=6)
label_unite_gamma_beton_arme.place(x=200,y=50)
#gamma_béton_non_armé
label_gamma_beton_non_arme= Label(frame_beton, text="ϒ béton non armé=")
choice_gamma_beton_non_arme=[24]
entry_gamma_beton_non_arme= ttk.Combobox(frame_beton,values=choice_gamma_beton_non_arme)
entry_gamma_beton_non_arme.current('0')
label_unite_gamma_beton_non_arme=Label(frame_beton,text="kN/m3")
label_gamma_beton_non_arme.place(x=10,y=80)
entry_gamma_beton_non_arme.place(x=120,y=80)
entry_gamma_beton_non_arme.configure(width=6)
label_unite_gamma_beton_non_arme.place(x=200,y=80)
#coef de poisson du béton
label_vbeton= Label(frame_beton, text="Coefficient de Poisson ν=")
entry_vbeton= Entry(frame_beton)
label_unite_vbeton=Label(frame_beton,text="")
label_vbeton.place(x=10,y=110)
entry_vbeton.place(x=150,y=110)
entry_vbeton.configure(width=10)
label_unite_vbeton.place(x=220,y=110)
#dmax
label_dmax= Label(frame_beton, text="Dmax (granulats)=")
choice_dmax=[10,15,20]
spinbox_dmax= ttk.Combobox(frame_beton,values=choice_dmax)
spinbox_dmax.current('0')
label_unite_dmax= Label(frame_beton,text="mm")
label_dmax.place(x=10,y=140)
spinbox_dmax.place(x=120,y=140)
spinbox_dmax.configure(width=6)
label_unite_dmax.place(x=200,y=140)





#ICONE ACIERS
frame_aciers=Frame(notebook,width=350, height=300,bd=4, relief=GROOVE)



#fyk
label_fyk= Label(frame_aciers, text="fyk=")
choice_fyk=[500]
entry_fyk= ttk.Combobox(frame_aciers,values=choice_fyk)
entry_fyk.current('0')
label_unite_fyk=Label(frame_aciers,text="MPa")
label_fyk.place(x=10,y=20)
entry_fyk.place(x=40,y=20)
entry_fyk.configure(width=10)
label_unite_fyk.place(x=130,y=20)
#gt
label_gt= Label(frame_aciers, text="gt")
label_nappeinf=Label(frame_aciers,text='Nappe inf')
label_nappesup=Label(frame_aciers,text='Nappe sup')
choice_nappeinf=[0.07]
choice_nappesup=[0.07]
entry_gtinf= ttk.Combobox(frame_aciers,values=choice_nappeinf)
entry_gtinf.current('0')
entry_gtsup= ttk.Combobox(frame_aciers,values=choice_nappesup)
entry_gtsup.current('0')
label_unite_nappeinf=Label(frame_aciers,text="m")
label_unite_nappesup=Label(frame_aciers,text="m")
label_gt.place(x=10,y=100)
label_nappeinf.place(x=60,y=70)
label_nappesup.place(x=200,y=70)
entry_gtinf.place(x=60,y=100)
entry_gtsup.place(x=200,y=100)
entry_gtinf.configure(width=4)
entry_gtsup.configure(width=4)
label_unite_nappeinf.place(x=110,y=100)
label_unite_nappesup.place(x=250,y=100)






#ICONE CHARGEMENT
frame_chargement=Frame(notebook,width=710, height=300,bd=4, relief=GROOVE)

p1=ttk.PanedWindow(frame_chargement,orient=HORIZONTAL)
#charge ponctuelle
frame_charge_ponctuelle=ttk.LabelFrame(p1,text='Charge ponctuelle',width=200,height=200)


#Q
label_Q= Label(frame_charge_ponctuelle, text="Q=")
entry_Q= Entry(frame_charge_ponctuelle)
label_unite_Q=Label(frame_charge_ponctuelle,text="kN")
label_Q.place(x=10,y=40)
entry_Q.place(x=40,y=40)
entry_Q.configure(width=8)
label_unite_Q.place(x=90,y=40)
#position de Q
label_position=Label(frame_charge_ponctuelle,text='Position de la charge ponctuelle')
position_x=Label(frame_charge_ponctuelle,text='x=')
position_y=Label(frame_charge_ponctuelle,text='y=')
entry_x=Entry(frame_charge_ponctuelle)
entry_y=Entry(frame_charge_ponctuelle)
label_unite_x=Label(frame_charge_ponctuelle,text='m')
label_unite_y=Label(frame_charge_ponctuelle,text='m')
label_position.place(x=10,y=80)
position_x.place(x=10,y=100)
entry_x.place(x=30,y=100)
entry_x.configure(width=8)
label_unite_x.place(x=110,y=100)
position_y.place(x=10,y=125)
entry_y.place(x=30,y=125)
entry_y.configure(width=8)
label_unite_y.place(x=110,y=125)

#couple de charges ponctuelles
frame_couple=ttk.LabelFrame(p1,text='Couple de charges ponctuelles',width=330,height=335)

#Q1
label_Q1= Label(frame_couple, text="Q1=")
entry_Q1= Entry(frame_couple)
label_unite_Q1=Label(frame_couple,text="kN")
label_Q1.place(x=10,y=40)
entry_Q1.place(x=50,y=40)
entry_Q1.configure(width=6)
label_unite_Q1.place(x=90,y=40)
#Q2
label_Q2= Label(frame_couple, text="Q2=")
entry_Q2= Entry(frame_couple)
label_unite_Q2=Label(frame_couple,text="kN")
label_Q2.place(x=190,y=40)
entry_Q2.place(x=220,y=40)
entry_Q2.configure(width=8)
label_unite_Q2.place(x=270,y=40)
#pression de contact
label_pression_de_contact=Label(frame_couple,text='Pression de contact=')
choice_pression_de_contact=[5,6]
entry_pression_de_contact=ttk.Combobox(frame_couple,values=choice_pression_de_contact)
entry_pression_de_contact.current('0')
label_unite_pression_de_contact=Label(frame_couple,text='MPa')
label_pression_de_contact.place(x=10,y=90)
entry_pression_de_contact.place(x=130,y=90)
entry_pression_de_contact.configure(width=4)
label_unite_pression_de_contact.place(x=180,y=90)
#type de trafic
label_type_trafic=Label(frame_couple,text='Type de trafic=')
choice_type_trafic=['Occasionnel','Courant','Intense']
entry_type_trafic=ttk.Combobox(frame_couple,values=choice_type_trafic)
entry_type_trafic.current('0')
label_type_trafic.place(x=10,y=120)
entry_type_trafic.place(x=100,y=120)
entry_type_trafic.configure(width=12)
#distance a,b,c
rectangle1=Canvas(frame_couple)
rectangle1.create_rectangle((10,10),(35,50),width=2,outline='green')
rectangle1.place(x=35,y=180)
rectangle2=Canvas(frame_couple)
rectangle2.create_rectangle((10,10),(35,50),width=2,outline='green')
rectangle2.place(x=132,y=180)
ligne1=Canvas(frame_couple)
ligne1.create_line((10,20),(110,20),arrow='both',width=1)
ligne1.place(x=45,y=240)
label_a_dim=Label(frame_couple,text="a")
label_a_dim.place(x=100,y=237)
label_b_dim=Label(frame_couple,text="b")
label_b_dim.place(x=148,y=168)
label_c_dim=Label(frame_couple,text="c")
label_c_dim.place(x=169,y=195)

label_a=Label(frame_couple,text='a=')
entry_a=Entry(frame_couple)
label_unite_a=Label(frame_couple,text='m')
label_a.place(x=220,y=180)
entry_a.place(x=250,y=180)
entry_a.configure(width=6)
label_unite_a.place(x=300,y=180)

label_b=Label(frame_couple,text='b=')
entry_b=Entry(frame_couple)
label_unite_b=Label(frame_couple,text='m')
label_b.place(x=220,y=210)
entry_b.place(x=250,y=210)
entry_b.configure(width=6)
label_unite_b.place(x=300,y=210)

label_c=Label(frame_couple,text='c=')
entry_c=Entry(frame_couple)
label_unite_c=Label(frame_couple,text='m')
label_c.place(x=220,y=240)
entry_c.place(x=250,y=240)
entry_c.configure(width=6)
label_unite_c.place(x=300,y=240)

#text
text1=Label(frame_couple,text='a: distance entre les deux charges',font=italique1,fg='grey')
text1.place(x=20,y=280)

text2= Label(frame_couple, text='b x c: surface de contact de chaque bandage',font=italique1,fg='grey')
text2.place(x=20,y=300)


#charge répartie
frame_repartie=ttk.LabelFrame(p1,text='Charge répartie',width=150,height=100)

#q
label_q_rep= Label(frame_repartie, text="q=")
entry_q_rep= Entry(frame_repartie)
label_unite_q_rep=Label(frame_repartie,text="kN/m²")
label_q_rep.place(x=10,y=40)
entry_q_rep.place(x=40,y=40)
entry_q_rep.configure(width=8)
label_unite_q_rep.place(x=90,y=40)


p1.add(frame_charge_ponctuelle)
p1.add(frame_couple)
p1.add(frame_repartie)
p1.place(x=5,y=5)










#ICONE SOL SUPPORT
frame_sol_support=Frame(notebook,width=410, height=300,bd=4, relief=GROOVE)


#nombre de couches
label_nb_couches=Label(frame_sol_support,text='Nombre de couches=')
choice_nb_couches=[1,2,3,4,5]
entry_nb_couches=ttk.Combobox(frame_sol_support,values=choice_nb_couches)
entry_nb_couches.current('0')
label_nb_couches.place(x=10,y=20)
entry_nb_couches.place(x=140,y=20)
entry_nb_couches.configure(width=4)

#modules de déformations
#couches
label_couches=Label(frame_sol_support,text='Couches')
label_couches.place(x=20,y=60)

#Es
label_Es=Label(frame_sol_support,text='Es (en MPa)')
label_Es.place(x=100,y=60)

#coef de poisson
label_vs=Label(frame_sol_support,text='Coefficient de Poisson ν')
label_vs.place(x=180,y=60)

#epaisseur de couches
label_ep=Label(frame_sol_support,text='Epaisseur (m)')
label_ep.place(x=340,y=60)

#numéro de couches
label_couche1=Label(frame_sol_support,text='1')
label_couche1.place(x=30,y=80)
label_couche2=Label(frame_sol_support,text='2')
label_couche2.place(x=30,y=100)
label_couche3=Label(frame_sol_support,text='3')
label_couche3.place(x=30,y=120)
label_couche4=Label(frame_sol_support,text='4')
label_couche4.place(x=30,y=140)
label_couche5=Label(frame_sol_support,text='5')
label_couche5.place(x=30,y=160)

#Esi
entry_Es1=Entry(frame_sol_support)
entry_Es1.place(x=100,y=80)
entry_Es1.configure(width=8)
entry_Es2=Entry(frame_sol_support)
entry_Es2.place(x=100,y=100)
entry_Es2.configure(width=8)
entry_Es3=Entry(frame_sol_support)
entry_Es3.place(x=100,y=120)
entry_Es3.configure(width=8)
entry_Es4=Entry(frame_sol_support)
entry_Es4.place(x=100,y=140)
entry_Es4.configure(width=8)
entry_Es5=Entry(frame_sol_support)
entry_Es5.place(x=100,y=160)
entry_Es5.configure(width=8)

#vsi
entry_vs1=Entry(frame_sol_support)
entry_vs1.place(x=210,y=80)
entry_vs1.configure(width=8)
entry_vs2=Entry(frame_sol_support)
entry_vs2.place(x=210,y=100)
entry_vs2.configure(width=8)
entry_vs3=Entry(frame_sol_support)
entry_vs3.place(x=210,y=120)
entry_vs3.configure(width=8)
entry_vs4=Entry(frame_sol_support)
entry_vs4.place(x=210,y=140)
entry_vs4.configure(width=8)
entry_vs5=Entry(frame_sol_support)
entry_vs5.place(x=210,y=160)
entry_vs5.configure(width=8)

#epaisseur de couches
entry_ep1=Entry(frame_sol_support)
entry_ep1.place(x=340,y=80)
entry_ep1.configure(width=8)
entry_ep2=Entry(frame_sol_support)
entry_ep2.place(x=340,y=100)
entry_ep2.configure(width=8)
entry_ep3=Entry(frame_sol_support)
entry_ep3.place(x=340,y=120)
entry_ep3.configure(width=8)
entry_ep4=Entry(frame_sol_support)
entry_ep4.place(x=340,y=140)
entry_ep4.configure(width=8)
entry_ep5=Entry(frame_sol_support)
entry_ep5.place(x=340,y=160)
entry_ep5.configure(width=8)

#coefficient de frottement dallage/sol
label_mu= Label(frame_sol_support, text="Coefficient de frottement support/dallage µ =")
choice_mu= [0.5,1.5]
entry_mu= ttk.Combobox(frame_sol_support,values=choice_mu)
entry_mu.current(0)
label_unite_mu=Label(frame_sol_support,text="µ=0,5 si présence de couche de glissement ; µ=1,5 si support lisse et fermé",font=italique1,fg='grey')
label_mu.place(x=10,y=195)
entry_mu.place(x=260,y=195)
entry_mu.configure(width=4)
label_unite_mu.place(x=10,y=220)










#COMBINAISONS D'ACTIONS
frame_combinaison=Frame(notebook,width=410, height=300,bd=4, relief=GROOVE)


#elu
label_elu=Label(frame_combinaison,text="A l'ELU : ")
#Gelu
choice_coef_Gelu=[1,1.35]
entry_coef_Gelu=ttk.Combobox(frame_combinaison,values=choice_coef_Gelu)
entry_coef_Gelu.current('0')
label_elu.place(x=20,y=40)
entry_coef_Gelu.place(x=100,y=40)
entry_coef_Gelu.configure(width=4)
label_Gelu=Label(frame_combinaison, text="G    +")
label_Gelu.place(x=150,y=40)
#Qelu
choice_coef_Qelu=[1,1.5]
entry_coef_Qelu=ttk.Combobox(frame_combinaison,values=choice_coef_Qelu)
entry_coef_Qelu.current('0')
entry_coef_Qelu.place(x=200,y=40)
entry_coef_Qelu.configure(width=4)
label_Qelu=Label(frame_combinaison, text="Q")
label_Qelu.place(x=250,y=40)

#els
label_els=Label(frame_combinaison,text="A l'ELS : ")
#Gels
choice_coef_Gels=[1,1.35]
entry_coef_Gels=ttk.Combobox(frame_combinaison,values=choice_coef_Gels)
entry_coef_Gels.current('0')
label_els.place(x=20,y=80)
entry_coef_Gels.place(x=100,y=80)
entry_coef_Gels.configure(width=4)
label_Gels=Label(frame_combinaison, text="G    +")
label_Gels.place(x=150,y=80)
#Qels
choice_coef_Qels=[1,1.5]
entry_coef_Qels=ttk.Combobox(frame_combinaison,values=choice_coef_Qels)
entry_coef_Qels.current('0')
entry_coef_Qels.place(x=200,y=80)
entry_coef_Qels.configure(width=4)
label_Qels=Label(frame_combinaison, text="Q")
label_Qels.place(x=250,y=80)



notebook.add(frame_geometrie, text="GEOMETRIE")
notebook.add(frame_beton, text="BETON")
notebook.add(frame_aciers,text="ACIERS")
notebook.add(frame_chargement, text="CHARGEMENT")
notebook.add(frame_sol_support,text="SOL SUPPORT")
notebook.add(frame_combinaison,text="COMBINAISONS")

notebook.place(x=30, y=180)











#resultat1: 
res1=ttk.PanedWindow(root0,orient=VERTICAL)

#modules du béton
modules= ttk.LabelFrame(res1,text='MODULES DU BETON',width=300,height=100,relief=SUNKEN)
#Ecm
label_Ecm= Label(modules, text="Module instantané Ecm=")
entry_Ecm= Label(modules, width=7,height=1,relief=SUNKEN)
label_unite_Ecm=Label(modules,text="MPa")
label_Ecm.place(x=10,y=10)
entry_Ecm.place(x=160,y=10)
entry_Ecm.configure(width=9)
label_unite_Ecm.place(x=210,y=10)
#Ec_eff
label_Ec_eff= Label(modules, text="Module différé Ec,eff=")
entry_Ec_eff= Label(modules,width=7,height=1,relief=SUNKEN)
label_unite_Ec_eff=Label(modules,text="MPa")
label_Ec_eff.place(x=10,y=35)
entry_Ec_eff.place(x=160,y=35)
label_unite_Ec_eff.place(x=210,y=35)

#resultat2: 
res2=ttk.PanedWindow(root0,orient=VERTICAL)

#Diamètres d'impact
diamètre_deq= ttk.LabelFrame(res2,text="DIAMETRES D'IMPACT Deq",width=300,height=100,relief=SUNKEN)
#Deq_c_
label_Deq_c_= Label(diamètre_deq, text="Deq (courte durée)=")
entry_Deq_c= Label(diamètre_deq,width=7,height=1,relief=SUNKEN)
label_unite_Deq_c_=Label(diamètre_deq,text="m")
label_Deq_c_.place(x=10,y=10)
entry_Deq_c.place(x=160,y=10)
label_unite_Deq_c_.place(x=210,y=10)
#Deq_l_
label_Deq_l_= Label(diamètre_deq, text="Deq (longue durée)=")
entry_Deq_l= Label(diamètre_deq,width=7,height=1,relief=SUNKEN)
label_unite_Deq_l_=Label(diamètre_deq,text="m")
label_Deq_l_.place(x=10,y=35)
entry_Deq_l.place(x=160,y=35)
label_unite_Deq_l_.place(x=210,y=35)

#resultat3: 
res3=ttk.PanedWindow(root0,orient=VERTICAL)
#MODULE CONVENTIONNEL DE REACTION DU SUPPORT
module_Kdeq= ttk.LabelFrame(res3,text="MODULE CONVENTIONNEL DE REACTION DU SUPPORT KDeq",width=350,height=100,relief=SUNKEN)
#Kdeq_c_
label_Kdeq_c_= Label(module_Kdeq, text="K Deq (courte durée)=")
entry_KDeq_c= Label(module_Kdeq,width=7,height=1,relief=SUNKEN)
label_unite_Kdeq_c_=Label(module_Kdeq,text="MPa/m")
label_Kdeq_c_.place(x=10,y=10)
entry_KDeq_c.place(x=160,y=10)
label_unite_Kdeq_c_.place(x=210,y=10)
#Kdeq_l_
label_Kdeq_l_= Label(module_Kdeq, text="K Deq (longue durée)=")
entry_KDeq_l= Label(module_Kdeq,width=7,height=1,relief=SUNKEN)
label_unite_Kdeq_l_=Label(module_Kdeq,text="MPa/m")
label_Kdeq_l_.place(x=10,y=35)
entry_KDeq_l.place(x=160,y=35)
label_unite_Kdeq_l_.place(x=210,y=35)


res1.add(modules)
res1.place(x=780,y=30)
res2.add(diamètre_deq)
res2.place(x=780,y=150)
res3.add(module_Kdeq)
res3.place(x=780,y=270)

label=Label(root0)
root0.bind('<ButtonPress-1>',partial(calculs,label))












#Déformations et tassements
top_level_deformations=Toplevel(root0,width=700,height=400)
top_level_deformations.withdraw()
top_level_deformations.resizable('false','False')
#button_deformations
Button_deformations=Button(root0,text="DEFORMATIONS ET TASSEMENTS", relief=RAISED,command=afficher_fen_deformations)
Button_deformations.place(x=780,y=400)

def_=ttk.PanedWindow(top_level_deformations)
#déformation limite
def_lim=ttk.LabelFrame(def_,text='DEFORMATION LIMITE',width=300,height=70,relief=SUNKEN)

label_wlim=Label(def_lim,text='w lim=')
entry_wlim= Label(def_lim, width=7,height=1,relief=SUNKEN)
label_unite_wlim=Label(def_lim,text="mm")
label_wlim.place(x=10,y=10)
entry_wlim.place(x=80,y=10)
entry_wlim.configure(width=9)
label_unite_wlim.place(x=150,y=10)

#tassement en partie courante
def_part_courante=ttk.LabelFrame(def_,text='TASSEMENT EN PARTIE COURANTE',width=300,height=200,relief=SUNKEN)

label_w_part_courante=Label(def_part_courante,text='w =')
entry_w_part_courante= Label(def_part_courante, width=7,height=1,relief=SUNKEN)
label_unite_w_part_courante=Label(def_part_courante,text="mm")
label_w_part_courante.place(x=10,y=10)
entry_w_part_courante.place(x=180,y=10)
entry_w_part_courante.configure(width=9)
label_unite_w_part_courante.place(x=250,y=10)
#retrait linéaire
label_retrait= Label(def_part_courante,text="Retrait linéaire εr=")
entry_retrait= Label(def_part_courante,width=7,height=1,relief=SUNKEN)
label_unite_retrait= Label(def_part_courante, text="mm/m")
label_retrait.place(x=10,y=35)
entry_retrait.place(x=180,y=35)
entry_retrait.configure(width=9)
label_unite_retrait.place(x=250,y=35)
#retrait différentiel
label_retrait_diff= Label(def_part_courante,text="Retrait différentiel ε'r=")
entry_retrait_diff= Label(def_part_courante,width=7,height=1,relief=SUNKEN)
label_unite_retrait_diff= Label(def_part_courante, text="mm/m")
label_retrait_diff.place(x=10,y=60)
entry_retrait_diff.place(x=180,y=60)
entry_retrait_diff.configure(width=9)
label_unite_retrait_diff.place(x=250,y=60)
#effets conjugués du retrait différentiel et gradient thermique
label_grad_retrait= Label(def_part_courante,text='ε"r=')
entry_grad_retrait= Label(def_part_courante,width=7,height=1,relief=SUNKEN)
label_unite_grad_retrait= Label(def_part_courante, text="mm/m")
label_grad_retrait.place(x=10,y=85)
entry_grad_retrait.place(x=180,y=85)
entry_grad_retrait.configure(width=9)
label_unite_grad_retrait.place(x=250,y=85)
label_rmq=Label(def_part_courante,text='''ε"r: effets conjugués de ε'r et du gradient thermique''',font=italique1,fg='grey')
label_rmq.place(x=10,y=110)


#.add()
def_.add(def_lim)
def_.add(def_part_courante)
def_.place(x=20,y=20)

def_1=ttk.PanedWindow(top_level_deformations)

#tassement en bordure de dalle
def_bordure=ttk.LabelFrame(def_1,text='DEFORMATIONS EN BORDUERE DE DALLE',width=350,height=130,relief=SUNKEN)
#Lsb
label_lsb=Label(def_bordure,text='Longueur de soulèvement Lsb=')
entry_lsb= Label(def_bordure, width=7,height=1,relief=SUNKEN)
label_unite_lsb=Label(def_bordure,text="m")
label_lsb.place(x=10,y=10)
entry_lsb.place(x=200,y=10)
entry_lsb.configure(width=9)
label_unite_lsb.place(x=270,y=10)
#wsb
label_wsb=Label(def_bordure,text='Soulèvement wsb=')
entry_wsb= Label(def_bordure, width=7,height=1,relief=SUNKEN)
label_unite_wsb=Label(def_bordure,text="mm")
label_wsb.place(x=10,y=35)
entry_wsb.place(x=200,y=35)
entry_wsb.configure(width=9)
label_unite_wsb.place(x=270,y=35)
#wrb
label_wrb=Label(def_bordure,text='Flèche résiduelle wrb=')
entry_wrb= Label(def_bordure, width=7,height=1,relief=SUNKEN)
label_unite_wrb=Label(def_bordure,text="mm")
label_wrb.place(x=10,y=60)
entry_wrb.place(x=200,y=60)
entry_wrb.configure(width=9)
label_unite_wrb.place(x=270,y=60)
#wcb
label_wcb=Label(def_bordure,text='Tassement complémentaire wc=')
entry_wcb= Label(def_bordure, width=7,height=1,relief=SUNKEN)
label_unite_wcb=Label(def_bordure,text="mm")
label_wcb.place(x=10,y=85)
entry_wcb.place(x=200,y=85)
entry_wcb.configure(width=9)
label_unite_wcb.place(x=270,y=85)

#tassement en bordure de dalle
def_angle=ttk.LabelFrame(def_1,text='DEFORMATIONS EN ANGLE DE DALLE',width=350,height=130,relief=SUNKEN)
#Lsa
label_lsa=Label(def_angle,text='Longueur de soulèvement Lsa=')
entry_lsa= Label(def_angle, width=7,height=1,relief=SUNKEN)
label_unite_lsa=Label(def_angle,text="m")
label_lsa.place(x=10,y=10)
entry_lsa.place(x=200,y=10)
entry_lsa.configure(width=9)
label_unite_lsa.place(x=270,y=10)
#wsa
label_wsa=Label(def_angle,text='Soulèvement wsa=')
entry_wsa= Label(def_angle, width=7,height=1,relief=SUNKEN)
label_unite_wsa=Label(def_angle,text="mm")
label_wsa.place(x=10,y=35)
entry_wsa.place(x=200,y=35)
entry_wsa.configure(width=9)
label_unite_wsa.place(x=270,y=35)
#wra
label_wra=Label(def_angle,text='Flèche résiduelle wra=')
entry_wra= Label(def_angle, width=7,height=1,relief=SUNKEN)
label_unite_wra=Label(def_angle,text="mm")
label_wra.place(x=10,y=60)
entry_wra.place(x=200,y=60)
entry_wra.configure(width=9)
label_unite_wra.place(x=270,y=60)
#wca
label_wca=Label(def_angle,text='Tassement complémentaire wc=')
entry_wca= Label(def_angle, width=7,height=1,relief=SUNKEN)
label_unite_wca=Label(def_angle,text="mm")
label_wca.place(x=10,y=85)
entry_wca.place(x=200,y=85)
entry_wca.configure(width=9)
label_unite_wca.place(x=270,y=85)

def_1.add(def_bordure)
def_1.add(def_angle)
def_1.place(x=335,y=20)

button_valid_def=Button(top_level_deformations,text='Valider',command=afficher_fen_deformations)
button_valid_def.place(x=500,y=350)
    








#sollicitations
top_level_sollicitations=Toplevel(root0,width=600,height=450)
top_level_sollicitations.withdraw()
top_level_sollicitations.resizable('false','false')
#button_sollicitations
Button_sollicitations=Button(root0,text="SOLLICITATIONS", relief=RAISED,command=afficher_fen_sollicitations)
Button_sollicitations.place(x=1000,y=400)

sol_=ttk.PanedWindow(top_level_sollicitations)
#sollicitation limite
sol_lim=ttk.LabelFrame(sol_,text='CONTRAINTE LIMITE DE TRACTION DU BETON',width=300,height=70,relief=SUNKEN)

label_sigma_lim=Label(sol_lim,text='σlim=')
entry__sigma_lim= Label(sol_lim, width=7,height=1,relief=SUNKEN)
label_unite_sigma_lim=Label(sol_lim,text="MPa")
label_sigma_lim.place(x=10,y=10)
entry__sigma_lim.place(x=50,y=10)
entry__sigma_lim.configure(width=9)
label_unite_sigma_lim.place(x=110,y=10)
#sollicitations en partie courante
sol_part_courante=ttk.LabelFrame(sol_,text='SOLLICITATIONS EN PARTIE COURANTE',width=300,height=170,relief=SUNKEN)

label_sigma_part_courante=Label(sol_part_courante,text='σ =')
entry_sigma_part_courante= Label(sol_part_courante, width=7,height=1,relief=SUNKEN)
label_unite_sigma_part_courante=Label(sol_part_courante,text="MPa")
label_sigma_part_courante.place(x=10,y=10)
entry_sigma_part_courante.place(x=40,y=10)
entry_sigma_part_courante.configure(width=9)
label_unite_sigma_part_courante.place(x=100,y=10)
#sollicitations dues au retrait linéaire
label_sigma1= Label(sol_part_courante,text="σr=")
entry_sigma1= Label(sol_part_courante,width=7,height=1,relief=SUNKEN)
label_unite_sigma1= Label(sol_part_courante, text="MPa")
label_sigma1.place(x=10,y=40)
entry_sigma1.place(x=40,y=40)
entry_sigma1.configure(width=9)
label_unite_sigma1.place(x=100,y=40)

label_rmq1=Label(sol_part_courante,text='''σr: sollicitations dues au retrait''',font=italique1,fg='grey')
label_rmq1.place(x=10,y=60)
#incidence des gradients de T° en partie courante
label_sigma2= Label(sol_part_courante,text="σt=")
entry_sigma2= Label(sol_part_courante,width=7,height=1,relief=SUNKEN)
label_unite_sigma2= Label(sol_part_courante, text="MPa")
label_sigma2.place(x=10,y=85)
entry_sigma2.place(x=40,y=85)
entry_sigma2.configure(width=9)
label_unite_sigma2.place(x=100,y=85)

label_rmq2=Label(sol_part_courante,text='''σt: incidence des gradients de T°''',font=italique1,fg='grey')
label_rmq2.place(x=10,y=110)

#sollicitations en bordure de dalle
sol_bordure=ttk.LabelFrame(sol_,text='SOLLICITATIONS EN BORDURE DE DALLE',width=300,height=70,relief=SUNKEN)

label_sigma_bordure=Label(sol_bordure,text='σ =')
entry_sigma_bordure= Label(sol_bordure, width=7,height=1,relief=SUNKEN)
label_unite_sigma_bordure=Label(sol_bordure,text="MPa")
label_sigma_bordure.place(x=10,y=10)
entry_sigma_bordure.place(x=40,y=10)
entry_sigma_bordure.configure(width=9)
label_unite_sigma_bordure.place(x=100,y=10)

#sollicitations en angle de dalle
sol_angle=ttk.LabelFrame(sol_,text='SOLLICITATIONS EN ANGLE DE DALLE',width=300,height=70,relief=SUNKEN)

label_sigma_angle=Label(sol_angle,text='σ =')
entry_sigma_angle= Label(sol_angle, width=7,height=1,relief=SUNKEN)
label_unite_sigma_angle=Label(sol_angle,text="MPa")
label_sigma_angle.place(x=10,y=10)
entry_sigma_angle.place(x=40,y=10)
entry_sigma_angle.configure(width=9)
label_unite_sigma_angle.place(x=100,y=10)

sol_.add(sol_lim)
sol_.add(sol_part_courante)
sol_.add(sol_bordure)
sol_.add(sol_angle)
sol_.place(x=20,y=20)




root0.mainloop()
