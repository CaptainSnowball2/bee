from time import time
import pgzrun
import random
WIDTH=600
HEIGHT=500
start=time()
sat=[]
lines=[]
next=0
for i in range(10):
    s=Actor("cool")
    s.x=random.randint(50,550)
    s.y=random.randint(50,450)
    sat.append(s)
def on_mouse_down(pos):
    global next
    global lines
    if sat[next].collidepoint(pos):
        if next>0:
            lines.append((sat[next-1].pos,sat[next].pos))
            print(lines)
    
        next+=1
    else:
        lines=[]
        next=0
def update():
    pass
def draw():
    nummber=1
    global total
    global lines

    screen.blit("space",(0,0))
    for a in sat:
        a.draw()
        screen.draw.text(str(nummber),(a.x,a.y),color="red")
        nummber+=1
    for l in lines:
        screen.draw.line(l[0],l[1],"red")
    if next < 10:
        total=time()-start
        screen.draw.text(str(round(total,0)),(400,5))
    else:
        #screen.fill("black")
        screen.draw.text(str(total),(400,5))
        for i in sat:
            i.x=1000000
            i.y=1000000
        lines=[]

        
pgzrun.go()