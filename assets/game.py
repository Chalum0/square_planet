from math import dist
from assets.settings import *
import pygame
# import pygame


class Game:
    def __init__(self):
        self.player = Player()
        self.len_points = 0
        self.len_polygons = 1
        self.points = []
        self.polygons = []
        self.optimized_points = []
        self.optimized_polygons = []

        for i in range(200):
            self.create_quare()
        self.optimisation()

    def create_quare(self):
        self.points.append((5, 10, 5))
        self.points.append((10, 10, 5))
        self.points.append((5, 10, 10))
        self.points.append((10, 10, 10))
        self.len_points += 4

        self.polygons.append(([1*self.len_polygons - 1, 2*self.len_polygons - 1,
                               4*self.len_polygons - 1, 3*self.len_polygons - 1],
                              0, 4, (255, 0, 0)))

    def optimisation(self):

        # optimize points
        self.optimized_points = []
        for point in self.points:
            if not point in self.optimized_points:
                self.optimized_points.append(point)
        for i in range(len(self.polygons)):
            for y in range(len(self.polygons[i])):
                self.polygons[i][0][y] = self.optimized_points.index(self.points[self.polygons[i][0][y]])

        # optimize polygons
        self.optimized_polygons = []
        polygon_points = []
        for polygon in self.polygons:
            if not polygon[0] in polygon_points:
                self.optimized_polygons.append(polygon)
                polygon_points.append(polygon[0])








class Player:
    def __init__(self):
        self.camX = 0
        self.camY = 0
        self.pos = list(PLAYER_START_POS)
        self.fov = PLAYER_FOV
        self.speed = PLAYER_SPEED_START

    def controls(self, keys, dt):
        if keys[pygame.K_d]:  # If the D key is pressed: go right
            self.pos[0], self.pos[2] = calculate_new_xy((self.pos[0], self.pos[2]), -self.speed * dt, -self.camY)
        if keys[pygame.K_q] or keys[pygame.K_a]:  # If the Q or A key is pressed: go left
            self.pos[0], self.pos[2] = calculate_new_xy((self.pos[0], self.pos[2]), self.speed * dt, -self.camY)
        if keys[pygame.K_z] or keys[pygame.K_w]:  # If the Z or W key is pressed: go forward
            self.pos[0], self.pos[2] = calculate_new_xy((self.pos[0], self.pos[2]), self.speed * dt,
                                                        -self.camY + math.radians(90))
        if keys[pygame.K_s]:  # If the s key is pressed: go backward
            self.pos[0], self.pos[2] = calculate_new_xy((self.pos[0], self.pos[2]), -self.speed * dt,
                                                        -self.camY + math.radians(90))
        if keys[pygame.K_SPACE]:
            self.pos[1] -= self.speed * dt
        if keys[pygame.K_LCTRL] or keys[pygame.K_LSHIFT]:
            self.pos[1] += self.speed * dt
