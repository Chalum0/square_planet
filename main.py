# -- Made by Snappyink (chalumo) --
# ------ Open Source Project ------
# ---------- Using UTF 8 ----------

from math import degrees, cos, sin
from itertools import combinations
from assets.settings import *
import assets.game
import random
import pygame
import pickle
import time

pygame.init()
pygame.display.set_caption("BITE")
SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
CLOCK = pygame.time.Clock()

playing = True
while playing:

    # Get outside values
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    cos_x, cos_y, sin_x, sin_y = None, None, None, None



    # EVENTS
    for event in pygame.event.get():

        # IF THE WINDOW IS CLICKED
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False  # STOP THE LOOP (CLOSE THE GAME)
