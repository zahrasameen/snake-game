# Snake Game using Python

import pygame, sys, random, time

check_errors = pygame.init()
if check_errors[1]>0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

#Play Surface
playSurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game!')

#Colors
red = pygame.Color(255,0,0) #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,42,42) #food

#Frames Per Second Controller
fpsController = pygame.time.Clock()

#Important Variables
snakePos = [100,50] #holds coordinates of the snake
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

#Direction
direction = 'RIGHT'
changeto = direction

score = 0

#GameOver Function
def gameOver():
    myFont = pygame.font.SysFont('monaco',72)
    GOsurf = myFont.render('Game Over!',True,red) #True will make it Antisallion.
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf,GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit() #for pygame exit
    sys.exit() #for console exit
    
#Score Function
def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco',26)
    Ssurf = sFont.render('Score : {0}'.format(score), True, white)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80,10) 
    else:
        Srect.midtop = (360,120)
    playSurface.blit(Ssurf,Srect)
    
    
#Real Fun Begins Here!!
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
    #validation of direction  
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
     
    #Snake Position   
    if direction == 'RIGHT':
        snakePos[0] +=10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
        
        
    #Snake body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1 
        foodSpawn = False 
    else:
        snakeBody.pop()
    
    #Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True
    
    #Surface
    playSurface.fill(black)
    
    #Draw Snake 
    for pos in snakeBody:
        pygame.draw.rect(playSurface, brown, pygame.Rect(pos[0],pos[1],10,10)) 
    
    #Draw Food
    pygame.draw.rect(playSurface, green, pygame.Rect(foodPos[0],foodPos[1],10,10))
    
    #GameOver call
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] <0:
        gameOver()
        
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    
    
    showScore()
    pygame.display.flip()
    fpsController.tick(20)
    
    
        
    
        
        






  
