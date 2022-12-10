def etoileFond():
    smooth()
    fill(random(200,255))
    #La troisimèe variable c'est l'épaisseur des traits, la quatrième la longueur
    rect(random(1,800),random(1,t-45),random(0.2,0.5),random(1,5))

def fondPasBouge():
    x=10
    z=10
    v=10
    global t
    for i in range (0,700):
        if (i<=t):
            noStroke()
            fill(10,10,v)
            bezier(0,i,100,i-150,350,i-100,800,i)
            v=v+0.2
        if (i<=520 and i>t-10):
            fill(x,z,v)
            bezier(0,i,100,i-100,350,i-100,800,i)
            v=v+0.7
            x=x+0.7
            z=z+0.9
        if (i<=540 and i>t+20):
            fill(x,z,v)
            bezier(0,i,100,i-100,350,i-100,800,i)
            v=v+2
            x=x+2
            z=z+3

def menuBouton(): 
    global bJouer, menuAffiche
    imageMode(CENTER)
    image(bJouer, 400,450)
    if mouseX >= 340 and mouseX <= 460 and mouseY >= 430 and mouseY < 476:
        fill(255, 100)
    else: 
        fill(255, 0)
    rect(340,430,120,46)
    if (mouseX >= 340 and mouseX <= 460 and mouseY >= 430 and mouseY < 476) and (mousePressed and (mouseButton == LEFT)):
        menuAffiche = 0
    
def menuLogo():
    global bLogo, posLogo
    imageMode(CORNER)
    image(bLogo, 210, posLogo)

def setup():
    global bLogo, bJouer, menuAffiche, t, posLogo
    bLogo = loadImage("spaceInvadersLogo.png")
    bJouer = loadImage("boutonJouer.png")
    menuAffiche = 1
    posLogo = -80
    t=600
    frameRate(60)
    size(800,600)
    
    
def draw ():
    global t, menuAffiche, posLogo
    noStroke()
    fondPasBouge()
    for i in range (1,40):
        etoileFond()
    t=t+0.3
    if (menuAffiche == 1):
        menuLogo()
        if posLogo < 90: 
            posLogo += 5
        if posLogo == 90: 
            menuBouton()
