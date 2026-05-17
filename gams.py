import pgzrun
import time

HEIGHT = 450
WIDTH = 650

galaga = Actor("galaga")
galaga.pos = (325,400)
bugs = []
bulletstr = []
bugstr = []
x = 80
y = 50
cooldown = 1
lastshot = 0
direction = 1
gameover = False
for o in range(4):
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
    if gameover == True:
        screen.fill("#FFEC5D")
        screen.draw.text("YOU WIN", (225,325), color="white", fontsize = 100)

def update():
    global direction, score, gameover
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
            if bullet.colliderect(bug):
                bulletstr.append(bullet)
                bugstr.append(bug)
                score += 1
    for bullet in bulletstr:
        if bullet in bullets:
            bullets.remove(bullet)
    for bug in bugstr:
        if bug in bugs: 
            bugs.remove(bug)
    for bug in bugs:
        bug.x += 1 * direction
        if bugs[-1].x > 625:
            direction = -1
            for bug in bugs:
                bug.y += 2.5 
        if bugs[0].x < 25:
            direction = 1
            for bug in bugs:
                bug.y += 2.5
    if score == 16:
        gameover = True

def on_key_down(key):
    global lastshot
    currentime = time.time()
    if key == keys.SPACE:
        if currentime - lastshot > cooldown:
            bullet = Actor("bullet")
            bullet.pos = (galaga.x, galaga.y)
            bullets.append(bullet)
            lastshot = currentime

pgzrun.go()