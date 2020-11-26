import pygame
import random
import time
from pygame import mixer
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

level_one = True
level_two = False
nextLevel = False

a = random.randint(0,255)
b = random.randint(0,255)
c = random.randint(0,255)
randomColour = (a,b,c)

font_name = pygame.font.match_font('calibri')
 
pygame.init()

freeSpaces = []

x_speed = 0
y_speed = 0
# Set the width and height of the screen [width, height]
size = (800, 500) # y,x
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

map_one = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


map_two = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spongebob.jpg')
        #self.image = pygame.Surface((40,40))
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect() # rect helps with collisions
        self.rect.x = 250
        self.rect.y = 250
        self.health = 100
        self.money = 0
        self.keys = 0
        self.score = 0
        #self.rect.x = 120 # x coordinate
        #self.rect.y = 120 # y coordinate
        #self.movement = 0
            
    def update(self):
        player.rect.x += x_speed
        player.rect.y += y_speed
        if player.rect.x < 20:
            player.rect.x = 20
        if player.rect.x > 440:
            player.rect.x = 440
        if player.rect.y < 20:
            player.rect.y = 20
        if player.rect.y > 440:
            player.rect.y = 440

    def playerStats(self):
        font = pygame.font.Font(font_name, 30)
        healthStats = font.render('Health: ' + str(self.health),True,BLACK)
        screen.blit(healthStats, (550,100))
        moneyStats = font.render('Money: ' + str(self.money),True,BLACK)
        screen.blit(moneyStats, (550,150))
        keysStats = font.render('Keys: ' + str(self.keys),True,BLACK)
        screen.blit(keysStats, (550,200))
        scoreStats = font.render('Score: ' + str(self.score),True,BLACK)
        screen.blit(scoreStats, (550,250))
        #text = font.render(str(int(self.rect.y/40))+" "+str(int(self.rect.x/40)),True,BLACK)
        #text_rect = text.get_rect()
        #text_rect.center=(self.rect.x+20,self.rect.y+20)
        #screen.blit(stats, text_rect)
    

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect = self.image.get_rect() # rect helps with collisions
        self.rect.y = y # y coordinate
        self.rect.x = x # x coordinate
        
class Wall2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(RED)
        self.rect = self.image.get_rect() # rect helps with collisions
        self.rect.y = y # y coordinate
        self.rect.x = x # x coordinate

class Portal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('krabbypatty.png')
        #self.image = pygame.Surface((40,40))
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        e = random.randint(1,3)
        if e == 1:
            self.image = pygame.image.load('moustacheEnemy.png')
        elif e == 2:
            self.image = pygame.image.load('supervillainEnemy.jpg')
        else:
            self.image = pygame.image.load('plankton.jpg')
        #self.image = pygame.Surface((40,40))
        #self.image.fill(randomColour)
        self.rect = self.image.get_rect() # rect helps with collisions
        #self.rect.x = random.randint(20,440)
        #self.rect.y = random.randint(20,440)        
        self.rect.x = x
        self.rect.y = y        

