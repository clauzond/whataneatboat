import window
import math

_mass = 1000 # en kg
_speedx = 0 # vitesse initiale en m.s-1
_speedy = 0
_anglerad = math.pi/2 # angle initial en radian

_canvas = "vide"

_x=0 # position initiale
_y=0 # position initiale

_forceamplitude = 3000


class Mur :

    def __init__(self):
        return()

    def __reptr__(self):

        attrs = vars(self)

        return('\n'.join("%s: %s" % item for item in attrs.items()))


# (Ré)Initialise l'environnement de bateaux
class TotalShips :


    def __init__(self,canvas):
        """"

        Manipulation de ShipList : self.ShipList[n] renvoie le (n+1)ème bateau créé
        Enregistre la liste des bateaux
        Enregistre le canvas actuel de la simulation
        Enregistre le temps passé depuis le début de la simulation
        """
        self.ShipList=[]
        self.NextShipNumber=0

        self.canvas=canvas

        self.time_since_begin = 0 # en s

    def __repr__(self):

        attrs = vars(self)

        return('\n'.join("%s: %s" % item for item in attrs.items()))

# Lorsqu'on crée un bateau : on l'ajoute à la liste totale ; on lui donne un numéro unique dans l'environnement actuel
    def addship(self,canvas=_canvas,x=_x,y=_y,mass=_mass,anglerad=_anglerad,speedx=_speedx,speedy=_speedy):

        ship=Ship(self.NextShipNumber,canvas,x,y,mass,anglerad,speedx,speedy)

        self.NextShipNumber += 1
        self.ShipList.append(ship)




# Pour manipuler un bateau : [TotalShips].ShipList[nombre].fonctionàexécuter
class Ship :



    def __init__(self,shipnumber,canvas=_canvas,x=_x,y=_y,mass=_mass,anglerad=_anglerad,speedx=_speedx,speedy=_speedy):


        # Permet de distinguer un bateau d'un autre dans la liste "[TotalShips].ShipList()"
        self.shipnumber = shipnumber


        # Est-ce que le bateau doit être affiché sur l'écran ?
        #try:

            #coords = [(x,y),(x+10,y+10),(x+10,y),(x,y+10)]
            #self.polygon = canvas.create_polygon(coords,fill='red',outline='yellow',width=3)


        self.polygon,self.label = window.create_ship_on_canvas(canvas,x,y,shipnumber)

        print("Le bateau n°",str(shipnumber),"a été créé")

        #except:
        #    print("Erreur : le polygone n'a PAS été créé ! non reconnu")



        self.mass = mass
        self.speedx = speedx
        self.speedy = speedy

        self.canvas = canvas

        self.x=x
        self.y=y

        self.deltax = 0
        self.deltay = 0


        self.thetarad = anglerad
        self.thetadeg = math.degrees(anglerad)

        self.manual_ForceExist = False
        self.manual_ForceRadAngle = 0
        self.manual_ForceAmplitude = _forceamplitude #norme de la force en N(ewton) = kg.m.s-2



    def __repr__(self):

        attrs = vars(self)

        return(' | '.join("%s: %s" % item for item in attrs.items())+"\n")

    # Ne fait rien pour l'instant
    def move(self,x,y):
        return()



## Fonctions

