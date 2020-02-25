import math
from tkinter import *

import equation
import ship

#global env_canvas

# Aide pour les interfaces Tkinter
# https://python.doctor/page-tkinter-interface-graphique-python-tutoriel

## Création de la fenêtre de départ
def create_window():
    main_window = Tk()
    main_window.title("Fenêtre principale")
    #main_window.geometry('%dx%d' % (largeur_bc*pas, hauteur_bc*pas))
    main_window.geometry('300x600')
    main_window.resizable(False, False)


    main_canvas = Canvas(main_window,bg="lightgray")
    main_canvas.pack(fill=BOTH,expand=1)

    # Bouton type :
    #Resoudre=Button(main_canvas,text="Résoudre",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=BoutonResoudre)
    #Resoudre.grid(row=##,column=##,rowspan=1,columnspan=1,padx=10,pady=10)

    bouton_environnement=Button(main_canvas,text="Environnement",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=create_environnement)
    bouton_environnement.pack(fill=X,padx=50,pady=50)

    bouton_parametres=Button(main_canvas,text="Paramètres",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=create_parametres)
    bouton_parametres.pack(fill=X,padx=50,pady=50)

    main_window.mainloop()



## Fenêtre des paramètres

def create_parametres():
    global var_1,var_2,var_3,var_4,var_5,var_6


    par_window = Toplevel()
    par_window.title("Paramètres")
    #main_window.geometry('%dx%d' % (largeur_bc*pas, hauteur_bc*pas))
    par_window.geometry('300x600')
    par_window.resizable(False, False)


    par_canvas = Canvas(par_window,bg="lightgray")
    par_canvas.pack(fill=BOTH,expand=1)



    Label_1=Label(par_canvas,font="Constantia 18",text="Valeur de LAMBDA (en kg.s-1)")
    Label_1.pack(fill=X,padx=10,pady=10)
    var_1=IntVar()
    var_1.set("200")
    Champ_1=Entry(par_canvas,textvariable=var_1,font="Constantia 18",width=10)
    Champ_1.pack(fill=X,padx=10,pady=10)



    Label_2=Label(par_canvas,font="Constantia 18",text="Valeur de AMPLITUDE FORCE (en N ou kg.m.s-2)")
    Label_2.pack(fill=X,padx=10,pady=10)
    var_2=IntVar()
    var_2.set("1000")
    Champ_2=Entry(par_canvas,textvariable=var_2,font="Constantia 18",width=10)
    Champ_2.pack(fill=X,padx=10,pady=10)

    Label_3=Label(par_canvas,font="Constantia 18",text="Valeur de MASSE BATEAU (en kg)")
    Label_3.pack(fill=X,padx=10,pady=10)
    var_3=IntVar()
    var_3.set("1000")
    Champ_3=Entry(par_canvas,textvariable=var_3,font="Constantia 18",width=10)
    Champ_3.pack(fill=X,padx=10,pady=10)

    var_4=IntVar()
    var_4.set("VARIABLE 4")
    Champ_4=Entry(par_canvas,textvariable=var_4,font="Constantia 18",width=10)
    Champ_4.pack(fill=X,padx=10,pady=10)

    var_5=IntVar()
    var_5.set("VARIABLE 5")
    Champ_5=Entry(par_canvas,textvariable=var_5,font="Constantia 18",width=10)
    Champ_5.pack(fill=X,padx=10,pady=10)

    var_6=IntVar()
    var_6.set("VARIABLE 6")
    Champ_6=Entry(par_canvas,textvariable=var_6,font="Constantia 18",width=10)
    Champ_6.pack(fill=X,padx=10,pady=10)


    bouton_1=Button(par_canvas,text="bouton 1",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=get_parametre)
    bouton_1.pack(fill=BOTH,padx=10,pady=10)

    par_window.mainloop()

def get_parametre():
    global var_1,var_2,var_3,var_4,var_5,var_6

    print(var_1.get(),var_2.get())

## Fenêtre de l'environnement [fenêtre et autre]


