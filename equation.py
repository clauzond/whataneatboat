import math

"""" Fonctions à faire :
dt = 1/60 s
Les passages de t à t+dt de :
    - la vitesse sans force supplémentaire par Euler -> bateau.speedx et bateau.speedy
    - la vitesse avec force supplémentaire par Euler -> bateau.speedx et bateau.speedy
        puis deltax et deltay -> bateau.deltax et bateau.deltay
            puis bateau.x et bateau.y (fonction de dx et dy)
            puis dtheta (fonction de dx et dy)
                puis bateau.orientation (fonction de dtheta)

Unité S.I :
vitesse en m.s-1
masse en kg
temps en s-1
angles en radian, sauf contre-indication
amplitude force en N (newton)

Variables expérimentales :
masse du bateau en kg
lambda en kg.s-1
dt = 1/60 s fixe

"""

def update_ship_without_Fext(bateau,dt,_lambda):
    """
    Passe l'environnement de t (donné, l'état passé) à t+dt (nouvel état) :

    !!! NE MODIFIE PAS totalships.time_since_begin !!!

    modifie bateau.speedx et bateau.speedy sans force extérieure, avec l'aide de Euler explicite [ v(i+1) = (1 - dt/tau) v(i) ]
    puis modifie bateau.x et bateau.y (en fonction de dx et dy)
    puis modifie theta (en fonction de dtheta)

    bateau : variable de la classe Ship, correspond à 1 bateau donné
    dt : l'unité infinitésimale de temps, qu'on pose égale à [...] ms
    _lambda : variable expérimentale, correspond à la force de frottement en -lambda*v ; lambda en kg.s-1

    """



    tau = bateau.mass / _lambda # tau = masse/lambda où masse en kg, lambda en kg.s-1

    new_speedx = (1 - dt/tau)*bateau.speedx
    new_speedy = (1 - dt/tau)*bateau.speedy


    bateau.speedx = new_speedx
    bateau.speedy = new_speedy

    deltax = dt * bateau.speedx
    deltay = dt * bateau.speedy

    bateau.x += deltax
    bateau.y += deltay

    bateau.deltax = deltax
    bateau.deltay = deltay

    # Tout ceci est pour réglé le problème avec la division par 0, et le problème de signe. La fonction atan2 [ help(atan2) ] gère tout ceci
    # if deltax == 0:
    #     if deltay == 0:
    #         dtheta = 0
    #     elif deltay>0:
    #         dtheta = (math.pi)/2
    #     elif deltay<0:
    #         dtheta = -(math.pi)/2
    #
    # elif deltax != 0 :
    #     dtheta = math.atan(deltay/deltax)

    dtheta = math.atan2(deltay,deltax) # Renvoie arctan(dy/dx) en prenant en compte la potentielle nullité de dx et le signe de dy


    bateau.thetarad = dtheta # dtheta en radian
    if bateau.thetarad > 2*math.pi :
        bateau.thetarad -= 2*math.pi # on garde l'angle en radian entre 0 et 2*pi
    elif bateau.thetarad < 0:
        bateau.thetarad += 2*math.pi
    bateau.thetadeg = math.degrees(dtheta) # en degré



