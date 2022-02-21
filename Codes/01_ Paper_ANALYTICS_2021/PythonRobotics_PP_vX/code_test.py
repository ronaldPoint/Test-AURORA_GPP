
from matplotlib import lines
import pandas as pd
import math
import matplotlib.pyplot as plt
import csv
from pathlib import Path
import winsound
import numpy as np
from numpy.core.fromnumeric import size
from RobotPP_vX import *

map_size = 100
map_X, map_XA, map_XB = map_type.line_coord_gen(clearance=5, map_size=100)
clearance = 5
map_size = 100

def line_coord_gen(clearance, map_size):    # Generate coordinates for lines obstacles
        x1 = int(clearance)
        x2 = int(np.trunc(map_size/2-clearance/2))
        x3 = int(np.trunc(map_size/2+clearance/2))
        x4 = int(map_size-clearance)

        y1 = x1
        y2 = x2
        y3 = x3
        y4 = x4
        # lines --> l1, l2, l3, ...
        x_lines = [[x1, x4, y4], [x1, x4, y3], [x1, x2, y2], [x1, x2, y1], [x3, x4, y2], [x3, x4, y1]]
        y_lines = [[y3, y4, x1], [y3, y4, x4], [y1, y2, x1], [y1, y2, x2], [y1, y2, x3], [y1, y2, x4]]
        map_X = [x_lines, y_lines]
        ##
        r  = int(np.trunc((x2-x1)/2))
        map_XA = [(x1+r, y1+r, r), (x3+r, y1+r, r)]
        k = 1
        while (x1+k*r) <= (x4-r): 
            new_circle = (x1+k*r, y3+r, r)
            map_XA.append(new_circle)
            k = k + 2

        ## 
        map_XB = [ [[x1, x4, x4, x1], [y3, y3, y4, y4] ], [[x1, x2, x2, x1], [y1, y1, y2, y2]], [[x3, x4, x4, x3], [y1, y1, y2, y2]] ]
        return map_X, map_XA, map_XB 
    
map_X, map_XA, map_XB = line_coord_gen(clearance, map_size)
print(len(map_XA))
print(map_XA[0])
print(map_XA)
# print(map_XA)

