#Import all needed modules
import pygame
import random
import os
import ctypes
import sys

#Setting resolution and frame rate
WIDTH = 600
HEIGHT = 480
FPS = 60

#assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "assets")

#Initialisation of pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("RPG")  
clock = pygame.time.Clock()
pygame.key.set_repeat(1000)

#Screen Drawing
font_name = pygame.font.match_font("courier")
def screen_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def battle_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def name_text(surf, text, size, x, y, colour):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

                            
#This Is Where All Game Graphics Are Loaded

#Title Screen Sprites
title = pygame.image.load(os.path.join(img_folder, "title.bmp")).convert_alpha()

#Load Map Sprites
item_tile = pygame.image.load(os.path.join(img_folder, "item.bmp")).convert_alpha()
stairs_tile = pygame.image.load(os.path.join(img_folder, "stairs.bmp")).convert_alpha()
background = pygame.image.load(os.path.join(img_folder, "background.bmp")).convert_alpha()

#Wall Sprites
wall1 = pygame.image.load(os.path.join(img_folder, "obstacle1.bmp")).convert_alpha()
wall2 = pygame.image.load(os.path.join(img_folder, "obstacle2.bmp")).convert_alpha()
wall3 = pygame.image.load(os.path.join(img_folder, "obstacle3.bmp")).convert_alpha()

#Load Character sprites
#Knight
knight_left = pygame.image.load(os.path.join(img_folder,"knight_left.bmp")).convert_alpha()
knight_up = pygame.image.load(os.path.join(img_folder, "knight_up.bmp")).convert_alpha()
knight_down = pygame.image.load(os.path.join(img_folder,"knight_down.bmp")).convert_alpha()
knight_right = pygame.image.load(os.path.join(img_folder, "knight_right.bmp")).convert_alpha()

#Rogue
rogue_left = pygame.image.load(os.path.join(img_folder,"rogue_left.bmp")).convert_alpha()
rogue_up = pygame.image.load(os.path.join(img_folder, "rogue_up.bmp")).convert_alpha()
rogue_down = pygame.image.load(os.path.join(img_folder, "rogue_down.bmp")).convert_alpha()
rogue_right = pygame.image.load(os.path.join(img_folder,"rogue_right.bmp")).convert_alpha()

#Warlock
warlock_left = pygame.image.load(os.path.join(img_folder, "warlock_left.bmp")).convert_alpha()
warlock_up = pygame.image.load(os.path.join(img_folder, "warlock_up.bmp")).convert_alpha()
warlock_down = pygame.image.load(os.path.join(img_folder, "warlock_down.bmp")).convert_alpha()
warlock_right = pygame.image.load(os.path.join(img_folder, "warlock_right.bmp")).convert_alpha()

#Ranger
ranger_left = pygame.image.load(os.path.join(img_folder, "ranger_left.bmp")).convert_alpha()
ranger_up = pygame.image.load(os.path.join(img_folder, "ranger_up.bmp")).convert_alpha()
ranger_down = pygame.image.load(os.path.join(img_folder, "ranger_down.bmp")).convert_alpha()
ranger_right = pygame.image.load(os.path.join(img_folder, "ranger_right.bmp")).convert_alpha()

#Enemy Sprites
enemy_tile = pygame.image.load(os.path.join(img_folder, "enemy_map.bmp")).convert_alpha()
enemy_battle = pygame.image.load(os.path.join(img_folder, "enemy_battle.bmp")).convert_alpha()

#Battle menu icons
fight = pygame.image.load(os.path.join(img_folder, "fight.bmp")).convert_alpha()
guard = pygame.image.load(os.path.join(img_folder, "shield.bmp")).convert_alpha()
bag = pygame.image.load(os.path.join(img_folder, "bag.bmp")).convert_alpha()
flee = pygame.image.load(os.path.join(img_folder, "run.bmp")).convert_alpha()

#Battle state sprites
select_fight = pygame.image.load(os.path.join(img_folder, "select_fight.bmp")).convert_alpha()
select_guard = pygame.image.load(os.path.join(img_folder, "select_shield.bmp")).convert_alpha()
select_bag = pygame.image.load(os.path.join(img_folder, "select_bag.bmp")).convert_alpha()
select_flee = pygame.image.load(os.path.join(img_folder, "select_run.bmp")).convert_alpha()
battleground = pygame.image.load(os.path.join(img_folder, "battle_background.bmp")).convert_alpha()


