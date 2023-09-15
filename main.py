# -- Made by Snappyink (chalumo) --
# ------ Open Source Project ------
# ---------- Using UTF 8 ----------

from math import degrees, cos, sin
from itertools import combinations
from assets.settings import *
import random
import pygame
import pickle
import time

pygame.init()
pygame.display.set_caption("3D Maker")
SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y), pygame.FULLSCREEN)
SCREEN_X, SCREEN_Y = SCREEN.get_size()
HALF_SCREEN_X, HALF_SCREEN_Y = (int(SCREEN_X / 2), int(SCREEN_Y / 2))
CLOCK = pygame.time.Clock()


playing = True
while playing:

    # EVENTS
    for event in pygame.event.get():

        # IF THE WINDOW IS CLICKED
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False  # STOP THE LOOP (CLOSE THE GAME)
