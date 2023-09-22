# -- Made by Snappyink (chalumo) --
# ------ Open Source Project ------
# ---------- Using UTF 8 ----------

from math import cos, sin
# from itertools import combinations
from assets.settings import *
from numba import njit
import assets.game
import pygame
import time

pygame.init()
pygame.display.set_caption("BITE")
DISPLAY = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
SCREEN = pygame.Surface((SCREEN_X, SCREEN_Y))
# FONT = pygame.font.Font("assets/pixel.ttf", 25)
FONT = pygame.font.SysFont('arial', 25)
pygame.mouse.set_visible(False)
CLOCK = pygame.time.Clock()

game = assets.game.Game()


@njit
def get_point_pos(pts_: tuple or list, cos_x_: float, cos_y_: float, sin_x_: float,
                  sin_y_: float, fov_: int, pos_: list) -> tuple:
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
    ps_ = []
    vs_points_ = []
    pos_x, pos_y, pos_z = pos_[0], pos_[1], pos_[2]
    indx = 0
    for p in pts_:
        """distance = ((p[0] - pos_x) ** 2 + (p[1] - pos_y) ** 2 + (
                    p[2] - pos_z) ** 2) ** 0.5  # dist(pos, p)  # Gets distance between the point p and the player"""
        p = (p[0] - pos_x, p[1] - pos_y, p[2] - pos_z)  # The position of the point p for calculations
        p_x, p_y, p_z = p[0], p[1], p[2]
        transformed_point = (p_x * cos_y_ + p_z * sin_y_,
                             p_x * (sin_x_ * sin_y_) + p_y * cos_x_ - p_z * (sin_x_ * cos_y_),
                             p_y * sin_x_ + p_z * (cos_x_ * cos_y_) - p_x * (cos_x_ * sin_y_))
        # vs_points.append((transformed_point, distance))
        vs_points_.append(transformed_point)
        tp2 = transformed_point[2]
        if tp2 > 0:  # coordinates in screen space, point = (x*fov/z, y*fov/z)
            p = (transformed_point[0] * fov_ / tp2,
                 transformed_point[1] * fov_ / tp2)
            ps_.append([p[0] + HALF_SCREEN_X, p[1] + HALF_SCREEN_Y])
        else:
            ps_.append(None)
        indx += 1
    return ps_, vs_points_


get_point_pos(game.optimized_points, 1.0, 1.0, 0.0, 0.0, PLAYER_FOV, game.player.pos)

playing = True
while playing:

    # Get outside values
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    cam_x, cam_y = game.player.camX, game.player.camY
    cos_x, cos_y, sin_x, sin_y = cos(cam_x), cos(cam_y), sin(cam_x), sin(cam_y)
    player_fov = game.player.fov

    # Mouse head movement
    if mouse_pos_x != HALF_SCREEN_X:
        game.player.camY -= (mouse_pos_x - HALF_SCREEN_X) * CAMERA_SENSIBILITY
        pygame.mouse.set_pos((HALF_SCREEN_X, mouse_pos_y))
    if mouse_pos_y != HALF_SCREEN_Y:
        move = mouse_pos_y - HALF_SCREEN_Y
        if (move > 0 and cam_x <= RD85) or (move < 0 and cam_x >= NRD85):
            game.player.camX += move * CAMERA_SENSIBILITY
        pygame.mouse.set_pos((mouse_pos_x, HALF_SCREEN_Y))

    game.player.controls(pygame.key.get_pressed(), CLOCK.tick(MAX_FPS) / 100)

    SCREEN.fill((0, 150, 255))  # Clear screen

    # Get onscreen position of points
    ps, vs_points = get_point_pos(game.optimized_points, cos_x, cos_y, sin_x, sin_y, player_fov, game.player.pos)

    displayed_faces = 0
    # Draw polygons
    if game.len_points >= 2:
        # system.update_polygons_distance()
        for k in game.optimized_polygons:
            i = k[0]  # every element of polygon is this way : ([points], distance, length, color)
            not_false_point = []
            len_points = 0
            points = []
            pts = []
            for y in range(k[2]):  # For every point in the polygon
                point = i[y]
                ps_point = ps[point]
                points.append(ps_point)
                len_points += 1
                pts.append((vs_points[point]))
                if ps_point is not None:
                    not_false_point.append(ps_point)
            if len(not_false_point) >= 1:
                if None in points:
                    lst = []
                    for x in range(len_points):
                        if points[x] is not None:
                            lst.append(points[x])

                        point_ = points[(x + 1) % len_points]
                        if (point_ is None and points[x] is not None) or (
                                point_ is not None and points[x] is None):
                            lst.append(clip3d(pts[(x + 1) % len_points], pts[x], player_fov))
                    if len(lst) >= 3:
                        pygame.draw.polygon(SCREEN, k[3], lst)
                        displayed_faces += 1
                else:
                    pygame.draw.polygon(SCREEN, k[3], points)
                    displayed_faces += 1

    # Display fps on screen
    SCREEN.blit(FONT.render(f"FACES: {displayed_faces}", True, (255, 255, 255)), (5, 5))
    SCREEN.blit(FONT.render(f"FPS: {round(CLOCK.get_fps(), 1)}", True, (255, 255, 255)), (5, 25))

    DISPLAY.blit(SCREEN, (0, 0))

    pygame.display.flip()
    # EVENTS
    for event in pygame.event.get():

        # IF THE WINDOW IS CLICKED
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False  # STOP THE LOOP (CLOSE THE GAME)
