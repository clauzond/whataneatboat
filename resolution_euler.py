from math import *

import numpy as np



# regarder pour la manipulation de vecteurs "updateShipExternalState" du module "simulationEnvironment" de utseasim



"""Conclusion de la méthode de la résolution d'Euler à lire dans le .txt"""





labda=100 # en kg s-1

masse=1000 # en kg

tau= masse/labda # en s















# en fait t0 n'intervient jamais, et c'est d'ailleurs normal



def solution_analytique(time_total=10,vx0=0,vy0=0):

    return( np.array([vx0*exp( -(time_total)/tau ),vy0*exp( -(time_total)/tau )]))





def solution_euler_explicite(n=60,time_total=10,vx0=0,vy0=0):



    # FORMULE UTILISEE : v(i+1) = ( 1 - timestep/tau )*v(i)

    # time_total en seconde, n le nombre d'intervalles pour l'approximation





    timestep = time_total/n  # en s, correspond au delta t



    vitesse = np.array([vx0,vy0])





    for i  in range(0,n+1):



        vitesse = vitesse* (1 - timestep/tau)



    return(vitesse)





def solution_euler_implicite(n=60,time_total=10,vx0=0,vy0=0):



    # FORMULE UTILISEE : v(i+1) = ( 1 - timestep/tau )*v(i)

    # time_total en seconde, n le nombre d'intervalles pour l'approximation



    timestep = time_total/n  # en s, correspond au delta t



    vitesse = np.array([vx0,vy0])





    for i  in range(0,n+1):



        vitesse = vitesse* (1 / (1 + timestep/tau))



    return(vitesse)





def comparaisons(n=60,time_total=10,vx0=0,vy0=0):



    v_ana = solution_analytique(time_total,vx0,vy0)

    v_expl = solution_euler_explicite(n,time_total,vx0,vy0)

    v_impl = solution_euler_implicite(n,time_total,vx0,vy0)



    print("Analytique :",solution_analytique(time_total,vx0,vy0))

    print("Explicite :",solution_euler_explicite(n,time_total,vx0,vy0))

    print("Implicite :",solution_euler_implicite(n,time_total,vx0,vy0))





    print("ANA - EXPLICITE :",abs(v_ana - v_expl))

    print("ANA - IMPLICITE :",abs(v_ana - v_impl))

    print("EXPLICITE - IMPLICITE",abs(v_expl - v_impl))

    return()





def division_de_la_tache(div=1,n=60,time_total=10,vx0=0,vy0=0):

    """ On divise la tache en plusieurs fois pour regarder si le résultat est cohérent :

    il faut qu'on observe que "il se passe 10 secondes" et "il se passe 5 fois 2 secondes" donnent les mêmes résultats

    donc on divise le temps par "div", puis pour i allant de 1 à div on réinjecte avec les conditions initiales du dernier résultat """



    new_time = (time_total/div)





    v_ana = solution_analytique(new_time,vx0,vy0)

    for i in range(1,div):

        v_ana = solution_analytique(new_time,v_ana[0],v_ana[1])



    print("Analytique sans division:",solution_analytique(time_total,vx0,vy0))

    print("Analytique avec division :",v_ana)





    v_expl = solution_euler_explicite(n,new_time,vx0,vy0)

    for i in range(1,div):

        v_expl = solution_euler_explicite(n,new_time,v_expl[0],v_expl[1])

    print("Explicite sans division:",solution_euler_explicite(n,time_total,vx0,vy0))

    print("Explicite avec division :",v_expl)





    new_time = (time_total/div)

    v_impl = solution_euler_implicite(n,new_time,vx0,vy0)

    for i in range(1,div):

        v_impl = solution_euler_implicite(n,new_time,v_impl[0],v_impl[1])

    print("Implicite sans division:",solution_euler_implicite(n,time_total,vx0,vy0))

    print("Implicite avec division :",v_impl)