#The following will be focussed on the sprites
#Sprite Classes
sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
mobs = pygame.sprite.Group()
items = pygame.sprite.Group()
walls = pygame.sprite.Group()
stairs = pygame.sprite.Group()

#This is the sprite class that the will be obstacles on the map
class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.randint(0,2)
        if self.type == 0:
            self.image = wall1
        if self.type == 1:
            self.image = wall2
        if self.type == 2:
            self.image = wall3

        self.rect = self.image.get_rect()
        self.rect.left = ((random.randint(0, 8)) * 32) + 160
        self.rect.top = ((random.randint(0, 8)) * 32) + 20

    #This part spawns a random number of obstacle tile at random parts of the map
    
    def spawnwalls(Wall):
        number = random.randint(1,8)
        for i in range(number):
            wall = Wall()
            sprites.add(wall)
            walls.add(wall)

wall = Wall()

        
#This is a variable that will be used to stop the player sprite group from colliding with the wall sprite group
get_bump = False

#This is the sprite class that the player will use
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = knight_up
        self.rect = self.image.get_rect()
        self.rect.topleft = (160, 20)


    def update(self):
        #Key inputs
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            self.image = knight_up
            self.rect.y -= 32

        if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
            self.image = knight_down
            self.rect.y += 32

        if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
            self.image = knight_left
            self.rect.x -= 32
                
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.image = knight_right
            self.rect.x += 32

        if get_bump:
            if keystate[pygame.K_w] or keystate[pygame.K_UP]:
                self.rect.y += 64
            if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
                self.rect.y -= 64
            if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
                self.rect.x += 64
            if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
                self.rect.x -= 64


        #Setting borders
        if self.rect.right >= 448:
            self.rect.right = 448
            
        if self.rect.left <= 160:
            self.rect.left = 160
        if self.rect.top <= 20:
            self.rect.top = 20
        if self.rect.bottom >= 340:
            self.rect.bottom = 340
    #Spawns the player sprite onto the grid
    def spawnplayer(Player):
        player = Player()
        sprites.add(player)
        players.add(player)

    
#This is the sprite class that the items will use
class Drop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = item_tile
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.left = ((random.randint(0, 8)) * 32) + 160
        self.rect.top = ((random.randint(0, 8)) * 32) + 20

    #Spawns the item sprite onto the grid
    def spawndrops(Drop):
        item = Drop()
        items.add(item)


#This is the sprite class that the stairs will use
class Exit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = stairs_tile
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left = ((random.randint(0, 8)) * 32) + 160
        self.rect.top = ((random.randint(0, 8)) * 32) + 20

    #Spawns the sprite that refreshes the grid
    def spawnsteps(Exit):
        steps = Exit()
        sprites.add(steps)
        stairs.add(steps)


#This is the sprite class that the enemies will use
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_tile
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left = ((random.randint(0, 8)) * 32) + 160
        self.rect.top = ((random.randint(0, 8)) * 32) + 20

    #Spawns mobs onto the grid
    def spawnmobs(Mob):
        #This line spawns a random number of enemies.
        number = random.randint(1,10)
        for i in range(number):
            enemy = Mob()
            sprites.add(enemy)
            mobs.add(enemy)
    

    def update(self):
        self.direct = random.randint(0,50)
        if self.direct == 0 or self.direct >4:
            self.rect.x += 0
            self.rect.x += 0
        if self.direct == 1:
            self.rect.y += 32
            self.rect.x += 0
        if self.direct == 2:
            self.rect.y += 0
            self.rect.x += 32
        if self.direct == 3:
            self.rect.y -= 32
            self.rect.x -= 0
        if self.direct == 4:
            self.rect.y -= 0
            self.rect.x -= 32
        
        #Setting borders
        if self.rect.right >= 448:
            self.rect.right = 448
        if self.rect.left <= 160:
            self.rect.left = 160
        if self.rect.top <= 20:
            self.rect.top = 20
        if self.rect.bottom >= 340:
            self.rect.bottom = 340

