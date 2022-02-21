
import math
import matplotlib.pyplot as plt
import csv
from pathlib import Path
import winsound

class sounds:   
    def beep( duration, frequency):
        frequency = frequency  # Set Frequency To 2500 Hertz
        duration = duration  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

class ObstaclePolygon:

    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list

        self.close_polygon()
        self.make_clockwise()

    def make_clockwise(self):
        if not self.is_clockwise():
            self.x_list = list(reversed(self.x_list))
            self.y_list = list(reversed(self.y_list))

    def is_clockwise(self):
        n_data = len(self.x_list)
        eval_sum = sum([(self.x_list[i + 1] - self.x_list[i]) *
                        (self.y_list[i + 1] + self.y_list[i])
                        for i in range(n_data - 1)])
        eval_sum += (self.x_list[0] - self.x_list[n_data - 1]) * \
                    (self.y_list[0] + self.y_list[n_data - 1])
        return eval_sum >= 0

    def close_polygon(self):
        is_x_same = self.x_list[0] == self.x_list[-1]
        is_y_same = self.y_list[0] == self.y_list[-1]
        if is_x_same and is_y_same:
            return  # no need to close

        self.x_list.append(self.x_list[0])
        self.y_list.append(self.y_list[0])

    def plot(self):
        plt.plot(self.x_list, self.y_list, "-k")

""" class ObstaclePolygon:

    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list

        self.close_polygon()
        self.make_clockwise()

    def make_clockwise(self):
        if not self.is_clockwise():
            self.x_list = list(reversed(self.x_list))
            self.y_list = list(reversed(self.y_list))

    def is_clockwise(self):
        n_data = len(self.x_list)
        eval_sum = sum([(self.x_list[i + 1] - self.x_list[i]) *
                        (self.y_list[i + 1] + self.y_list[i])
                        for i in range(n_data - 1)])
        eval_sum += (self.x_list[0] - self.x_list[n_data - 1]) * \
                    (self.y_list[0] + self.y_list[n_data - 1])
        return eval_sum >= 0

    def close_polygon(self):
        is_x_same = self.x_list[0] == self.x_list[-1]
        is_y_same = self.y_list[0] == self.y_list[-1]
        if is_x_same and is_y_same:
            return  # no need to close

        self.x_list.append(self.x_list[0])
        self.y_list.append(self.y_list[0])

    def plot(self):
        plt.plot(self.x_list, self.y_list, "-k")
 """
class scenarios:
    def __init__(self):
        self.x = 0
        self.map_dim = [-1, 11, -1, 11]    # [x1, x2, y1, y2]
    
    def scenario_0(map_dim):   # Empty map
        # ox, oy, map = Maps.get_map_P_empty_demo(map_dim)   # Map1, Payam Squares
        ox, oy, map = Maps.get_map_P_demo(map_dim)   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_1():
        ox, oy, map = Maps.get_map_P1()   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_2():     
        ox, oy, map = Maps.get_map_P2()   # Map2, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_3():
        ox, oy, map = Maps.get_map_P3()   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_C1():   # scenario non convex 1
        ox, oy, map = Maps.get_map_C1()   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_C2():   # scenario non convex 1
        ox, oy, map = Maps.get_map_C2()   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_C3():   # scenario non convex 1
        ox, oy, map = Maps.get_map_C3()   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_C4():   # scenario non convex 1
        ox, oy, map = Maps.get_map_C4()   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius

    def scenario_C5():   # scenario non convex 1
        ox, oy, map = Maps.get_map_C5()   # Map1, Payam Squares
        sx, sy, gx, gy, grid_size, robot_radius = Maps.init_P1()
        return ox, oy, map, sx, sy, gx, gy, grid_size, robot_radius


class Metrics:
    def __init__(self, path, x, y):
		#self.path = path
        self.x = x
        self.y = y
			
    def get_path_length( path):
        le = 0
        for i in range(len(path) - 1):
            dx = path[i + 1][0] - path[i][0]
            dy = path[i + 1][1] - path[i][1]
            d = math.sqrt(dx * dx + dy * dy)
            le += d
        return le

    def path_length( x, y):
        le = 0
        for i in range(len(x) - 1):
            dx = x[i + 1] - x[i]
            dy = y[i + 1] - y[i]
            d = math.sqrt(dx * dx + dy * dy)
            le += d
        return le

