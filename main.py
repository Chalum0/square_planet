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
    cam_x, cam_y = None, None
    cos_x, cos_y, sin_x, sin_y = None, None, None, None



    # Mouse head movement
    if mouse_pos_x != HALF_SCREEN_X:
        system.player.camY -= (mouse_pos_x - HALF_SCREEN_X) * CAMERA_SENSIBILITY
        pygame.mouse.set_pos((HALF_SCREEN_X, mouse_pos_y))

    if mouse_pos_y != HALF_SCREEN_Y:
        move = mouse_pos_y - HALF_SCREEN_Y
        if ((move > 0 and cam_x <= RD85) or (move < 0 and cam_x >= NRD85)):
            system.player.camX += move * CAMERA_SENSIBILITY
        pygame.mouse.set_pos((mouse_pos_x, HALF_SCREEN_Y))


    # EVENTS
    for event in pygame.event.get():

        # IF THE WINDOW IS CLICKED
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False  # STOP THE LOOP (CLOSE THE GAME)
