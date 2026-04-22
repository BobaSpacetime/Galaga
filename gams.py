import pgzrun

HEIGHT = 450
WIDTH = 650

galaga = Actor("galaga")
galaga.pos = (325,400)
bullets = []
def draw():
    screen.fill("#001787")
    galaga.draw()
    for bullet in bullets:
        bullet.draw()

def update():
    if keyboard.left: 
        galaga.x-=10
        if galaga.x<50:
            galaga.x=50
    if keyboard.right:
        galaga.x+=10
        if galaga.x>600:
            galaga.x=600

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.pos = (galaga.x, galaga.y)
        bullets.append(bullet)


pgzrun.go()