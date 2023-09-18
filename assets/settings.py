import math

# Screen settings
SCREEN_X, SCREEN_Y = (1080, 720)
HALF_SCREEN_X, HALF_SCREEN_Y = (int(SCREEN_X/2), int(SCREEN_Y/2))


# Player settings
PLAYER_START_POS = (0, 0, 0)
PLAYER_FOV = 400
PLAYER_SPEED_START = 3.0
CAMERA_SENSIBILITY = round((0.05/2) * (0.05/2) * 3, 7)


# Other
RD85 = math.radians(85)
NRD85 = -RD85
ZCD = 1

def clip3d(p1, p2, fov):
    p1_0, p1_1, p1_2 = p1
    p2_0, p2_1, p2_2 = p2
    step = ((ZCD-p1_2)/(p2_2-p1_2))
    return (p1_0 + (p2_0 - p1_0) * step) * fov / ZCD + HALF_SCREEN_X, (p1_1 + (p2_1 - p1_1) * step) * fov / ZCD + HALF_SCREEN_Y
