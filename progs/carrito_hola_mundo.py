'''
Realiza el movimiento de un carrito de 2 motores.
se mueve al frente y rota 4 veces por el mismo tiempo,
de manera ideal dibuja un cuadrado, pero dependerá que el tiempo de giro corresponda con 90 grados

Autor: Miguel Angel Robles
'''
from machine import Pin
from time import sleep_ms

#definición de pines
A1= Pin(33, Pin.OUT)
A2= Pin(35, Pin.OUT)
B1= Pin(37, Pin.OUT)
B2= Pin(39, Pin.OUT)

#funciones de movimientos
def frente():
    A1.on()
    A2.off()
    B1.on()
    B2.off()

def der():
    A1.on()
    A2.off()
    B1.off()
    B2.off()

def izq():
    A1.off()
    A2.off()
    B1.on()
    B2.off()

def frente():
    A1.on()
    A2.off()
    B1.on()
    B2.off()

def alto():
    A1.off()
    A2.off()
    B1.off()
    B2.off()

#tiempo moviendo al frente
time_run = 1200
#tiempo rotando
time_rt = 600

#secuencia de movimientos
frente()
sleep_ms(time_run)
der()
sleep_ms(time_rt)

frente()
sleep_ms(time_run)
der()
sleep_ms(time_rt)

frente()
sleep_ms(time_run)
der()
sleep_ms(time_rt)

frente()
sleep_ms(time_run)
der()
sleep_ms(time_rt)

alto()
