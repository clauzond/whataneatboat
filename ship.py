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


class TotalObstacles :
    def __init__(self,canvas):
        self.canvas = canvas
        self.ObstacleList = []
        self.NextObstacleNumber = 0

        self.LastObstacleCollision = (-1)

    def __repr__(self):

        attrs = vars(self)

        return('\n'.join("%s: %s" % item for item in attrs.items()))

    def addobstacle(self,x,y,rayon):

        obstacle = Obstacle(self.canvas,x,y,rayon,self.NextObstacleNumber)
        self.ObstacleList.append(obstacle)
        self.NextObstacleNumber += 1

    def is_near(self,x,y,incertitude):
        """ Détermine si un point donné par (x,y) est "près" de n'importe quel obstacle, càd s'il est dans un rayon [rayon + incertitude] d'un obstacle
        """
        for obstacle in self.ObstacleList:
            if obstacle.is_near(x,y,incertitude):
                self.LastObstacleCollision = obstacle.obstaclenumber
                return(True)
        return(False)

    def is_colliding(self,x,y):
        """ Détermine si un point donné par (x,y) est DANS n'importe quel l'obstacle, càd s'il est dans un rayon [rayon] de l'obstacle
        """
        return(self.is_near(x,y,0))

class Obstacle :

    def __init__(self,canvas,x,y,rayon,obstaclenumber):
        """ Initialisation d'un obstacle
        canvas
        emplacement (x,y) du centre de l'obstacle
        rayon de l'obstacle
        numéro de l'obstacle (pour le numéroter dans la liste et sur le canvas
        """

        self.canvas = canvas

        self.polygon,self.label = window.create_obstacle_on_canvas(canvas,x,y,rayon,obstaclenumber)

        self.x = x
        self.y = y

        self.rayon = rayon
        self.obstaclenumber = obstaclenumber

        self.LastObstacleCollision = (-1)

    def __repr__(self):

        attrs = vars(self)

        return('\n'.join("%s: %s" % item for item in attrs.items()))


    def is_near(self,x,y,incertitude):
        """ Détermine si un point donné par (x,y) est "près" de l'obstacle, càd s'il est dans un rayon [rayon + incertitude] de l'obstacle
        """
        rayon_complet = self.rayon + incertitude

        if ((self.x - rayon_complet) <= x <= (self.x + rayon_complet)) and ((self.y - rayon_complet) <= y <= (self.y + rayon_complet)):
            return(True)

        return(False)


    def is_colliding(self,x,y):
        """ Détermine si un point donné par (x,y) est DANS l'obstacle, càd s'il est dans un rayon [rayon] de l'obstacle
        """
        return(self.is_near(x,y,0))

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


        self.LastObstacleCollision = (-1)
        self.LastCollisionRadAngle = 0



    def __repr__(self):

        attrs = vars(self)

        return(' | '.join("%s: %s" % item for item in attrs.items())+"\n")

    # Ne fait rien pour l'instant
    def move(self,x,y):
        return()



## Fonctions

