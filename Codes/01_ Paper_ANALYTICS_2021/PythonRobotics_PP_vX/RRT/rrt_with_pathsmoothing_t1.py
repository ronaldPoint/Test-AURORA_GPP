"""

Path planning Sample Code with RRT with path smoothing

@author: AtsushiSakai(@Atsushi_twi)

"""

import math
import os
import random
import sys
import time
import matplotlib.pyplot as plt

from RobotPP_vX import *

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from rrt_t1 import RRT
except ImportError:
    raise

show_animation = False


def get_path_length(path):
    le = 0
    for i in range(len(path) - 1):
        dx = path[i + 1][0] - path[i][0]
        dy = path[i + 1][1] - path[i][1]
        d = math.sqrt(dx * dx + dy * dy)
        le += d

    return le


def get_target_point(path, targetL):
    le = 0
    ti = 0
    lastPairLen = 0
    for i in range(len(path) - 1):
        dx = path[i + 1][0] - path[i][0]
        dy = path[i + 1][1] - path[i][1]
        d = math.sqrt(dx * dx + dy * dy)
        le += d
        if le >= targetL:
            ti = i - 1
            lastPairLen = d
            break

    partRatio = (le - targetL) / lastPairLen

    x = path[ti][0] + (path[ti + 1][0] - path[ti][0]) * partRatio
    y = path[ti][1] + (path[ti + 1][1] - path[ti][1]) * partRatio

    return [x, y, ti]


def line_collision_check(first, second, obstacleList):
    # Line Equation

    x1 = first[0]
    y1 = first[1]
    x2 = second[0]
    y2 = second[1]

    try:
        a = y2 - y1
        b = -(x2 - x1)
        c = y2 * (x2 - x1) - x2 * (y2 - y1)
    except ZeroDivisionError:
        return False

    for (ox, oy, size) in obstacleList:
        d = abs(a * ox + b * oy + c) / (math.sqrt(a * a + b * b))
        if d <= size:
            return False

    return True  # OK


def path_smoothing(path, max_iter, obstacle_list):
    le = get_path_length(path)

    for i in range(max_iter):
        # Sample two points
        pickPoints = [random.uniform(0, le), random.uniform(0, le)]
        pickPoints.sort()
        first = get_target_point(path, pickPoints[0])
        second = get_target_point(path, pickPoints[1])

        if first[2] <= 0 or second[2] <= 0:
            continue

        if (second[2] + 1) > len(path):
            continue

        if second[2] == first[2]:
            continue

        # collision check
        if not line_collision_check(first, second, obstacle_list):
            continue

        # Create New path
        newPath = []
        newPath.extend(path[:first[2] + 1])
        newPath.append([first[0], first[1]])
        newPath.append([second[0], second[1]])
        newPath.extend(path[second[2] + 1:])
        path = newPath
        le = get_path_length(path)
    
    return path, i


def main():
    algorithm = 'RRT_Path_Smoothing'

    setup = 0
    map = 'Type_4'  # Id for a map type
    map_size = 200  #100
    clearance = [5, 10, 15, 20, 25, 30]#, 35, 40]    # cases = [1, 2, 3, 4, 5, 6,7]
    type_map = ['Type_1', 'Type_2_1', 'Type_2_2', 'Type_3_1', 'Type_3_2', 'Type_3_3', 'Type_3_4', 
                'Type_4', 'Type_5_1', 'Type_5_2', 'Type_5_3', 'Type_5_4', 'Type_6_1', 'Type_6_2',
                'Type_7_1', 'Type_7_2', 'Type_7_3', 'Type_7_4', 'Type_8_1', 'Type_8_2']
    
    for x in type_map:
        for c in clearance:   #range (0,len(clearance)):
            map, mapX, mapXA, mapXB = line_coord_gen(c, map_size, x)

            obstacleList, sx, sy, gx, gy, grid_size, robot_radius = scenarios.scenario_XA(mapXA)

            rrt = RRT(start=[sx, sy], goal=[gx, gy],
                    rand_area=[0, 200], obstacle_list=obstacleList)
            
            path, iter = rrt.planning(animation=show_animation)

            len_p = Metrics.get_path_length(path)
            
            # Path smoothing
            maxIter = 1000
            smoothedPath, cnt2 = path_smoothing(path, maxIter, obstacleList)

            lSmoothPath = Metrics.get_path_length(smoothedPath)
            #print('Length Smoothed Path-->', lSmoothPath)

            manageData.saveData(algorithm, map, sx, sy, gx, gy, [x for (x, y) in smoothedPath], [y for (x, y) in smoothedPath], lSmoothPath, iter, setup, c)
        
            # Draw final path
            if show_animation:
                rrt.draw_graph()
                plt.plot([x for (x, y) in path], [y for (x, y) in path], '-r')

                plt.plot([x for (x, y) in smoothedPath], [
                    y for (x, y) in smoothedPath], '-c')

                plt.grid(True)
                plt.pause(0.01)  # Need for Mac
                plt.show()


if __name__ == '__main__':
    for i in range(1):
        main()
    
    sounds.beep(1000, 850)   # (duration, frequency)
