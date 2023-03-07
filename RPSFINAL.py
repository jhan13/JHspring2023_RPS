
# File created by: Joon Han
# 
 
# import libraries
from time import sleep
import random
import pygame as pg
import os

game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
#print(game_folder)

# game settings
WIDTH = 1200
HEIGHT = 800
FPS = 30
GAMEOVER = False

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up game system
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

# rock image
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = 35
rock_image_rect.y = 50

# paper image
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 475
paper_image_rect.y = 50

# scissors image
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 950
scissors_image_rect.y = 50

# font
font = pg.font.SysFont('Arial', 20, bold=True, italic=False) #try inkfree, georgia,impact,dubai,arial
font.set_underline(True)

# variables
running = True
playerHand = -1 # -1-nothing, 0-rock, 1-paper, 2-scissors
npcHand = -1    # -1-nothing, 0-rock, 1-paper, 2-scissors

# draw text 
message = 'Hello Everyone!'

def drawText():
    text = font.render(message,True,(255,255,255)) #This creates a new Surface with the specified text rendered on it
    textrect = text.get_rect()
    textrect.center = (WIDTH*0.5, HEIGHT*0.7)
    screen.blit(text, textrect)
    return

def WhoWins():
    msg = ''

    if playerHand == 0:
        if npcHand == 0:
            msg = 'Tied!'
        elif npcHand == 1: 
            msg = 'You lost!'
        elif npcHand == 2:
            msg = 'You won!'
    elif playerHand == 1:
        if npcHand == 0:
            msg = 'You won!'
        elif npcHand == 1: 
            msg = 'Tied!'
        elif npcHand == 2:
            msg = 'You lost!'
    elif playerHand == 2:
        if npcHand == 0:
            msg = 'You lost!'
        elif npcHand == 1: 
            msg = 'You won!'
        elif npcHand == 2:
            msg = 'Tied!'
    else:
        msg = "You clicked nothing!" 

    return msg

while running:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # 
        if event.type == pg.MOUSEBUTTONUP:
            # 
            print(pg.mouse.get_pos()[0])
            # 
            print(pg.mouse.get_pos()[1])
            # 
            mouse_coords = pg.mouse.get_pos()

            if rock_image_rect.collidepoint(mouse_coords):
                playerHand = 0
                npcHand = random.randint(0, 2);
                message = WhoWins()
            elif paper_image_rect.collidepoint(mouse_coords):
                playerHand = 1
                npcHand = random.randint(0, 2);
                message = WhoWins()
            elif scissors_image_rect.collidepoint(mouse_coords):
                playerHand = 2
                npcHand = random.randint(0, 2);
                message = WhoWins() 
            else:
                playerHand = -1
                npcHand = -1
                message = "You clicked nothing!"    

    ########## input ###########
    # HCI - human computer interaction...
    # keyboard, mouse, controller, vr headset
    
    ########## update ###################
    # rock_image_rect.x += 1
   # if rock_image_rect.y < 300 and not GAMEOVER:
    #    rock_image_rect.y += 1
    

    ############ draw ###################
    screen.fill(BLACK)

    if not GAMEOVER:
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    else:
        screen.blit(rock_image, rock_image_rect)

    # draw text message
    drawText()
    
    pg.display.flip()

# Quit the game system.
pg.quit()
