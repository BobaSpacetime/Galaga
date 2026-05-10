import pgzrun

HEIGHT = 450
WIDTH = 650

galaga = Actor("galaga")
galaga.pos = (325,400)
bugs = []
x = 80
y = 50
direction = 1
for o in range(3):
    for i in range(4):
        bug = Actor("bug")
        bug.pos = (x,y)
        bugs.append(bug)
        x += 50
    x -= 200
    y += 40
bullets = []
score = 0
def draw():
    screen.fill("#001787")
    galaga.draw()
    for bug in bugs:
        bug.draw()
    screen.draw.text("Score: " + str(score), (10,10), color="white")
    for bullet in bullets:
        bullet.draw()

def update():
    global direction
    if keyboard.left: 
        galaga.x-=10
        if galaga.x<50:
            galaga.x=50
    if keyboard.right:
        galaga.x+=10
        if galaga.x>600:
            galaga.x=600
    for bullet in bullets:
        bullet.y -= 5
        if bullet.y < 0: 
            bullets.remove(bullet)
    for bug in bugs:
        bug.x += 1*direction
        if bugs[-1].x > 650:
            direction = -1
        if bugs[0].x < 0:
            direction = 1


        
    

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.pos = (galaga.x, galaga.y)
        bullets.append(bullet)


pgzrun.go()