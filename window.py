from tkinter import *
import ship
import math
import equation

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


    var_1=IntVar()
    var_1.set("VARIABLE 1")
    Champ_1=Entry(par_canvas,textvariable=var_1,font="Constantia 18",width=10)
    Champ_1.pack(fill=X,padx=20,pady=20)

    var_2=IntVar()
    var_2.set("VARIABLE 2")
    Champ_2=Entry(par_canvas,textvariable=var_2,font="Constantia 18",width=10)
    Champ_2.pack(fill=X,padx=20,pady=20)

    var_3=IntVar()
    var_3.set("VARIABLE 3")
    Champ_3=Entry(par_canvas,textvariable=var_3,font="Constantia 18",width=10)
    Champ_3.pack(fill=X,padx=20,pady=20)

    var_4=IntVar()
    var_4.set("VARIABLE 4")
    Champ_4=Entry(par_canvas,textvariable=var_4,font="Constantia 18",width=10)
    Champ_4.pack(fill=X,padx=20,pady=20)

    var_5=IntVar()
    var_5.set("VARIABLE 5")
    Champ_5=Entry(par_canvas,textvariable=var_5,font="Constantia 18",width=10)
    Champ_5.pack(fill=X,padx=20,pady=20)

    var_6=IntVar()
    var_6.set("VARIABLE 6")
    Champ_6=Entry(par_canvas,textvariable=var_6,font="Constantia 18",width=10)
    Champ_6.pack(fill=X,padx=20,pady=20)


    bouton_1=Button(par_canvas,text="bouton 1",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=create_parametres)
    bouton_1.pack(fill=BOTH,padx=20,pady=20)

    par_window.mainloop()


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

    #env_canvas.bind("<Button-1>", press)
    #env_canvas.bind("<B1-Motion>", motion)


    #env_canvas.bind('<Button-1>',clicksouris)

   #
   #  env_canvas.bind('<KeyPress-Left>',move_left)
   #  env_canvas.bind('<KeyPress-Right>',move_right)

   #   env_canvas.bind('<KeyRelease-Up>',release)
   #  env_canvas.bind('<KeyRelease-Left>',release)
   #  env_canvas.bind('<KeyRelease-Right>',release)




    envbutton1=Button(bottomframe,text="Démarrer l'environnement'",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=start_environment)

    envbutton1.pack(padx=10,pady=10,side=LEFT)

    envbutton2=Button(bottomframe,text="Start/Stop loop",font="Constantia 15",justify="center",overrelief="groove",activeforeground="blue",activebackground="white",bg="white",command=start_loop)
    
    menubar = Menu(env_window)
    
    # Environnement pulldown menu
    envmenu = Menu(menubar, tearoff=0)
    envmenu.add_command(label="Démarrer l'environnement",command=start_environment)
    envmenu.add_separator()
    envmenu.add_command(label="Démarrer la boucle",command=start_loop)
    
    
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
    global state_loop
    if state_loop==False:
        try:
            print("Loop démarrée")
            envmenu.entryconfig(2, label="Loop : ON")
            envbutton2.config(text="Loop : ON")
            env_canvas.config()
            state_loop=True
            loop()
        except:
            print("Environnement pas démarré !")
            state_loop=False
    else:
        envmenu.entryconfig(2,label="Loop : OFF")
        envbutton2.config(text="Loop : OFF")
        state_loop=False

def move_event(event):
    if event.keysym == 'Up':
        move_front()
    elif event.keysym == 'Left':
        move_left()
    elif event.keysym == 'Right':
        move_right()
def release(event):
    if event.keysym in ['Up','Left','Right']:

        for bateau in totalships.ShipList:
            bateau.state_ForceExist = False
            bateau.state_ForceRadAngle = 0
        print("RELEASE")


def move_front():
    for bateau in totalships.ShipList :
        bateau.state_ForceExist = True
        bateau.state_ForceRadAngle = 0
    print("FRONT")

def move_left():
    for bateau in totalships.ShipList :
        bateau.state_ForceExist = True
        bateau.state_ForceRadAngle = -(math.pi)/2
    print("LEFT")

def move_right():
    for bateau in totalships.ShipList :
        bateau.state_ForceExist = True
        bateau.state_ForceRadAngle = (math.pi)/2
    print("RIGHT")







# Fonction exécutée depuis "ship.py" dans la méthode "__init__" de "Ship"
# Créer l'image du bateau (un polygone) et l'associe au bateau self.polygon pour pouvoir le bouger plus tard

# http://tkinter.fdex.eu/doc/caw.html#ellipses-et-cercles pour "comment les coordonnées de l'ovale marche"
# coin haut gauche (x0,y0) coin bas droite (x1,y1)
def create_ship_on_canvas(canvas,x,y):
    global coords



    coords = [(x-5,y-5),(x+5,y+5)]
    Polygon = canvas.create_oval(coords,fill='red',outline='yellow',width=1)

    canvas.update()

    print("Polygon = ",Polygon,"Canvas = ",canvas)

    return(Polygon)


# Fonction qui déplace le bateau sur le canvas
# Prend comme argument "[Ship].polygon", et les coordonnées du déplacement (delta x, delta y)
def move_ship_on_canvas(bateau,polygone,tmax,tactuel):

    equation.update_ship_with_Fext(bateau,100,0,1000)
    env_canvas.move(polygone,bateau.deltax,bateau.deltay)
    tactuel += 1/60


    if tactuel < tmax:
        env_canvas.after(1,move_ship_on_canvas,bateau,polygone,tmax,tactuel)

        #[x0,y0,x1,y1]=env_canvas.coords(polygone)
        # print("Centre (x,y) du polygone n°",bateau.shipnumber," :",[(x0+x1)/2,(y0+y1)/2])
        # print("bateau.x=",bateau.x)
        # print("bateau.y=",bateau.y)
        # print("bateau.speedx=",bateau.speedx)
        # print("bateau.speedy=",bateau.speedy)
        # print("temps total :",totalships.time_since_begin)




## LOOP

def update_environnement(totalships,canvas,_lambda,dt):



    for bateau in totalships.ShipList :

        if bateau.state_ForceExist == True:
            # On applique les changements à faire, en considérant que la force du moteur EXISTE, d'angle relatif bateau.state_ForceRadAngle et d'amplitude bateau.state_ForceAmplitude
            equation.update_ship_with_Fext(bateau,dt,_lambda,bateau.state_ForceRadAngle,bateau.state_ForceAmplitude)
            print("forceexist")
        else:
            # On applique les changements à faire, en considérant que le bateau n'applique AUCUNE FORCE DE MOTEUR
            equation.update_ship_without_Fext(bateau,dt,_lambda)

        canvas.move(bateau.polygon,bateau.deltax,bateau.deltay)



    totalships.time_since_begin += dt


dt = 0.01 #(10 ms)
_lambda = 200
state_loop=False
def loop():
    global state_loop
    update_environnement(totalships,env_canvas,_lambda,dt)

    if state_loop == True :
        env_canvas.after(10,loop)
    else:
        print("Loop arrêtée")







## ENVIRONNEMENT CREATION

# NumberOfShips défini précédemment
def start_environment():
    global totalships
    
    envbutton1.config(text="Ajouter des bateaux")
    envmenu.entryconfigure(0,label="Ajouter des bateaux")

    NumberOfShips=1

    totalships = ship.TotalShips(env_canvas)

    for k in range(0,NumberOfShips):
        print("Bateau en création")
        totalships.addship(env_canvas)

    return()


## Tests pour exécuter le fichier.
# Ne pas mettre de choses nécessaires dessous, uniquement des éléments à tester.

#create_window()