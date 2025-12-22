import pgzrun
import random
WIDTH=600
HEIGHT=500
R=random.randint(50,550)
A=random.randint(50,450)
B=Actor("bee")
F=Actor("flower")
B.x=300
B.y=250
F.x=R
F.y=A
def draw():
    screen.blit("background",(0,0))
    B.draw()
    F.draw()

def update():
    if keyboard.w:
        B.y = B.y - 2
    if keyboard.a:
        B.x = B.x - 2
    if keyboard.s:
         B.y = B.y + 2      
    if keyboard.d:
         B.x = B.x + 2  
pgzrun.go()