def update_ship_with_Fext(bateau,dt,_lambda,orientation_absolue_force,amplitude_force):
    """
    Passe l'environnement de t (donné, l'état passé) à t+dt (nouvel état) :

    !!! NE MODIFIE PAS totalships.time_since_begin !!! [cette fonction est individuelle]

    modifie bateau.speedx et bateau.speedy sans force extérieure, avec l'aide de Euler explicite [ v(i+1) = (1 - dt/tau) v(i) + dt/m * F(i)]
    puis modifie bateau.x et bateau.y (en fonction de dx et dy)
    puis modifie theta (en fonction de dtheta)

    bateau : variable de la classe Ship, correspond à 1 bateau donné
    dt : l'unité infinitésimale de temps, qu'on pose égale à [...] ms
    _lambda : variable expérimentale, correspond à la force de frottement en -lambda*v ; lambda en kg.s-1
    orientation_absolue_force : voir un schéma pour mieux se représenter, on a pris une orientation anti-trigo pour s'accorder à tkinter
        -> si = 0, tout droit [par rapport à la direction actuelle du bateau]
        -> si positive, signifie tourner à droite [par rapport à la direction actuelle du bateau]
        -> si négative, signifie tourner à gauche [par rapport à la direction actuelle du bateau]
        si tu es confus, teste pour theta=0 et orientation_absolue_force=pi/2, et voit que cela tourne bien vers la droite
    amplitude_force : Fext = F*cos(theta + orientation_absolue_force )*ux  +  F*sin(theta + orientation_absolue_force)*uy
        où F est amplitude_force en Newton
        où theta = bateau.thetarad l'orientation actuelle du bateau, s'il veut aller tout droit force dirigée vers ur par exemple.

    """
    F = amplitude_force
    theta = bateau.thetarad # orientation à t du bateau

    orientation_relative_force = theta + orientation_absolue_force # orientation "relative" de la force, càd sur notre repère tkinter

    Fx = F * math.cos(orientation_relative_force)
    Fy = F * math.sin(orientation_relative_force)


    tau = bateau.mass / _lambda # tau = masse/lambda où masse en kg, lambda en kg.s-1

    new_speedx = (1 - dt/tau)*bateau.speedx + (dt/bateau.mass)*Fx
    new_speedy = (1 - dt/tau)*bateau.speedy + (dt/bateau.mass)*Fy



    bateau.speedx = new_speedx
    bateau.speedy = new_speedy

    deltax = dt * bateau.speedx
    deltay = dt * bateau.speedy

    bateau.x += deltax
    bateau.y += deltay

    bateau.deltax = deltax
    bateau.deltay = deltay

    # Tout ceci est pour régler le problème avec la division par 0, et le problème de signe. La fonction atan2 [ help(atan2) ] gère tout ceci
    # if deltax == 0:
    #     if deltay == 0:
    #         dtheta = 0
    #     elif deltay>0:
    #         dtheta = (math.pi)/2
    #     elif deltay<0:
    #         dtheta = -(math.pi)/2
    #
    # elif deltax != 0 :
    #     dtheta = math.atan(deltay/deltax)

    dtheta = math.atan2(deltay,deltax) # Renvoie arctan(dy/dx) en prenant en compte la potentielle nullité de dx et le signe de dy


    bateau.thetarad = dtheta # dtheta en radian
    if bateau.thetarad > 2*math.pi :
        bateau.thetarad -= 2*math.pi # on garde l'angle en radian entre 0 et 2*pi
    elif bateau.thetarad < 0:
        bateau.thetarad += 2*math.pi
    bateau.thetadeg = math.degrees(dtheta) # en degré


def reaction_bateau_obstacle(bateau,dt,_lambda):
    """
    Simule la réaction d'un bateau lors qu'il entre en collision avec un obstacle
    "Renvoie le bateau avec une force proportionnelle à sa vitesse, dans une direction opposée à celle d'arrivée"

    bateau : variable de la classe Ship, correspond à 1 bateau donné
    dt : l'unité infinitésimale de temps, qu'on pose égale à [...] ms
    _lambda : variable expérimentale, correspond à la force de frottement en -lambda*v ; lambda en kg.s-1
    RadAngleCollision : voir un schéma pour mieux se représenter, on a pris une orientation anti-trigo pour s'accorder à tkinter
        -> si = 0, tout droit [par rapport à la direction actuelle du bateau]
        -> si positive, signifie tourner à droite [par rapport à la direction actuelle du bateau]
        -> si négative, signifie tourner à gauche [par rapport à la direction actuelle du bateau]
        si tu es confus, teste pour theta=0 et orientation_absolue_force=pi/2, et voit que cela tourne bien vers la droite
    amplitude_force : Fext = F*cos(theta + orientation_absolue_force )*ux  +  F*sin(theta + orientation_absolue_force)*uy
        où F est amplitude_force en Newton
        où theta = bateau.thetarad l'orientation actuelle du bateau, s'il veut aller tout droit force dirigée vers ur par exemple.

    L est une constante, le bateau sera renvoyée avec une force proportionnelle à sa vitesse
    """

    RadAngleCollision = bateau.LastCollisionRadAngle
    norme_vitesse = math.sqrt( (bateau.speedx)**2 + (bateau.speedy)**2 )
    bateau.speedx = 0
    bateau.speedy = 0
    L = 100
    """new_angle = (RadAngleCollision + math.pi)
    if new_angle > 2*math.pi:
        new_angle -= 2*math.pi
    elif new_angle < 0:
        new_angle += 2*math.pi"""

    new_angle = math.pi

    new_force = L * (_lambda * norme_vitesse)
    print("Angle de réaction :",new_angle)
    print("Force de réaction :",new_force)
    print("Force_amplitude bateau:",bateau.manual_ForceAmplitude)
    update_ship_with_Fext(bateau,dt,_lambda,new_angle,new_force)