from math import sin, cos, dist
from assets.settings import *
import pygame



class System:
    def __init__(self):
        self.player = Player()
        self.points = []
        self.polygons = []


class Player:
    def __init__(self):
        self.camX = 0
        self.camY = 0
        self.pos = list(PLAYER_START_POS)
        self.fov = PLAYER_FOV
        self.speed = PLAYER_SPEED_START