class PowerUps(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('question mark.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 400


def timer():
    clock = pygame.time.Clock()

    frame_count = 0
    start_time = 30
    font = pygame.font.Font(font_name, 30)

    total_seconds = start_time - (frame_count // 60)
    if total_seconds < 0:
        total_seconds = 0

    minutes = total_seconds // 60

    seconds = total_seconds % 60

    thetime = 'Time left - ' + str(minutes) + ' : ' + str(seconds)

    text = font.render(thetime, True, BLACK)

    screen.blit(text, [550, 400])

    frame_count += 1

    clock.tick(60)
    pygame.display.flip()

mysteryHealth = PowerUps()
powerUps_list = pygame.sprite.Group()
powerUps_list.add(mysteryHealth)
portal = Portal()
portal_list = pygame.sprite.Group()
portal_list.add(portal)
all_sprites_list = pygame.sprite.Group() # group for all objects
player = Player() # object for player class
all_sprites_list.add(player)
walls_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group()

for y in range(25):
    for x in range(25):
        # creates walls on the map
        if map_one[y][x] == 1:
            wall = Wall(x*20,y*20)
            all_sprites_list.add(wall)
            walls_list.add(wall)
        else:
            freeSpaces.append([x,y])
            
for i in range(4):
    #enemy = Enemy()
    pos = random.randint(0, len(freeSpaces)-1)
    a = freeSpaces[pos]
    b = a[0]
    c = a[1]
    enemy = Enemy(b*20,c*20)
    all_sprites_list.add(enemy)
    enemies_list.add(enemy)


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates

displayProceedMessage = False

mixer.music.load('intro.wav')
if not done:
    mixer.music.play(-1)


# -------- Main Program Loop -----------
while not done:
    #timer()
    # --- Main event loop
    for event in pygame.event.get():
        if level_one:
            if event.type == pygame.QUIT:
                done = True
 
            # --- Game logic should go here

            # User pressed down on a key
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                
                if event.key == pygame.K_LEFT:
                    x_speed = -3
                    #player.rect.x = player.rect.x + player.movement
                elif event.key == pygame.K_RIGHT:
                    x_speed = 3
                    
                    #player.rect.x = player.rect.x + player.movement
                elif event.key == pygame.K_UP:
                    y_speed = -3
                    
                    #player.rect.y = player.rect.y + player.movement
                elif event.key == pygame.K_DOWN:
                    y_speed = 3
                    
                    #player.rect.y = player.rect.y + player.movement
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        x_speed = 0
                        
                        #player.rect.x = player.rect.x + player.movement
                    elif event.key == pygame.K_RIGHT:
                        x_speed = 0
                        
                        #player.rect.x = player.rect.x + player.movement
                    elif event.key == pygame.K_UP:
                        y_speed = 0

                        #player.rect.y = player.rect.y + player.movement
                    elif event.key == pygame.K_DOWN:
                        y_speed = 0

        elif level_two:
            # User pressed down on a key
            if event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed.
                
                if event.key == pygame.K_LEFT:
                    x_speed = -10
                    #player.rect.x = player.rect.x + player.movement
                elif event.key == pygame.K_RIGHT:
                    x_speed = 10
                    
                    #player.rect.x = player.rect.x + player.movement
                elif event.key == pygame.K_UP:
                    y_speed = -10
                    
                    #player.rect.y = player.rect.y + player.movement
                elif event.key == pygame.K_DOWN:
                    y_speed = 10
                    
                    #player.rect.y = player.rect.y + player.movement
            elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        x_speed = 0
                        
                        #player.rect.x = player.rect.x + player.movement
                    elif event.key == pygame.K_RIGHT:
                        x_speed = 0
                        
                        #player.rect.x = player.rect.x + player.movement
                    elif event.key == pygame.K_UP:
                        y_speed = 0

                        #player.rect.y = player.rect.y + player.movement
                    elif event.key == pygame.K_DOWN:
                        y_speed = 0

    if level_one:
        player.update()
        newFont = pygame.font.SysFont(font_name, 50)
        losingMessage = newFont.render('GAME OVER',True,RED)
        winningMessage = newFont.render('PROCEED',True,GREEN)
        enemyHit = pygame.sprite.spritecollide(player,enemies_list,True) # checks if any enemy hit player. True/False deletes enemy if True
        damage = random.randint(1,20)
        
        mystery = pygame.sprite.spritecollide(player,powerUps_list,True)
        xyz = random.randint(0,9)
        if xyz in (1,2,3):
            powerUps_list.draw(screen)

        if mystery:
            player.health = random.randint(1,100)
        
        if enemyHit:
            player.health = player.health - damage
            if player.health <= 0:
                player.health = 0
                screen.blit(losingMessage,(550,300))
                pygame.display.update()
                time.sleep(5)
                done = True
            else:
                player.keys = player.keys + 1
                player.score = player.score + 100
                if player.keys == 4:
                    displayProceedMessage = True

        portalHit = pygame.sprite.spritecollide(player,portal_list,False)
        if displayProceedMessage:
            screen.blit(winningMessage,(550,300))
            portal_list.draw(screen)
            if portalHit:
                level_one = False
                nextLevel = True

    if nextLevel:
        freeSpaces = []
        level_two = True
        displayProceedMessage = False
        player.health = 100
        player.keys = 0
        player.rect.x = 20
        player.rect.y = 20
        player.update()
        mixer.music.load('a-few-moments-later.mp3')
        mixer.music.play()
        time.sleep(3)
        mixer.music.load('Spongebob Best day ever.wav')
        mixer.music.play(-1)
        all_sprites_list.empty()
        all_sprites_list.add(player)
        for y in range(25):
            for x in range(25):
                # creates walls on the map
                if map_two[y][x] == 1:
                    wall = Wall2(x*20,y*20)
                    all_sprites_list.add(wall)
                    walls_list.add(wall)
                    nextLevel = False
                else:
                    freeSpaces.append([x,y])
        for i in range(4):
            #enemy = Enemy()
            pos = random.randint(0, len(freeSpaces)-1)
            a = freeSpaces[pos]
            b = a[0]
            c = a[1]
            enemy = Enemy(b*20,c*20)
            all_sprites_list.add(enemy)
            enemies_list.add(enemy)

        
    if level_two:
        #player.image = pygame.Surface((10,10))
        all_sprites_list.draw(screen)
        newFont = pygame.font.SysFont(font_name, 50)
        losingMessage = newFont.render('GAME OVER',True,RED)
        winningMessage = newFont.render('PROCEED',True,GREEN)
        enemyHit = pygame.sprite.spritecollide(player,enemies_list,True) # checks if any enemy hit player. True/False deletes enemy if True
        damage = random.randint(1,20)
        enemyWall = pygame.sprite.spritecollide(wall,enemies_list,False)
        enemyEnemy = pygame.sprite.spritecollide(enemy,enemies_list,False)
        counter = 0
        
        while enemyWall and enemyEnemy:
            for enemy in enemyWall:
                enemies_list.remove(enemy)
                counter = counter + 1
                
            for enemy in enemyEnemy:
                enemies_list.remove(enemy)
                counter = counter + 1

            for i in range(counter):
                enemies_list.add(enemy)

                
        if enemyHit:
            player.health = player.health - damage
            if player.health <= 0:
                player.health = 0
                screen.blit(losingMessage,(550,300))
                pygame.display.update()
                time.sleep(5)
                done = True
            else:
                player.keys = player.keys + 1
                player.score = player.score + 100
                if player.keys == 4:
                    displayProceedMessage = True
                    

        mazeHit = pygame.sprite.spritecollide(player,walls_list,False)
        if (player.rect.x != 20 or player.rect.y != 20) and mazeHit:
            player.rect.x = 20
            player.rect.y = 20

        portalHit = pygame.sprite.spritecollide(player,portal_list,False)
        if displayProceedMessage:
            screen.blit(winningMessage,(550,300))
            portal_list.draw(screen)
            if portalHit:
                time.sleep(1)
                done = True
        
        
    pygame.display.update()
    
    '''
        # this code is to move the player block by block

        keys = pygame.key.get_pressed()  #checking pressed keys
        if event.type == pygame.K_UP:
                while keys[pygame.KEYDOWN]:
                        player.rect.y = player.rect.y - 20
                        if keys[pygame.K_DOWN]:
                                break
        if event.type == pygame.KEYDOWN:
                if keys[pygame.K_DOWN]:
                        player.rect.y = player.rect.y + 20
        

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.movement = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.movement = 0
    '''
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with bliting the
    # background image.

    
    screen.fill(WHITE)
    if level_one:
        background = pygame.image.load('town.png')
        screen.blit(background,(0,0))
    if level_two:
        background = pygame.image.load('house.png')
        screen.blit(background,(0,0))
    player.playerStats()

    # --- Drawing code should go here
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    
    '''
    for y in range(25):
        for x in range(25):
            text = font.render('hello',True,BLACK)
            screen.blit(text, [y,x])
    '''
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
 
# Close the window and quit.
pygame.quit()
