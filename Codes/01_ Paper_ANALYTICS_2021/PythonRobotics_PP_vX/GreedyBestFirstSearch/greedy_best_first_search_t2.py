"""

Greedy Best-First grid planning

author: Erwin Lejeune (@spida_rwin)

See Wikipedia article (https://en.wikipedia.org/wiki/Best-first_search)

"""

import math
import time
import matplotlib.pyplot as plt

from RobotPP_vX import *

show_animation = True


class BestFirstSearchPlanner:

    def __init__(self, ox, oy, reso, rr):
        """
        Initialize grid map for greedy best-first planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.reso = reso
        self.rr = rr
        self.calc_obstacle_map(ox, oy)
        self.motion = self.get_motion_model()

    class Node:
        def __init__(self, x, y, cost, pind, parent):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.pind = pind
            self.parent = parent

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.pind)

    def planning(self, sx, sy, gx, gy):
        """
        Greedy Best-First search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """
        cnt1 = 0
        nstart = self.Node(self.calc_xyindex(sx, self.minx),
                           self.calc_xyindex(sy, self.miny), 0.0, -1, None)
        ngoal = self.Node(self.calc_xyindex(gx, self.minx),
                          self.calc_xyindex(gy, self.miny), 0.0, -1, None)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(nstart)] = nstart

        while 1:
            cnt1 = cnt1 + 1
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: self.calc_heuristic(ngoal, open_set[o]))

            current = open_set[c_id]

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current.x, self.minx),
                         self.calc_grid_position(current.y, self.miny), "xc")
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event:
                                             [exit(0)
                                              if event.key == 'escape'
                                              else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            if current.x == ngoal.x and current.y == ngoal.y:
                print("Found goal")
                ngoal.pind = current.pind
                ngoal.cost = current.cost
                break

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion):
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2],
                                 c_id, current)

                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node
                else:
                    if open_set[n_id].cost > node.cost:
                        open_set[n_id] = node
        closed_set[ngoal.pind] = current
        rx, ry = self.calc_final_path(ngoal, closed_set)
        return rx, ry, cnt1

    def calc_final_path(self, ngoal, closedset):
        # generate final course
        rx, ry = [self.calc_grid_position(ngoal.x, self.minx)], [
            self.calc_grid_position(ngoal.y, self.miny)]
        n = closedset[ngoal.pind]
        while n is not None:
            rx.append(self.calc_grid_position(n.x, self.minx))
            ry.append(self.calc_grid_position(n.y, self.miny))
            n = n.parent

        return rx, ry

    @staticmethod
    def calc_heuristic(n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        return d

    def calc_grid_position(self, index, minp):
        """
        calc grid position

        :param index:
        :param minp:
        :return:
        """
        pos = index * self.reso + minp
        return pos

    def calc_xyindex(self, position, min_pos):
        return round((position - min_pos) / self.reso)

    def calc_grid_index(self, node):
        return (node.y - self.miny) * self.xwidth + (node.x - self.minx)

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.minx)
        py = self.calc_grid_position(node.y, self.miny)

        if px < self.minx:
            return False
        elif py < self.miny:
            return False
        elif px >= self.maxx:
            return False
        elif py >= self.maxy:
            return False

        # collision check
        if self.obmap[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.minx = round(min(ox))
        self.miny = round(min(oy))
        self.maxx = round(max(ox))
        self.maxy = round(max(oy))
        print("min_x:", self.minx)
        print("min_y:", self.miny)
        print("max_x:", self.maxx)
        print("max_y:", self.maxy)

        self.xwidth = round((self.maxx - self.minx) / self.reso)
        self.ywidth = round((self.maxy - self.miny) / self.reso)
        print("x_width:", self.xwidth)
        print("y_width:", self.ywidth)

        # obstacle map generation
        self.obmap = [[False for _ in range(self.ywidth)]
                      for _ in range(self.xwidth)]
        for ix in range(self.xwidth):
            x = self.calc_grid_position(ix, self.minx)
            for iy in range(self.ywidth):
                y = self.calc_grid_position(iy, self.miny)
                for iox, ioy in zip(ox, oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.rr:
                        self.obmap[ix][iy] = True
                        break

    @staticmethod
    def get_motion_model():
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1],
                  [-1, -1, math.sqrt(2)],
                  [-1, 1, math.sqrt(2)],
                  [1, -1, math.sqrt(2)],
                  [1, 1, math.sqrt(2)]]

        return motion


def main():
    print(__file__ + " start!!")
    algorithm = 'Greedy_BFS'

    setup = 0
    # map = 'Type_4'  # Id for a map type
    map_size = 200  #100
    wall_coord = map_type.wall_coord(1) # Default 100x100 map -->0
    clearance = [5, 10, 15, 20, 25, 30]#, 35, 40]
    type_map = ['Type_1', 'Type_2_1', 'Type_2_2', 'Type_3_1', 'Type_3_2', 'Type_3_3', 'Type_3_4', 
                'Type_4', 'Type_5_1', 'Type_5_2', 'Type_5_3', 'Type_6_1', 'Type_6_2',
                'Type_7_1', 'Type_7_2', 'Type_7_3', 'Type_7_4']
    
    # for x in type_map:
    for c in clearance:   #range (0,len(clearance)):
            # map, mapX, mapXA, mapXB = line_coord_gen(c, map_size, x)
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_1(c, map_size, 'Type_1')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_2_1(c, map_size, 'Type_2_1')
            map, mapX, mapXA, mapXB = map_type.line_coord_gen_2_2(c, map_size, 'Type_2_2')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_3_1(c, map_size, 'Type_3_1')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_3_2(c, map_size, 'Type_3_2')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_3_3(c, map_size, 'Type_3_3')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_3_4(c, map_size, 'Type_3_4')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_4(c, map_size, 'Type_4')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_5_1(c, map_size, 'Type_5_1')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_5_2(c, map_size, 'Type_5_2')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_5_3(c, map_size, 'Type_5_3')

            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_6_1(c, map_size, 'Type_6_1')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_6_2(c, map_size, 'Type_6_2')

            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_7_1(c, map_size, 'Type_7_1')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_7_2(c, map_size, 'Type_7_2')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_7_3(c, map_size, 'Type_7_3')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_7_4(c, map_size, 'Type_7_4')

            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_8_1(c, map_size, 'Type_8_1')
            # map, mapX, mapXA, mapXB = map_type.line_coord_gen_8_2(c, map_size, 'Type_8_2')

            ox, oy, sx, sy, gx, gy, grid_size, robot_radius = scenarios.scenario_X(mapX, wall_coord)

            if show_animation:  # pragma: no cover
                plt.plot(ox, oy, ".k")
                plt.plot(sx, sy, "og")
                plt.plot(gx, gy, "xb")
                plt.grid(True)
                plt.axis("equal")

            greedybestfirst = BestFirstSearchPlanner(ox, oy, grid_size, robot_radius)
        
            rx, ry, iter = greedybestfirst.planning(sx, sy, gx, gy)
            
            len_p = Metrics.path_length(rx, ry)

            manageData.saveData(algorithm, map, sx, sy, gx, gy, rx, ry, len_p, iter, setup, c)

            if show_animation:  # pragma: no cover
                plt.plot(rx, ry, "-r")
                plt.pause(0.01)
                plt.show()


if __name__ == '__main__':
    for i in range(1):
        main()
    
    sounds.beep(1000, 850)   # (duration, frequency)
