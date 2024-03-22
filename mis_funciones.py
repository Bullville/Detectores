import numpy as np 
import pandas as pd
import random
import matplotlib.pyplot as plt 


def angulos_iniciales(thetamax, phimax = 0):
    '''
    Función para generar los angulos iniciales desde el origen de coordenadas, prefijamos el angulo phi en 
    0 para trabajar en el plano YZ hasta que funcione bien la cosa
    '''
    
    theta_inicial = random.uniform(-thetamax,thetamax)
    phi_inicial = random.uniform(0,phimax)
    return theta_inicial, phi_inicial

def coor_inc_material(theta, phi, distancia_fuente_material):
    '''
    Coordenadas del punto de incidencia en el material. 

    theta: ángulo theta de la trayectoria inicial
    phi: ángulo phi de la trayectoria inicial 
    distancia_fuente_material: distancia entre la fuente de fotones y el material absorbente 

    En esta primera interacción los ángulos no cambian
    '''

    costheta = np.cos(theta)
    sentheta = np.sqrt(1-costheta**2)
    tantheta = sentheta/costheta

    z = distancia_fuente_material
    x = z * tantheta * np.cos(phi)
    y = z * tantheta * np.sin(phi)

    return x, y, z

def recorrido_libre_medio(a):
    '''
    Recorrido libre medio de un fotón dentro de un material con un coeficiente de atenuación a. Es equivalente 
    a decir que es la distancia que recorre un fotón hasta interaccionar

    a: coeficiente de atenuación
    '''

    x = -1/(a * np.log(random.random()))
    return x

def coordenadas_material(z_0, theta_0, phi_0, recorrido_libre_medio):
    '''
    Función para cambiar la trayectoria del fotón

    x_0: coordenada x
    y_0: coordenada y
    z_0: coordenada z
    theta_0: angulo plano ZY
    phi_0: angulo de revolución
    recorrido_libre_medio: modulo de la distancia recorrida dentro del material antes de interaccionar
    '''
    theta_nueva = -theta_0
    phi_nuevo = -phi_0

    sentheta = np.sin(theta_nueva)
    costheta = np.cos(theta_nueva)
    z_nuevo = z_0 + recorrido_libre_medio * costheta
    x_nuevo = recorrido_libre_medio * sentheta * np.cos(phi_nuevo)
    y_nuevo = recorrido_libre_medio * sentheta * np.sin(phi_nuevo)

    return x_nuevo, y_nuevo, z_nuevo, theta_nueva, phi_nuevo