def create_environnement():
    global env_canvas,envmenu,envbutton1,envbutton2

    env_window = Toplevel()
    env_window.title("Environnement")
    # Pour modifier la géométrie en fonction d'un paramètre :
    #env_window.geometry('%dx%d' % (largeur_bc*pas, hauteur_bc*pas))
    env_window.geometry('600x600')
    #env_window.resizable(False, False)


    topframe = Frame(env_window)
    topframe.pack(side=TOP)

    bottomframe= Frame(env_window)
    bottomframe.pack(side=BOTTOM)

    env_canvas = Canvas(topframe,bg="lightblue",width=1980,height=550)


    env_window.bind("<KeyPress>",move_event)
    env_window.bind("<KeyRelease>",release)

    env_canvas.pack()







    envbutton1=Button(bottomframe,text="Démarrer l'environnement",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=start_environnement)

    envbutton1.pack(padx=10,pady=10,side=LEFT)

    envbutton2=Button(bottomframe,text="Loop : OFF",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",state=DISABLED,command=start_loop)

    menubar = Menu(env_window)

    # Environnement pulldown menu
    envmenu = Menu(menubar, tearoff=0)
    envmenu.add_command(label="Démarrer l'environnement",command=start_environnement)
    envmenu.add_separator()
    envmenu.add_command(label="Loop : OFF",command=start_loop,state=DISABLED)


    menubar.add_cascade(label="Environnement",menu=envmenu)

    # Affichage pulldown menu
    affmenu = Menu(menubar, tearoff=1)
    affmenu.add_command(label="Option affichage 1")
    affmenu.add_separator()
    affmenu.add_command(label="Option affichage 2")

    menubar.add_cascade(label="Affichage",menu=affmenu)

    env_canvas.bind("<Button-3>",popup)


    envbutton2.pack(padx=10,pady=10,side=LEFT)


    # Démarre l'environnement
    env_window.config(menu=menubar)
    env_window.mainloop()


def popup(event):
    envmenu.post(event.x_root,event.y_root)

# ACTUELLEMENT :
# Ce bouton démarre la loop du temps
def start_loop():
    global loop_state
    if loop_state==False:
        try:
            print("Loop démarrée")
            envmenu.entryconfig(2, label="Loop : ON")
            envbutton2.config(text="Loop : ON")
            env_canvas.config()
            loop_state=True
            loop()
        except:
            print("Environnement pas démarré !")
            loop_state=False
    else:
        envmenu.entryconfig(2,label="Loop : OFF")
        envbutton2.config(text="Loop : OFF")
        loop_state=False

def move_event(event):
    if event.keysym == 'Up':
        manual_move_front()
    elif event.keysym == 'Left':
        manual_move_left()
    elif event.keysym == 'Right':
        manual_move_right()
def release(event):
    if event.keysym in ['Up','Left','Right']:

        for bateau in totalships.ShipList:
            bateau.manual_ForceExist = False
            bateau.manual_ForceRadAngle = 0
        print("RELEASE")


def manual_move_front():
    for bateau in totalships.ShipList :
        bateau.manual_ForceExist = True
        bateau.manual_ForceRadAngle = 0
    #print("FRONT")

def manual_move_left():
    for bateau in totalships.ShipList :
        bateau.manual_ForceExist = True
        bateau.manual_ForceRadAngle = -(math.pi)/2
    #print("LEFT")

def manual_move_right():
    for bateau in totalships.ShipList :
        bateau.manual_ForceExist = True
        bateau.manual_ForceRadAngle = +(math.pi)/2
    #print("RIGHT")







# Fonction exécutée depuis "ship.py" dans la méthode "__init__" de "Ship"
# Créer l'image du bateau (un polygone) et l'associe au bateau self.polygon pour pouvoir le bouger plus tard

# http://tkinter.fdex.eu/doc/caw.html#ellipses-et-cercles pour "comment les coordonnées de l'ovale marche"
# coin haut gauche (x0,y0) coin bas droite (x1,y1)
def create_ship_on_canvas(canvas,x,y,shipnumber):
    global coords



    coords = [(x-5,y-5),(x+5,y+5)]
    Polygon = canvas.create_oval(coords,fill='white',outline='red',width=1)
    Label = canvas.create_text(x,y,text=str(shipnumber),font="Helvetica 10")
    canvas.update()

    return(Polygon,Label)





## LOOP


# 1 pixel = 1 mètre puisqu'on manipule tout en mètre, et qu'on déplace le bateau selon "bateau.deltax" qui est en mètre aussi
# update_environnement sera la fonction qui modifie l'état du système entier pendant "dt"


# manual_update_environnement est une fonction pour TESTER nos déplacements de TOUS LES BATEAUX EN MEME TEMPS
# Il donne le MEME ORDRE à TOUS LES BATEAUX !
def manual_update_environnement(totalships,canvas,_lambda,dt):



    for bateau in totalships.ShipList :

        if bateau.manual_ForceExist == True:
            # On applique les changements à faire, en considérant que la force du moteur EXISTE, d'angle relatif bateau.manual_ForceRadAngle et d'amplitude bateau.manual_ForceAmplitude
            equation.update_ship_with_Fext(bateau,dt,_lambda,bateau.manual_ForceRadAngle,bateau.manual_ForceAmplitude)
        else:
            # On applique les changements à faire, en considérant que le bateau n'applique AUCUNE FORCE DE MOTEUR
            equation.update_ship_without_Fext(bateau,dt,_lambda)

        canvas.move(bateau.polygon,bateau.deltax,bateau.deltay)
        canvas.move(bateau.label,bateau.deltax,bateau.deltay)




    totalships.time_since_begin += dt

dt = 0.01 # en s, correspond à l'unité infinitésimale de temps sur laquelle on calcule toutes les valeurs. Au plus elle est petite, au plus les calculs sont précis.
dt_ms_loop = 1 # en ms, correspond au temps que l'on met pour afficher "dt" grâce à la fonction .after(dt_ms_loop,#args) ; le temps passera bien plus vite si dt_ms_loop > dt


_lambda = 50
loop_state=False

# On peut choisir d'avoir un dt_ms_loop bien plus petit que dt pour accélérer le temps
# le facteur d'accélération de temps est alors [dt_ms_loop / dt] (en mettant les bonnes unités !)
def loop():
    global loop_state
    manual_update_environnement(totalships,env_canvas,_lambda,dt)

    if loop_state == True :
        env_canvas.after(dt_ms_loop,loop)
    else:
        print("Loop arrêtée")



# global_update_environnement donne UN ORDRE INDIVIDUEL à CHAQUE BATEAU pour la durée dt.
# C'est cette fonction qui lancera "la demande" pour les paramètres à donner pour déplacer chaque bateau, pour lancer ensuite "individual_update"
# C'est cette fonction qui déplacera les bateaux par la fonction .move après update, et +dt à totalships,time_since_begin
def global_update_environnement(totalships,canvas,dt,_lambda):
    """
    totalships : élément de la classe TotalShips, qui correspond à notre flotte de bateau
    canvas :
    dt : l'unité infinitésimale de temps, qu'on pose égale à [...] ms
    _lambda : variable expérimentale, correspond à la force de frottement en -lambda*v ; lambda en kg.s-1

    """
    return()

# individual_update donne UN ORDRE à UN SEUL BATEAU pour la durée dt.
# On peut identifier un bateau par son shipnumber (via totalships.ShipList[shipnumber]) ou encore par sa classe "Ship"
# Cela outrepassera les touches "manuelles"
def individual_update(bateau,ForceExist,):
    """
    bateau : élément de la classe Ship, qui correspond au bateau à déplacer
    ForceExist : booléen, qui nous dit si la force existe ou non
    ForceAmplitude : entier, donne l'amplitude de la force en N // potentiellement optionnel
    ForceRadAngle: orientation absolue de la force, donc en bref 0 si tout droit, négatif tourner à gauche, positif tourner à droite  [voir equation.py pour plus d'explications]

    """
    return()




## ENVIRONNEMENT CREATION

# NumberOfShips sera défini ailleurs
environnement_state = False
def start_environnement():
    """
    totalships : élément de la classe TotalShips, qui correspond à notre flotte de bateau
    environnement_state : booléen déclare l'état actuel de l'environnement ; True si démarré, False sinon
    """
    global totalships,environnement_state

    if environnement_state == False:
        environnement_state = True
        envbutton1.config(text="Ajouter un bateau")
        envmenu.entryconfigure(0,label="Ajouter un bateau")
        envbutton2.config(state=NORMAL)
        envmenu.entryconfigure(2,state=NORMAL)

        NumberOfShips=1

        totalships = ship.TotalShips(env_canvas)

        for k in range(0,NumberOfShips):
            print("Bateau en création")
            totalships.addship(env_canvas)

    else:
        totalships.addship(env_canvas)


## Tests pour exécuter le fichier.
# Ne pas mettre de choses nécessaires dessous, uniquement des éléments à tester.


#create_window()
