#-------------------------------------------------------------------------------
# CS142 Assignment 1: Shadows of the Knight - Episode 1
# A solution to the activity Shadows of the Knight - Episode 1 from Codin Game.
#
# Rica Bernadine Calbario
# CS142 - G
#-------------------------------------------------------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x_0, y_0 = [int(i) for i in input().split()]
min_x = min_y  = 0
max_x = w - 1
max_y = h - 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if bomb_dir.find("L")>-1:
        max_x = x_0 - 1
    elif bomb_dir.find("R")>-1:
        min_x = x_0 + 1
    if bomb_dir.find("U")>-1:
        max_y = y_0 - 1
    elif bomb_dir.find("D")>-1:
        min_y = y_0 + 1

    x_0 = min_x + math.ceil((max_x  - min_x)/2)
    y_0 = min_y + math.ceil((max_y  - min_y)/2)
    # the location of the next window Batman should jump to.
    print("{0} {1}".format(int(x_0), int(y_0)))

# Reference: https://github.com/vadim-job-hg/Codingame/blob/master/MEDIUM/SHADOW%20OF%20THE%20KNIGHT%20-%20EPISODE%201/python/shadows-of-the-knight-episode-1.py