def etoileFond(v):
    posx=random(1,800)
    posy=random(1,t-45)
    tailleEtoile= random(0.7,3)
    stroke(200)
    strokeWeight(random(0.1,0.6))
    line(posx-tailleEtoile,posy-tailleEtoile,posx,posy)
    line(posx+tailleEtoile,posy-tailleEtoile,posx,posy)
    line(posx-tailleEtoile,posy+tailleEtoile,posx,posy)
    line(posx+tailleEtoile,posy+tailleEtoile,posx,posy)
    line(posx+tailleEtoile+v,posy,posx,posy)
    line(posx-tailleEtoile-v,posy,posx,posy)
    line(posx,posy+tailleEtoile+v,posx,posy)
    line(posx,posy-tailleEtoile-v,posx,posy)

def fondPasBouge():
    global t,h
    x=10
    z=10
    v=10
    
    #t permet de faire bouger vers le bas l atmosphere car il active plus les conditions de latmosphere
    t=t+2
    # a chaque frame augmente, baissant petit à petit le fond
    h=h+0.0009
    for i in range (0,800):
        #degrade lent
        if (i<=t):
            noStroke()
            fill(20,20,v)
            bezier(0,i,200,i-150,600,i-100,800,i)
            v=v+0.3-h
        #debut de latmospher
        if (i<=700 and i>t-10):
            fill(x,z,v)
            bezier(0,i,200,i-100,600,i-100,800,i)
            v=v+0.9
            x=x+0.9
            z=z+1.5
        #fin de l'atmosphere
        if (i<=800 and i>t+35):
            fill(x,z,v)
            bezier(0,i,200,i-100,600,i-100,800,i)
            v=v+2.5
            x=x+2.5
            z=z+2.5



def menuBouton(): 
    #importation des variables globales
    global bJouer, menuAffiche
    #chagement de l'allignement de l'image
    imageMode(CENTER)
    #affichage de l'image
    image(bJouer, 400,450)
    if mouseX >= 340 and mouseX <= 460 and mouseY >= 430 and mouseY < 476:
        fill(255, 100)
    else: 
        fill(255, 0)
    noStroke()
    rect(345,427,115,46)
    rect(340,427,5,40)
    triangle(340, 467, 345, 467, 345, 473)
    if (mouseX >= 340 and mouseX <= 460 and mouseY >= 430 and mouseY < 476) and (mousePressed and (mouseButton == LEFT)):
        menuAffiche = 0
    
def menuLogo():
    #importation des variables globales
    global bLogo, posLogo
    imageMode(CORNER)
    image(bLogo, 210, posLogo)



def setup():
    #importation des variables globales
    global bLogo, bJouer, menuAffiche, t, h, posLogo
    #mise en place de la taille de l'écran    
    size(800,600)
    #importation des images
    bLogo = loadImage("spaceInvadersLogo.png")
    bJouer = loadImage("boutonJouer.png")
    #mise en place des variables
    menuAffiche = 1
    posLogo = -80
    t=540
    h=0
    #mise en place du framerate du jeu
    frameRate(30)
    
    
def draw ():
    #importation des variables globales
    global t, h, menuAffiche, posLogo
    noStroke()
    fondPasBouge()
    #appel de la fonction "etoileFond()"
    for i in range (1,90):
        etoileFond(random(0.1,0.6))
    #modification de la variable "t"
    #affichage du menu si la variable "menuAffiche" = 1 
    if (menuAffiche == 1):
        menuLogo()
        if posLogo < 90: 
            posLogo += 5
        if posLogo == 90: 
            menuBouton()
