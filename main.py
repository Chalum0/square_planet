# -- Made by Snappyink (chalumo) --
# ------ Open Source Project ------
# ---------- Using UTF 8 ----------

from math import cos, sin
# from itertools import combinations
from assets.settings import *
import assets.game
import pygame
import time

pygame.init()
pygame.display.set_caption("BITE")
SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
CLOCK = pygame.time.Clock()

game = assets.game.Game()

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


    SCREEN.fill((0, 150, 255))  # Clear screen

    # Get onscreen position of points
    ps, vs_points = assets.game.get_point_pos(game.points, cos_x, cos_y, sin_x, sin_y, player_fov, game.player.pos)




    # Draw polygons
    if game.len_points >= 2:
        # system.update_polygons_distance()




        for k in game.polygons:
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
                if ps_point is not False:
                    not_false_point.append(ps_point)
            if len(not_false_point) >= 1:
                if False in points:
                    lst = []
                    for x in range(len_points):
                        if points[x] is not False:
                            lst.append(points[x])

                        point_ = points[(x + 1) % len_points]
                        if (point_ is False and points[x] is not False) or (
                                point_ is not False and points[x] is False):

                            lst.append(clip3d(pts[(x + 1) % len_points], pts[x], player_fov))
                    if len(lst) >= 3:
                        pygame.draw.polygon(SCREEN, k[3], lst)
                else:
                    pygame.draw.polygon(SCREEN, k[3], points)






    # EVENTS
    for event in pygame.event.get():

        # IF THE WINDOW IS CLICKED
        if event.type == pygame.QUIT:
            time.sleep(0.2)
            playing = False  # STOP THE LOOP (CLOSE THE GAME)
