from time import sleep_ms
from machine import Pin

#define pin de sensores
#derecho
pinD = Pin(11, Pin.IN)
#Izquierdo
pinI = Pin(16, Pin.IN)

#define pin motores
#derecho
pin_motorD1= Pin(33, Pin.OUT)
pin_motorD2 = Pin(35, Pin.OUT)
#izquierdo
pin_motorI1 = Pin(37, Pin.OUT)
pin_motorI2 = Pin(39, Pin.OUT)

def forward(pin1, pin2):
    pin1.on()
    pin2.off()

def stop(pin1, pin2):
    pin1.off()
    pin2.off()

def der_on():
    forward(pin_motorD1, pin_motorD2)

def izq_on():
    forward(pin_motorI1, pin_motorI2)

def der_off():
    stop(pin_motorD1, pin_motorD2)

def izq_off():
    stop(pin_motorI1, pin_motorI2)

time_rot=150
while(True):
    der = pinD.value()
    if (der == 0):
        der_on()
    else:
        der_off()
    izq = pinI.value()
    if (izq == 0):
        izq_on()
    else:
        izq_off()
    


