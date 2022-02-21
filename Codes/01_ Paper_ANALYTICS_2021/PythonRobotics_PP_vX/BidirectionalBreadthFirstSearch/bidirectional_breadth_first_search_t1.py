"""

Bidirectional Breadth-First grid planning

author: Erwin Lejeune (@spida_rwin)

See Wikipedia article (https://en.wikipedia.org/wiki/Breadth-first_search)

"""

import math
import time
import matplotlib.pyplot as plt

from RobotPP_vX import *

show_animation = False


class BidirectionalBreadthFirstSearchPlanner:

    def __init__(self, ox, oy, resolution, rr):
        """
        Initialize grid map for bfs planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.min_x, self.min_y = None, None
        self.max_x, self.max_y = None, None
        self.x_width, self.y_width, self.obstacle_map = None, None, None
        self.resolution = resolution
        self.rr = rr
        self.calc_obstacle_map(ox, oy)
        self.motion = self.get_motion_model()

    class Node:
        def __init__(self, x, y, cost, parent_index, parent):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index
            self.parent = parent

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):
        """
        Bidirectional Breadth First search based planning

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
        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1,
                               None)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1,
                              None)

        open_set_A, closed_set_A = dict(), dict()
        open_set_B, closed_set_B = dict(), dict()
        open_set_B[self.calc_grid_index(goal_node)] = goal_node
        open_set_A[self.calc_grid_index(start_node)] = start_node

        meet_point_A, meet_point_B = None, None

        while 1:
            cnt1 = cnt1 + 1
            if len(open_set_A) == 0:
                print("Open set A is empty..")
                break

            if len(open_set_B) == 0:
                print("Open set B is empty")
                break

            current_A = open_set_A.pop(list(open_set_A.keys())[0])
            current_B = open_set_B.pop(list(open_set_B.keys())[0])

            c_id_A = self.calc_grid_index(current_A)
            c_id_B = self.calc_grid_index(current_B)

            closed_set_A[c_id_A] = current_A
            closed_set_B[c_id_B] = current_B

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current_A.x, self.min_x),
                         self.calc_grid_position(current_A.y, self.min_y),
                         "xc")
                plt.plot(self.calc_grid_position(current_B.x, self.min_x),
                         self.calc_grid_position(current_B.y, self.min_y),
                         "xc")
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect(
                    'key_release_event',
                    lambda event: [exit(0) if event.key == 'escape' else None])
                if len(closed_set_A.keys()) % 10 == 0:
                    plt.pause(0.001)

            if c_id_A in closed_set_B:
                print("Find goal")
                meet_point_A = closed_set_A[c_id_A]
                meet_point_B = closed_set_B[c_id_A]
                break

            elif c_id_B in closed_set_A:
                print("Find goal")
                meet_point_A = closed_set_A[c_id_B]
                meet_point_B = closed_set_B[c_id_B]
                break

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion):
                breakA = False
                breakB = False

                node_A = self.Node(current_A.x + self.motion[i][0],
                                   current_A.y + self.motion[i][1],
                                   current_A.cost + self.motion[i][2],
                                   c_id_A, None)
                node_B = self.Node(current_B.x + self.motion[i][0],
                                   current_B.y + self.motion[i][1],
                                   current_B.cost + self.motion[i][2],
                                   c_id_B, None)

                n_id_A = self.calc_grid_index(node_A)
                n_id_B = self.calc_grid_index(node_B)

                # If the node is not safe, do nothing
                if not self.verify_node(node_A):
                    breakA = True

                if not self.verify_node(node_B):
                    breakB = True

                if (n_id_A not in closed_set_A) and \
                        (n_id_A not in open_set_A) and (not breakA):
                    node_A.parent = current_A
                    open_set_A[n_id_A] = node_A

                if (n_id_B not in closed_set_B) and \
                        (n_id_B not in open_set_B) and (not breakB):
                    node_B.parent = current_B
                    open_set_B[n_id_B] = node_B

        rx, ry = self.calc_final_path_bidir(
            meet_point_A, meet_point_B, closed_set_A, closed_set_B)
        return rx, ry,  cnt1

    # takes both set and meeting nodes and calculate optimal path
    def calc_final_path_bidir(self, n1, n2, setA, setB):
        rxA, ryA = self.calc_final_path(n1, setA)
        rxB, ryB = self.calc_final_path(n2, setB)

        rxA.reverse()
        ryA.reverse()

        rx = rxA + rxB
        ry = ryA + ryB

        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        n = closed_set[goal_node.parent_index]
        while n is not None:
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            n = n.parent

        return rx, ry

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True
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
    algorithm = 'Bidirectional_BFS'

    setup = 0
    map_size = 200  #100
    wall_coord = map_type.wall_coord(1) # Default 100x100 map
    clearance = [5, 10, 15, 20, 25, 30]#, 35, 40]
    type_map = ['Type_1', 'Type_2_1', 'Type_2_2', 'Type_3_1', 'Type_3_2', 'Type_3_3', 'Type_3_4', 
                'Type_4', 'Type_5_1', 'Type_5_2', 'Type_5_3', 'Type_5_4', 'Type_6_1', 'Type_6_2',
                'Type_7_1', 'Type_7_2', 'Type_7_3', 'Type_7_4', 'Type_8_1', 'Type_8_2']
    
    for x in type_map:
        for c in clearance:   #range (0,len(clearance)):
            map, mapX, mapXA, mapXB = line_coord_gen(c, map_size, x)
 
            ox, oy, sx, sy, gx, gy, grid_size, robot_radius = scenarios.scenario_X(mapX, wall_coord)

            if show_animation:  # pragma: no cover
                plt.plot(ox, oy, ".k")
                plt.plot(sx, sy, "og")
                plt.plot(gx, gy, "ob")
                plt.grid(True)
                plt.axis("equal")

            bi_bfs = BidirectionalBreadthFirstSearchPlanner(
                ox, oy, grid_size, robot_radius)

            rx, ry, iter = bi_bfs.planning(sx, sy, gx, gy)
            
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