#This is to draw the map grid
def draw_grid(self):
    for x in range(160, 480, 32):
        pygame.draw.line(screen, (100,100,100), (x, 20), (x,340))
    for y in range(20, 372, 32):
        pygame.draw.line(screen, (100,100,100), (160, y), (448, y))

#The next part of the code are what will be used in the battle state. 

#Physical Classes
knight = [1, 125, 75, 100, 150]
rogue = [2, 100, 150, 125, 75]

#Ranged Classes
ranger = [3, 125, 50, 150, 100]
warlock = [4, 175, 100, 75, 100]


#Battle state 
def battle(win, lose, item):

    #The next part of the code are what will be used in the battle state. 

    #Physical Classes
    knight = [1, 125, 75, 100, 150]
    rogue = [2, 100, 150, 125, 75]

    #Ranged Classes
    ranger = [3, 125, 50, 150, 100]
    warlock = [4, 175, 100, 75, 100]


    #Generate enemy stats and pack into array
    hp = random.randint(150,250)
    speed = random.randint(75, 175)
    attack = random.randint(100, 150)
    defence = random.randint(75, 150)
    mon_stats = [0, hp, speed, attack, defence]

    #Pack all character's stats into a 2d array
    act_order = [knight, rogue, ranger, warlock, mon_stats]

    #Declare variables for use
    pos = 0
    text1 = ("")
    text2 = ("")
    text3 = ("The Enemy has:")
    text4 = (str(mon_stats[1]))
    turn = 0
    death = 0
    
    while win == False and lose == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        
        #Sprite update
        screen.blit(battleground, (0,0))
        screen.blit(rogue_right, (237, 220))
        screen.blit(knight_right, (260,250))
        screen.blit(warlock_right, (215,250))
        screen.blit(ranger_right, (237, 270))
        screen.blit(enemy_battle, (345, 200))
        

        #This is what the game will read the HP value from
        knight_hp = str(knight[1])
        rogue_hp = str(rogue[1])
        ranger_hp = str(ranger[1])
        warlock_hp = str(warlock[1])

        #The Names inside the character HP boxes
        battle_text(screen, "Knight", 18, 540, 40)
        battle_text(screen, "Rogue", 18, 538, 150)
        battle_text(screen, "Ranger", 18, 540, 265)
        battle_text(screen, "Warlock", 18, 545, 380)

        #This part makes the hp value appear
        battle_text(screen, knight_hp, 20, 525, 65)
        battle_text(screen, rogue_hp, 20, 525, 175)
        battle_text(screen, ranger_hp, 20, 525, 290)
        battle_text(screen, warlock_hp, 20, 525, 405)

        #The text in the text box
        battle_text(screen, text1, 16, WIDTH /2, HEIGHT * 0.75)
        battle_text(screen, text2, 16, WIDTH /2, HEIGHT * 0.8)
        battle_text(screen, text3, 16, WIDTH /2, HEIGHT * 0.9)
        battle_text(screen, text4, 18, WIDTH /2, HEIGHT * 0.95)

        #Buttons for interacting with the battle state
        screen.blit(fight, (15,50))
        screen.blit(guard, (15,134))
        screen.blit(bag, (15,218))
        screen.blit(flee, (15,302))

        #Selection
        if pos == 0:
            screen.blit(select_fight, (15,50))
            text1 = ("Attack the enemy")
        if pos == 1:
            screen.blit(select_guard, (15,134))
            text1 = ("Reduce the damage taken")
        if pos == 2:
            screen.blit(select_bag, (15,218))
            text1 = ("Look in the bag")
        if pos == 3:
            screen.blit(select_flee, (15,302))
            text1 = ("Run away")

        pygame.display.flip()

        keypress = pygame.key.get_pressed()

        #Rounds the enemy's hp value. A string copy is assigned to the 4th line of the text box.
        mon_stats[1] = round(mon_stats[1])
        text4 = (str(mon_stats[1]))

        #Sorting act_order by the speed value
        act_order.sort(reverse = True, key = lambda x: x[2])

        #The HP text for party members
        battle_text(screen, str(act_order[1][1]), 18, 520, 20)

        #Battle menu selector
        if keypress[pygame.K_UP] or keypress[pygame.K_w]:
            pos -= 1
            if pos < 0:
                pos = 3
        if keypress[pygame.K_DOWN] or keypress[pygame.K_s]:
            pos += 1
            if pos > 3:
                pos = 0
        
        #Ensures turn counter is an integer
        turn = round(turn,0)
        
        hp = str(act_order[turn][1])

        if turn == 6:
            turn = 0
            
        if turn >= 0 and turn <= 5:
            #Class 5 is for the dead player characters
            if act_order[turn][0] == 5:
                text2 = ("This character is dead")
                turn += 1

            #Warlock's turn
            if act_order[turn][0] == 4:
                text2 = str(("Warlock's Turn. HP:", hp))
                if keypress[pygame.K_p] or keypress[pygame.K_RETURN]:
                    if pos == 0:
                        mon_stats[1] -= ((act_order[turn][3] * 100)/mon_stats[4])
                        if mon_stats[1] <= 0:
                            win = True
                    if pos == 1:
                        act_order[turn][4] *= 2
                    if pos == 2:
                        act_order[turn][1] += 125
                        item -= 1
                    if pos == 3:
                        chance = random.randint(0,4)
                        if chance == 0:
                            lose = True
                            win = True
                    turn += 1
                    if turn > 5:
                        turn = 0

            #Ranger's turn
            if act_order[turn][0] == 3:
                text2 = str(("Ranger's Turn. HP:", hp))
                if keypress[pygame.K_p] or keypress[pygame.K_RETURN]:
                    if pos == 0:
                        mon_stats[1] -= ((act_order[turn][3] * 100)/mon_stats[4])
                        if mon_stats[1] <= 0:
                            win = True
                    if pos == 1:
                        act_order[turn][4] *= 2
                    if pos == 2:
                        act_order[turn][1] += 125
                        item -= 1
                    if pos == 3:
                        chance = random.randint(0,4)
                        if chance == 0:
                            lose = True
                            win = True
                    turn += 1
                    if turn > 5:
                        turn = 0

            #Rogue's turn
            if act_order[turn][0] == 2:
                text2 = str(("Rogue's Turn. HP:", hp))
                if keypress[pygame.K_p] or keypress[pygame.K_RETURN]:
                    if pos == 0:
                        mon_stats[1] -= ((act_order[turn][3] * 100)/mon_stats[4])
                        if mon_stats[1] <= 0:
                            win = True
                    if pos == 1:
                        act_order[turn][4] *= 2
                    if pos == 2:
                        act_order[turn][1] += 100
                    if pos == 3:
                        chance = random.randint(0,4)
                        if chance == 0:
                            lose = True
                            win = True
                    turn += 1
                    if turn > 5:
                        turn = 0

            #Knight's turn
            if act_order[turn][0] == 1:
                text2 = str(("Knight's Turn. HP:", hp))
                if keypress[pygame.K_p] or keypress[pygame.K_RETURN]:
                    if pos == 0:
                        mon_stats[1] -= ((act_order[turn][3] * 100)/mon_stats[4])
                        if mon_stats[1] <= 0:
                            win = True
                    if pos == 1:
                        act_order[turn][4] *= 2
                    if pos == 2:
                        act_order[turn][1] += 100
                    if pos == 3:
                        chance = random.randint(0,4)
                        if chance == 0:
                            lose = True
                            win = True
                    turn += 1
                    if turn > 5:
                        turn = 0

            #Class 0 is for the enemy
            if act_order[turn][0] == 0:
                text2 = str(("Enemy's Turn"))
                target = random.randint(1,4)
                act_order[target][1] -= ((mon_stats[3] *100)/ act_order[target][4])
                act_order[target][1] = round(act_order[target][1], 0)
                turn += 1
                if turn > 5:
                    turn = 0
                else:
                    #A character has died
                    if act_order[target][1] <= 0:
                        print("Ally is dead")
                        act_order[target][1] = 0
                        act_order[target][0] = 5
                        death += 1
                        
                        if death == 4:
                            lose = True
                            win == False

        if win == True and lose == False:
            return ()
        if lose == True and win == False:
            pygame.draw.rect(screen, (0,0,0), (0,0,1000,1000))
            screen_text(screen, "GAME OVER", 50, WIDTH/2, HEIGHT/2)
            screen_text(screen, "The party has fallen", 20, WIDTH/2, HEIGHT * 0.7)
            pygame.display.flip()
            pygame.time.wait(3000)
            pygame.event.clear()
            pygame.quit()
            sys.exit()

        #Pacing
        pygame.time.wait(150)


