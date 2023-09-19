from machine import Pin
import car_robo as car

A1= Pin(33, Pin.OUT)
A2= Pin(35, Pin.OUT)
B1= Pin(37, Pin.OUT)
B2= Pin(39, Pin.OUT)

t= 1000

car.frente(A1,A2,B1,B2,t)
car.rev(A1,A2,B1,B2,t)
car.alto(A1,A2,B1,B2,t)
car.derecha(A1,A2,B1,B2,t)
car.izquierda(A1,A2,B1,B2,t)
