from math import dist
from assets.settings import *
# import pygame


def get_point_pos(points: tuple or list, cos_x: float, cos_y: float, sin_x: float,
                  sin_y: float, fov: int or float, pos: tuple or list) -> tuple:
    """Most optimised version of the function: made by snappyink (chalumo).
    Returns the position on screen of points out of a 3D coord. Takes 7 arguments:
    -Points : a list of the 3D coords of every point (must be a tuple or a list)
    -Cos_x : the cos value of the player cam_x value (must be a float)
    -Cos_y : the cos value of the player cam_y value (must be a float)
    -Sin_x : the sin value of the player cam_x value (must be a float)
    -Sin_y : the sin value of the player cam_y value (must be a float)
    -Fov : The player's FOV (must be an int or a float)
    -Pos : The player's 3D coords (must be a tuple or a list)
    """
    ps = []
    vs_points = []
    pos_x, pos_y, pos_z = pos[0], pos[1], pos[2]
    for p in points:
        distance = dist(pos, p)  # Gets distance between the point p and the player
        p = (p[0] - pos_x, p[1] - pos_y, p[2] - pos_z)  # The position of the point p for calculations
        p_x, p_y, p_z = p[0], p[1], p[2]
        transformed_point = (p_x * cos_y + p_z * sin_y,
                             p_x * (sin_x * sin_y) + p_y * cos_x - p_z * (sin_x * cos_y),
                             p_y * sin_x + p_z * (cos_x * cos_y) - p_x * (cos_x * sin_y))
        vs_points.append((transformed_point, distance))
        tp2 = transformed_point[2]
        if tp2 > 0:  # coordinates in screen space, point = (x*fov/z, y*fov/z)
            p = (transformed_point[0] * fov / tp2,
                 transformed_point[1] * fov / tp2)
            ps.append((p[0] + HALF_SCREEN_X, p[1] + HALF_SCREEN_Y))
        else:
            ps.append(False)
    return ps, vs_points


class Game:
    def __init__(self):
        self.player = Player()
        self.len_points = 0
        self.points = []
        self.polygons = []


class Player:
    def __init__(self):
        self.camX = 0
        self.camY = 0
        self.pos = list(PLAYER_START_POS)
        self.fov = PLAYER_FOV
        self.speed = PLAYER_SPEED_START