#Adding the sprites to groups to be put onto the screen
maximum = 0


#Here, I will declare variables to use during roaming state
text1 = ("")
text2 = ("")
floor = 0
item = 5


#Start up
title_rect = title.get_rect()
screen.blit(title, title_rect)
screen_text(screen, "Press any key to play", 20, WIDTH /2, HEIGHT * 0.8)
screen_text(screen, "W,A,S,D or Arrow keys: Move character", 16, WIDTH /2, HEIGHT * 0.5)
screen_text(screen, "P or Enter: Select", 16, WIDTH /2, HEIGHT * 0.55)
screen_text(screen, "I: Pause Game", 16, WIDTH /2, HEIGHT * 0.6)
screen_text(screen, "Esc or Close button: Exit game", 16, WIDTH /2, HEIGHT * 0.65)
pygame.display.flip()

run = False
pygame.event.clear()
while run == False:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        run = True

#This will spawn all the sprites for the first floor
Player.spawnplayer(Player)
Wall.spawnwalls(Wall)
Mob.spawnmobs(Mob)
Drop.spawndrops(Drop)
Exit.spawnsteps(Exit)

#Make Background
background_rect = background.get_rect()

#This will be the game loop
while run == True:
    clock.tick(FPS)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]: 
            run = False
    
    
    #Sprite update
    walls.update()
    mobs.update()
    items.update()
    stairs.update()
    players.update()
    #Draw and render the other screen elements
    screen.fill((0,0,255))
    screen.blit(background, background_rect)
    draw_grid(screen)
    sprites.draw(screen)
    items.draw(screen)
    screen_text(screen, text1, 16, WIDTH /2, HEIGHT * 0.8)
    screen_text(screen, text2, 16, WIDTH /2, HEIGHT * 0.85)
    pygame.display.flip()
    
    #Pause screen
    if key[pygame.K_i]:
        pygame.draw.rect(screen, (0,0,0,125), (0,0,640,480))
        screen_text(screen, "Paused", 25, WIDTH / 2, HEIGHT * 0.45)
        screen_text(screen, "Press any button to unpause", 20, WIDTH / 2, HEIGHT * 0.75)
        screen_text(screen, "Press Escape to exit the game", 20, WIDTH / 2, HEIGHT * 0.8)
        pygame.display.flip()
        run = False
        while run == False:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                run = True

    
    #Sprite Interactions
    get_battle = pygame.sprite.groupcollide(players, mobs, False, True)
    get_item = pygame.sprite.groupcollide(players, items, False,  True)
    get_bump = pygame.sprite.groupcollide(players, walls, False, False)
    get_next = pygame.sprite.groupcollide(players, stairs, False,  True)
    
    #If the player sprite collides with the enemy sprite, the battle state will begin
    if get_battle:
        win = False
        lose = False
        escape = False
        battle(win, lose, item)


    #When the player sprite collides with the stairs sprite, it enters a new floor.
    if get_next:
        floor +=1
        if floor < 10:
            sprites.empty()
            players.empty()
            mobs.empty()
            items.empty()
            walls.empty()
            Player.spawnplayer(Player)
            Wall.spawnwalls(Wall)
            Mob.spawnmobs(Mob)
            Drop.spawndrops(Drop)
            Exit.spawnsteps(Exit)
        else:
            ctypes.windll.user32.MessageBoxW(0,"You have reached the end of the dungeon!", "Well Played!", 0)
            run = False
        
    if get_bump:
        player = Player()
        text1 = ("bump")
        text2 = ("")
    
    if get_item:
        item += 1
        if item > 10:
            text1 = ("Got an item but your bag is full")
            item = 10
        else:
            text1 = ("Got an item")
        text2 = (str(item))
    
    
    pygame.time.wait(100)
    
#After the loop ends, the game will also end
pygame.quit()
sys.exit()