class manageData:
    def __init__(self):
        self.x = 0

    def saveData(algorithm, map, sx, sy, gx, gy, rx, ry, len, iter, Setup):
        with open('AlgorithmData.csv', mode='a+') as csv_file:
            fieldnames = ['Algorithm', 'Map', 'start_x', 'start_y', 'goal_x', 'goal_y', 'x_coord', 'y_coord', 'Path_length', 'Iteration', 'Setup']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Algorithm': algorithm, 'Map': map, 'start_x': sx, 'start_y': sy, 'goal_x': gx, 'goal_y': gy, 'x_coord': rx, 'y_coord': ry, 'Path_length': len, 'Iteration': iter, 'Setup':Setup})

    def create_csv_file():
        with open('AlgorithmData.csv', mode='a+') as csv_file:
            fieldnames = ['Algorithm', 'Map', 'start_x', 'start_y', 'goal_x', 'goal_y', 'x_coord', 'y_coord', 'Path_length', 'Iteration', 'Setup']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
			
class Maps:
    def __init__(self, map_dim):
        #self.map_dim = [-1, 102, -1, 102]    # [x1, x2, y1, y2]
        self.map_dim = map_dim

    def get_map_N1(): #Polygons Nacho 1
        # dx, dy, cost
        map1 = [ObstaclePolygon(
				[12.0, 24.0, 15.0, 7.0],
				[3.0, 14.0, 20.0, 14.0],
			),
			ObstaclePolygon(
				[12.0, 20.0, 25.0, 16.0, 7.0],
				[40.0, 40.0, 60.0, 70.0, 60.0],
			),
			ObstaclePolygon(
				[10.0, 40.0, 30.0],
				[85.0, 80.0, 60.0],
			),
		   ObstaclePolygon(
				[25.0, 30.0, 50.0, 30.0],
				[40.0, 30.0, 40.0, 50.0],
			), 
		   ObstaclePolygon(
				[40.0, 50.0, 60.0, 60.0, 50.0, 40.0],
				[55.0, 50.0, 55.0, 65.0, 70.0, 65.0],
			),
			ObstaclePolygon(
				[50.0, 75.0, 75.0, 50.0],
				[15.0, 15.0, 30.0, 30.0],
			),
			ObstaclePolygon(
				[70.0, 98.0, 95.0],
				[2.0, 5.0, 20.0],
			),    
			ObstaclePolygon(
				[75.0, 60.0, 75.0],
				[40.0, 80.0, 90.0],
			),    
			]
        return map1

    def get_map_P1(): # Obstacles using walls
        # set obstacle positions
            map = 'P1'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(15, 25):
                ox.append(i)
                oy.append(15)
            for i in range(15, 26):
                ox.append(i)
                oy.append(25)
            for i in range(15, 25):
                ox.append(15)
                oy.append(i)
            for i in range(15, 25):
                ox.append(25)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(75, 85):
                ox.append(i)
                oy.append(85)
            for i in range(75, 85):
                ox.append(i)
                oy.append(95)
            for i in range(85, 95):
                ox.append(75)
                oy.append(i)
            for i in range(85, 96):
                ox.append(85)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy, map
    
    def init_P1():
    # start and goal position
        sx = 0  # [m]
        sy = 0  # [m]
        gx = 100  # [m]
        gy = 100  # [m]
        grid_size = 1  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

    
    def get_map_P1A_empty(): #Circles 
            map = 'P1A_empty'
            obstacleList = [ ]  # [x, y, radius]
            return obstacleList, map

    
    def get_map_P1A(): #Circles 
            map = 'P1A'
            obstacleList = [(20, 20, 5*math.sqrt(2)), (80, 90, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList, map

    
    def get_map_P1B_empty(): #Polygons, Payam Version For Visibility Graph
        map = 'P1B_empty'
        map1 = [
			]
        return map1, map

    
    def get_map_P1B(): #Polygons, Payam Version For Visibility Graph
        map = 'P1B'
        map1 = [ObstaclePolygon(
				[15.0, 25.0, 25.0, 15.0],
				[15.0, 15.0, 25.0, 25.0],
			),
			ObstaclePolygon(
				[75.0, 85.0, 85.0, 75.0],
				[85.0, 85.0, 95.0, 95.0],
			),
			]
        return map1, map

    
    def get_map_P2(): # Obstacles using walls
        # set walls
            map = 'P2'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(40, 50):
                ox.append(i)
                oy.append(40)
            for i in range(40, 51):
                ox.append(i)
                oy.append(50)
            for i in range(40, 50):
                ox.append(40)
                oy.append(i)
            for i in range(40, 50):
                ox.append(50)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(40, 50):
                ox.append(i)
                oy.append(60)
            for i in range(40, 51):
                ox.append(i)
                oy.append(70)
            for i in range(60, 70):
                ox.append(40)
                oy.append(i)
            for i in range(60, 70):
                ox.append(50)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy, map
    
    def init_P2():
    # start and goal position
        sx = 45  # [m]
        sy = 0  # [m]
        gx = 45  # [m]
        gy = 100  # [m]
        grid_size = 1  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

    
    def get_map_P2A(): #Circles 
            map = 'P2A'
            obstacleList = [(45, 45, 5*math.sqrt(2)), (45, 65, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList, map

    
    def get_map_P2B(): #Polygons, PAyam Version For Visibility Graph
        map = 'P2B'
        map1 = [ObstaclePolygon(
				[40.0, 50.0, 50.0, 40.0],
				[40.0, 40.0, 50.0, 50.0],
			),
			ObstaclePolygon(
				[40.0, 50.0, 50.0, 40.0],
				[60.0, 60.0, 70.0, 70.0],
			),
			]
        return map1, map

#########################################################################################################
   
    def get_map_P3(): # Obstacles using walls
        # set walls
            map = 'P3'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(40, 50):
                ox.append(i)
                oy.append(40)
            for i in range(40, 50):
                ox.append(i)
                oy.append(50)
            for i in range(40, 50):
                ox.append(40)
                oy.append(i)
            for i in range(40, 51):
                ox.append(50)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(60, 70):
                ox.append(i)
                oy.append(60)
            for i in range(60, 70):
                ox.append(i)
                oy.append(70)
            for i in range(60, 70):
                ox.append(60)
                oy.append(i)
            for i in range(60, 71):
                ox.append(70)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy, map
    
    def init_P3():
    # start and goal position
        sx = 0  # [m]
        sy = 0  # [m]
        gx = 100  # [m]
        gy = 100  # [m]
        grid_size = 1  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

    def get_map_P3A(): #Circles 
            map = 'P3A'
            obstacleList = [(45, 45, 5*math.sqrt(2)), (65, 65, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList, map

    def get_map_P3B(): #Polygons, PAyam Version For Visibility Graph
        map = 'P3B'
        map1 = [ObstaclePolygon(
				[40.0, 50.0, 50.0, 40.0],
				[40.0, 40.0, 50.0, 50.0],
			),
			ObstaclePolygon(
				[60.0, 70.0, 70.0, 60.0],
				[60.0, 60.0, 70.0, 70.0],
			),
			]
        return map1, map

#########################################################################################################
#   For scenario 4, teh map is the same in P2 with different start and end points

    def init_P4():
    # start and goal position
        sx = 0  # [m]
        sy = 45  # [m]
        gx = 100  # [m]
        gy = 45  # [m]
        grid_size = 1  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

###########################################################################################################
# A naive empty map obstacles for Test
    
#    @staticmethod
    def get_map_P_empty(): # Obstacles using walls
        # set walls
            map = 'P_empty'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

            return ox, oy, map
#@staticmethod
    def get_map_P_empty_v2(map_dim): # Obstacles using walls
        # set walls
            map = 'P_empty'
            ox, oy = [], []
            for i in range(map_dim[0], map_dim[1]):
                ox.append(i)
                oy.append(map_dim[2])
            for i in range(map_dim[2],map_dim[3]+1):
                ox.append(map_dim[1])
                oy.append(i)
            for i in range(map_dim[0], map_dim[1]):
                ox.append(i)
                oy.append(map_dim[3])
            for i in range(map_dim[2],map_dim[3]):
                ox.append(map_dim[0])
                oy.append(i)
            return ox, oy, map

    def get_map_P_demo(map_dim): # Obstacles using walls
        # set walls
            map = 'P_empty'
            ox, oy = [], []
            for i in range(map_dim[0], map_dim[1]):
                ox.append(i)
                oy.append(map_dim[2])
            for i in range(map_dim[2],map_dim[3]+1):
                ox.append(map_dim[1])
                oy.append(i)
            for i in range(map_dim[0], map_dim[1]):
                ox.append(i)
                oy.append(map_dim[3])
            for i in range(map_dim[2],map_dim[3]):
                ox.append(map_dim[0])
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(4, 8):
                ox.append(i)
                oy.append(4)
            for i in range(4, 9):
                ox.append(i)
                oy.append(8)
            for i in range(4, 8):
                ox.append(4)
                oy.append(i)
            for i in range(4, 8):
                ox.append(8)
                oy.append(i)

            return ox, oy, map

##########################################################################################
    def get_map(map_dim, obstacles): # Obstacles using walls
        # set walls
            map = 'P_empty'
            ox, oy = [], []
            for i in range(map_dim[0], map_dim[1]):
                ox.append(i)
                oy.append(map_dim[2])
            for i in range(map_dim[2],map_dim[3]+1):
                ox.append(map_dim[1])
                oy.append(i)
            for i in range(map_dim[0], map_dim[1]):
                ox.append(i)
                oy.append(map_dim[3])
            for i in range(map_dim[2],map_dim[3]):
                ox.append(map_dim[0])
                oy.append(i)
            return ox, oy, map

###########################################################################################
# New group of maps
    
    def get_map_C1(): # Map complex1
        # set obstacle positions
            map = 'C1'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(15, 50):
                ox.append(i)
                oy.append(15)
            for i in range(15, 51):
                ox.append(i)
                oy.append(50)
            for i in range(15, 50):
                ox.append(15)
                oy.append(i)
            for i in range(15, 50):
                ox.append(50)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(50, 85):
                ox.append(i)
                oy.append(85)
            for i in range(50, 85):
                ox.append(i)
                oy.append(95)
            for i in range(85, 95):
                ox.append(50)
                oy.append(i)
            for i in range(85, 96):
                ox.append(85)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy, map
###################################################################
    @staticmethod
    def get_map_C2(): # Map complex1
        # set obstacle positions
            map = 'C2'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(15, 50):
                ox.append(i)
                oy.append(15)
            for i in range(15, 51):
                ox.append(i)
                oy.append(50)
            for i in range(15, 50):
                ox.append(15)
                oy.append(i)
            for i in range(15, 50):
                ox.append(50)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(50, 50):
                ox.append(i)
                oy.append(85)
            for i in range(50, 50):
                ox.append(i)
                oy.append(95)
            for i in range(50, 95):
                ox.append(50)
                oy.append(i)
            for i in range(50, 96):
                ox.append(50)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy, map      
#######################################################################
#     @staticmethod
    def get_map_C3(): # Map complex1
        # set obstacle positions
            map = 'C3'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(15, 50):
                ox.append(i)
                oy.append(15)
            for i in range(15, 51):
                ox.append(i)
                oy.append(50)
            for i in range(15, 50):
                ox.append(15)
                oy.append(i)
            for i in range(15, 50):
                ox.append(50)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(50, 85):
                ox.append(i)
                oy.append(95)
            for i in range(50, 85):
                ox.append(i)
                oy.append(50)
            for i in range(50, 95):
                ox.append(50)
                oy.append(i)
            for i in range(50, 96):
                ox.append(85)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy, map  

#######################################################################
#     @staticmethod
    def get_map_C4(): # Map complex1
        # set obstacle positions
            map = 'C4'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(15, 95):
                ox.append(i)
                oy.append(95)
            for i in range(15, 96):
                ox.append(i)
                oy.append(85)
            for i in range(85, 95):
                ox.append(15)
                oy.append(i)
            for i in range(85, 95):
                ox.append(95)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(85, 95):
                ox.append(i)
                oy.append(85)
            for i in range(85, 95):
                ox.append(i)
                oy.append(25)
            for i in range(25, 85):
                ox.append(85)
                oy.append(i)
            for i in range(25, 86):
                ox.append(95)
                oy.append(i)
            #print('ox =', ox)
            # Third rectangle obstacle
            for i in range(15, 95):
                ox.append(i)
                oy.append(15)
            for i in range(15, 96):
                ox.append(i)
                oy.append(25)
            for i in range(15, 25):
                ox.append(15)
                oy.append(i)
            for i in range(15, 25):
                ox.append(95)
                oy.append(i)
            return ox, oy, map  

#######################################################################
#     @staticmethod
    def get_map_C5(): # Map complex1
        # set obstacle positions
            map = 'C5'
            ox, oy = [], []
            for i in range(-1, 102):
                ox.append(i)
                oy.append(-1)
            for i in range(-1, 103):
                ox.append(102)
                oy.append(i)
            for i in range(-1, 102):
                ox.append(i)
                oy.append(102)
            for i in range(-1, 102):
                ox.append(-1)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(15, 95):
                ox.append(i)
                oy.append(95)
            for i in range(15, 96):
                ox.append(i)
                oy.append(85)
            for i in range(85, 95):
                ox.append(15)
                oy.append(i)
            for i in range(85, 95):
                ox.append(95)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(85, 95):
                ox.append(i)
                oy.append(85)
            for i in range(85, 95):
                ox.append(i)
                oy.append(25)
            for i in range(25, 85):
                ox.append(15)
                oy.append(i)
            for i in range(25, 86):
                ox.append(25)
                oy.append(i)
            #print('ox =', ox)
            # Third rectangle obstacle
            for i in range(15, 95):
                ox.append(i)
                oy.append(15)
            for i in range(15, 96):
                ox.append(i)
                oy.append(25)
            for i in range(15, 25):
                ox.append(15)
                oy.append(i)
            for i in range(15, 25):
                ox.append(95)
                oy.append(i)
            return ox, oy, map  

    def get_map_C1A(): #Circles 
            map = 'C1A'
            obstacleList = [(32.5, 32.5, 17.5*math.sqrt(2)), 
            (55, 90, 5*math.sqrt(2)), (65, 90, 5*math.sqrt(2)), (75, 90, 5*math.sqrt(2)), (80, 90, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList, map

    def get_map_C2A(): #Circles 
            map = 'C2A'
            obstacleList = [(32.5, 32.5, 17.5*math.sqrt(2)),
            (50, 65, 5*math.sqrt(2)), (50, 75, 5*math.sqrt(2)), (50, 75, 5*math.sqrt(2)), (50, 85, 5*math.sqrt(2)),
            (50, 90, 5*math.sqrt(2)), (50, 58, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList, map            
            
    def get_map_C3A(): #Circles 
            map = 'C3A'
            obstacleList = [(32.5, 32.5, 17.5*math.sqrt(2)),
            (67.5, 67.5, 17.5*math.sqrt(2)), (67.5, 70.25, 17.5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList, map

    def get_map_C4A(): #Circles 
            map = 'C4A'
            obstacleList = [(20, 20, 5), 
            (30, 20, 5), (40, 20, 5), (50, 20, 5), (60, 20, 5), (70, 20, 5), (80, 20, 5), (90, 20, 5),
            (90, 30, 5), (90, 40, 5), (90, 50, 5), (90, 60, 5), (90, 70, 5), (90, 80, 5), (90, 90, 5),
            (20, 90, 5), (30, 90, 5), (40, 90, 5), (50, 90, 5), (60, 90, 5), (70, 90, 5), (80, 90, 5)]  # [x, y, radius]
            return obstacleList, map

    def get_map_C5A(): #Circles 
            map = 'C5A'
            obstacleList = [(20, 20, 5),    
            (30, 20, 5), (40, 20, 5), (50, 20, 5), (60, 20, 5), (70, 20, 5), (80, 20, 5), (90, 20, 5),
            (20, 30, 5), (20, 40, 5), (20, 50, 5), (20, 60, 5), (20, 70, 5), (20, 80, 5), (20, 90, 5),
            (90, 90, 5), (30, 90, 5), (40, 90, 5), (50, 90, 5), (60, 90, 5), (70, 90, 5), (80, 90, 5)]  # [x, y, radius]
            return obstacleList, map

    ####################################################################################

    def get_map_C1B(): #Polygons, PAyam Version For Visibility Graph
            map = 'C1B'
            map1 = [ObstaclePolygon(
                    [15, 50, 50, 15],
                    [15, 15, 50, 50],
                ),
                ObstaclePolygon(
                    [50, 85, 85, 50],
                    [85, 85, 95, 95],
                ),
                ]
            return map1, map

    def get_map_C2B(): #Polygons, PAyam Version For Visibility Graph
            map = 'C2B'
            map1 = [ObstaclePolygon(
                    [15, 50, 50, 15],
                    [15, 15, 50, 50],
                ),
                ObstaclePolygon(
                    [50, 50],
                    [50, 95],
                ),
                ]
            return map1, map

    def get_map_C3B(): #Polygons, PAyam Version For Visibility Graph
            map = 'C3B'
            map1 = [ObstaclePolygon(
                    [15, 50, 50, 15],
                    [15, 15, 50, 50],
                ),
                ObstaclePolygon(
                    [50, 85, 85, 50],
                    [50, 50, 95, 95],
                ),
                ]
            return map1, map

    def get_map_C4B(): #Polygons, PAyam Version For Visibility Graph
            map = 'C4B'
            map1 = [ObstaclePolygon(
                    [15, 95, 95, 15, 15, 85, 85, 15],
                    [15, 15, 95, 95, 85, 85, 25, 25],
                ),
                ]
            return map1, map

    def get_map_C5B(): #Polygons, PAyam Version For Visibility Graph
            map = 'C5B'
            map1 = [ObstaclePolygon(
                    [15, 95, 95, 25, 25, 95, 95, 15],
                    [15, 15, 25, 25, 85, 85, 95, 95],
                ),
                ]
            return map1, map
