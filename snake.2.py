import turtle
import time
import random

posponer = 0,1

score = 0
high_score = 0

#cabeza
wn  = turtle.Screen()
wn.title("Juego de la serpiente")
wn.bgcolor("orange")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cabesita
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#funciones de la serp
def arriba():
    cabeza.direction = "up"

def abajo(): 
    cabeza.direction = "down"

def izquierda(): 
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"
    




def mov():

    
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.sety(y + 20)

while True:
    wn.update()

    mov()
    time.sleep(posponer)


