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
Score=0
GameOver=False
def draw():
    screen.blit("background",(0,0))
    B.draw()
    F.draw()
    screen.draw.text("score: "+str(Score),(515,20))
    if GameOver==True:
        screen.fill("black")
        screen.draw.text("GameOver",(300,250))
        screen.draw.text("Score: "+str(Score),(300,300))

def update():
    global Score
    if keyboard.w:
        B.y = B.y - 2
    if keyboard.a:
        B.x = B.x - 2
    if keyboard.s:
         B.y = B.y + 2      
    if keyboard.d:
         B.x = B.x + 2  
    if B.colliderect(F):
        Score+=1
        F.x=random.randint(55,550)
        F.y=random.randint(50,450)

def timer():
    global GameOver
    GameOver=True
clock.schedule(timer, 10.0)

pgzrun.go()