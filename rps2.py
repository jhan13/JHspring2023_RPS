# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 1000
HEIGHT = 1000
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initializes pi game 
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
# calculates the time and frames per second 
clock = pg.time.Clock()
# gets the image in your folder and creates a variable to store the pixels ready to be used 
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# it is storing not the pixels there are but where they are stored and lets us access and change the pixels 
rock_image_rect = rock_image.get_rect()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()

running = True
                                                                                                               
                                                                                                               
while running:
    # sets the frame rate for 30 fps 
    clock.tick(FPS)

# event is anytime you do anything for the computer, for ex: typing, moving the mouse 
    for event in pg.event.get():
        # whenever it runs its not true, its false, so after running once it will stop
        if event.type == pg.QUIT:
            running = False
        # the trackpad is tracking for when you click the image and releasing 
        if event.type == pg.MOUSEBUTTONUP:
           # displays coordinates for displaying 0 and 1, 0 and 1 are the parts of the tuple 
            print(pg.mouse.get_pos()[0])
            print(pg.mouse.get_pos()[1])
            mouse_coords = pg.mouse.get_pos()
            # if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            #     print("i clicked the rock")
            # else:
            #     print("no rock....")
            # this data type is returning a true or false 
            print(rock_image_rect.collidepoint(mouse_coords))
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock...")
            elif paper_image_rect.collidepoint(mouse_coords):
                pass
            else:
                print("you didn't click on anything...")
    ############### input ##############
    #HCI - human computer interaction... 
    # keyboard, mouse, controller , vr headset
    # get user input

    # update
    rock_image_rect.x += 1
    rock_image_rect.y += 1

    # draw
    screen.fill(BLACK)

    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(paper_image, paper_image_rect)


    pg.display.flip()

pg.quit()

