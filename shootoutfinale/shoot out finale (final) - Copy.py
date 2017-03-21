#PowerPuff Boys
#Shootout Finale
#Zane Mahmood, Tanvir Mahtab, Christopher Louis
from gamelib import*
game = Game(832,832,"Shoot Out Finale!")
dude = Image("images\\venom.png",game)
bk = Image("images\\loadingscreen.png",game)
bball = Image("images\\basketball.png",game)
hoop = Image("images\\Basketball_Net.png",game)

song = Sound("logic.wav",1)
point = Sound("point.wav",2)
ouch = Sound("ouch.wav",3)

bball.resizeTo(50,50)
hoop.resizeTo(150,150)
hoop.moveTo(150,150)
hoop.setSpeed(10,60)
dude.resizeTo(175,125)
dude.setSpeed(12,60)


while not game.over:
    game.processInput()
    game.clearBackground()
    bk.draw()
    song.play()
    dude.move("True")
    hoop.move("True")
  
    bball.moveTo(mouse.x, mouse.y)
    
 
    if dude.collidedWith(mouse) and mouse.LeftButton:
        game.score-=1
        ouch.play()
        x = randint(150,650)
        y = randint(150,450)
        dude.moveTo(x,y)
        dude.speed+=10
        dude.resizeBy(+8)



    if hoop.collidedWith(mouse) and mouse.LeftButton:
        game.score+=1
        point.play()
        x = randint(150,650)
        y = randint(150,450)
        hoop.moveTo(x,y)
        hoop.speed+=6
        hoop.resizeBy(-4)
   
   
    
    if game.score>=15:
        game.drawText("YOU WIN THIS ROUND!!!",300,0)
        game.over=True

    if game.score<=-5:
        game.drawText("GAME OVER! YOU! LOSE!",300,0)
        game.over=True

    game.displayScore()
    game.update(20)
game.wait(K_SPACE)
game.quit()
  

