import pgzrun
import random
WIDTH=600
HEIGHT=500
R=random.randint(50,550)
A=random.randint(50,450)
Sp=Actor("spider")
S=Actor("hmmmm")
Sp.x=300
Sp.y=250
S.x=R
S.y=A
Score=0
GameOver=False
Win=False
def draw():
    screen.blit("al",(0,0))
    Sp.draw()
    S.draw()
    screen.draw.text("score: "+str(Score),(515,20))
    if GameOver==True:        
        screen.fill("black")
        screen.draw.text("GameOver",(300,250))
        screen.draw.text("Score: "+str(Score),(300,300))
    if Win ==True:
        screen.fill("black")
        screen.blit("win",(70,0))
        screen.draw.text("Score: "+str(Score),(300,300))
def update():
    global Score
    if keyboard.w:
        Sp.y = Sp.y - 2
    if keyboard.a:
        Sp.x = Sp.x - 2
    if keyboard.s:
         Sp.y = Sp.y + 2      
    if keyboard.d:
         Sp.x = Sp.x + 2  
    if S.colliderect(Sp):
        Score+=1
        
            
        S.x=random.randint(55,550)
        S.y=random.randint(50,450)

def timer():
    global GameOver
    global Win
    GameOver=True
    if Score >1:  
        Win=True
clock.schedule(timer, 10.0)

pgzrun.go()