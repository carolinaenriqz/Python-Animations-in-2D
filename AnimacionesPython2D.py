#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Distintas opciones para pintar en python

Se aplica como ejemplo a la funcion u(t,x) = sin(x-ct)*exp(-alpha*t)
"""

from pylab import *


# Esto solo hace falta para a opción pintar4
import matplotlib.animation as animation

def onda(t,x,c,alpha):
    '''
    Definimos aquí la función que vamos a utilizar para pintar

    Parameters
    ----------
    t : float
        variable tiempo
    x : float / array
        variable espacio
    c : float
        velocidad de la onda
    alpha : float
        parámetro de amortiguación

    Returns
    -------
    float / array
        valor de la función u(t,x)

    '''
    return sin(x-c*t)*exp(-alpha*t)


def pintar1(L,T,Nx,Nt,c,alpha):
    '''
    Opción básica de pintado    

    Parameters
    ----------
    L : float
        punto final el intervalo
    T : float
        tiempo final para pintar
    Nx : int
        División espacial (Nx+1 puntos)
    Nt : int
        División temporal (Nt+1 puntos)

    Returns
    -------
    None.

    '''
    tpausa = 0.05 # tiempo de pausa entre un dibujo y el siguiente
    npintar = 1 # cada cuantas iteraciones se pinta
    
    dx = L/float(Nx)
    x = arange(0,L+dx,dx) # ponemos L+dx para que incluya el último punto
    # Otra opción equivalente sería
    # x = linspace(0,L,Nx+1)
    
    dt = T/float(Nt)
    
    for n in range(0,Nt+1):
        t = n*dt
        u = onda(t,x,c,alpha)
        if mod(n,npintar) == 0:
            cla() # limpiamos los ejes
            plot(x,u)
            # fijamos la ventana para que no cambie con el tiempo
            axis([0,L,-1.1,1.1])
            pause(tpausa)
            

def pintar2(L,T,Nx,Nt,c,alpha):
    '''
    Opción básica con control de ejes

    Parameters
    ----------
    L : float
        punto final el intervalo
    T : float
        tiempo final para pintar
    Nx : int
        División espacial (Nx+1 puntos)
    Nt : int
        División temporal (Nt+1 puntos)

    Returns
    -------
    None.

    '''
    tpausa = 0.05 # tiempo de pausa entre un dibujo y el siguiente
    npintar = 1 # cada cuantas iteraciones se pinta
    
    dx = L/float(Nx)
    x = arange(0,L+dx,dx) # ponemos L+dx para que incluya el último punto
    # Otra opción equivalente sería
    # x = linspace(0,L,Nx+1)
    
    dt = T/float(Nt)
    
    # Esta opción es útil si queremos manejar varias ventanas 
    # con gráficas diferentes
    
    # creamos una ventana para figuras
    fig = figure()
    # añadimos un eje
    ax = fig.add_subplot(1,1,1)
    
    # a partir de ahora, todas las funciones de pintado se referirán a ese eje
    
    for n in range(0,Nt+1):
        t = n*dt
        u = onda(t,x,c,alpha)
        if mod(n,npintar) == 0:
            ax.cla() # limpiamos los ejes
            ax.plot(x,u)
            # fijamos la ventana para que no cambie con el tiempo
            ax.axis([0,L,-1.1,1.1])
            pause(tpausa)
        

def pintar3(L,T,Nx,Nt,c,alpha):
    '''
    Opción más avanzada sin borrar ejes

    Parameters
    ----------
    L : float
        punto final el intervalo
    T : float
        tiempo final para pintar
    Nx : int
        División espacial (Nx+1 puntos)
    Nt : int
        División temporal (Nt+1 puntos)

    Returns
    -------
    None.

    '''
    tpausa = 0.05 # tiempo de pausa entre un dibujo y el siguiente
    npintar = 1 # cada cuantas iteraciones se pinta
    
    dx = L/float(Nx)
    x = arange(0,L+dx,dx) # ponemos L+dx para que incluya el último punto
    # Otra opción equivalente sería
    # x = linspace(0,L,Nx+1)
    
    dt = T/float(Nt)
    
    # Esta opción es útil si queremos manejar varias ventanas 
    # con gráficas diferentes
    
    # creamos una ventana para figuras
    fig = figure()
    # añadimos un eje
    ax = fig.add_subplot(1,1,1)
    
    # a partir de ahora, todas las funciones de pintado se referirán a ese eje
    
    # pintamos la iteración cero
    
    t = 0
    u = onda(t,x,c,alpha)
    
    # guardamos en la variable líneas una lista con los dibujos de los ejes
    
    lineas = ax.plot(x,u)
    ax.axis([0,L,-1.1,1.1])
    pause(tpausa) 
    
    
    print('La variable lineas: ')
    print(lineas)
    
    # en este caso solo tengo 1 dibujo que corresponde a la gráfica de la onda
    dibujo_onda = lineas[0]
   
    
    for n in range(1,Nt+1):
        t = n*dt
        u = onda(t,x,c,alpha)
        if mod(n,npintar) == 0:
            # Ahora, en lugar de borrar y pintar todo
            # solo cambio las ordenadas (eje y) de la línea
            dibujo_onda.set_ydata(u)
            pause(tpausa)    
    
    
# Opción más avanzada usando animation de matplotlib
# Esto permitiría incluso generar películas en formato mp4

# definimos la opción que controla la actualización de la animación

def animate(n,dt,x,c,alpha,dibujo_onda):
    t = n*dt
    u = onda(t,x,c,alpha)
    dibujo_onda.set_ydata(u)
    print('Funcion animate llamada con n=%d'%n)
    return dibujo_onda,
    
def pintar4(L,T,Nx,Nt,c,alpha):
    '''
    Opción más avanzada usando animatation

    Parameters
    ----------
    L : float
        punto final el intervalo
    T : float
        tiempo final para pintar
    Nx : int
        División espacial (Nx+1 puntos)
    Nt : int
        División temporal (Nt+1 puntos)

    Returns
    -------
    FuncAnimation

    '''

    
    dx = L/float(Nx)
    x = arange(0,L+dx,dx) # ponemos L+dx para que incluya el último punto
    # Otra opción equivalente sería
    # x = linspace(0,L,Nx+1)
    
    dt = T/float(Nt)
    
    # Esta opción es útil si queremos manejar varias ventanas 
    # con gráficas diferentes
    
    # creamos una ventana para figuras
    fig = figure()
    # añadimos un eje
    ax = fig.add_subplot(1,1,1)
    
    # a partir de ahora, todas las funciones de pintado se referirán a ese eje
    
    # pintamos la iteración cero
    
    t = 0
    u = onda(t,x,c,alpha)
    
    # guardamos en la variable líneas una lista con los dibujos de los ejes
    # se indica que es una animación
    lineas = ax.plot(x,u,animated=True)
    
    dibujo_onda = lineas[0]
    
    # animation.FuncAnimation directamente hace iteraciones que van desde 0 al valor indicado por frames
    # cada vez que hace una iteración, llama a la función animate que se ha definido
    # a esa función se le pasa el número de iteración y los argumentos dados por fargs
    # interval es el tiempo en milisegundos ente dos frames
    anim = animation.FuncAnimation(fig, animate, fargs=(dt,x,c,alpha,dibujo_onda), frames=Nt+1, interval=200, blit=True, repeat=False)
    return anim
       

if __name__ == "__main__":
    # Parámetros que definen la función
    c = 0.5 # velocidad de la onda
    alpha = 0.05 # amortiguación de la amplitud
    
    L = 4*pi # longitud del intervalo
    T = 50 # tiempo final
    
    Nx = 200 # número de divisiones espaciales
    Nt = 100 # número de divisiones temporales
    
    close() # cerramos las ventanas de figuras de ejecuciones anteriores
    
    pintar1(L,T,Nx,Nt,c,alpha)
    
    #pintar2(L,T,Nx,Nt,c,alpha)
    
    #pintar3(L,T,Nx,Nt,c,alpha)
    
    # Opción pro
    #anim = pintar4(L,T,Nx,Nt,c,alpha)
    
    
    
    
    


