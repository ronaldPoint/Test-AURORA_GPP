
import math
import matplotlib.pyplot as plt

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
		
			
class Maps:
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

    @staticmethod
    def get_map_P1(): # Obstacles using walls
        # set obstacle positions
            ox, oy = [], []
            for i in range(-10, 110):
                ox.append(i)
                oy.append(-10)
            for i in range(-10, 111):
                ox.append(110)
                oy.append(i)
            for i in range(-10, 110):
                ox.append(i)
                oy.append(110)
            for i in range(-10, 110):
                ox.append(-10)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(14, 26):
                ox.append(i)
                oy.append(14.0)
            for i in range(14, 27):
                ox.append(i)
                oy.append(26.0)
            for i in range(14, 26):
                ox.append(14.0)
                oy.append(i)
            for i in range(14, 26):
                ox.append(26.0)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(74, 86):
                ox.append(i)
                oy.append(85.0)
            for i in range(74, 86):
                ox.append(i)
                oy.append(96.0)
            for i in range(85, 96):
                ox.append(74.0)
                oy.append(i)
            for i in range(85, 97):
                ox.append(86.0)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy
    
    @staticmethod
    def init_P1():
    # start and goal position
        sx = 0  # [m]
        sy = 0  # [m]
        gx = 100  # [m]
        gy = 100  # [m]
        grid_size = 2  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

    @staticmethod
    def get_map_P1A(): #Circles 
            obstacleList = [(20, 20, 5*math.sqrt(2)), (80, 90, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList

    @staticmethod
    def get_map_P1B(): #Polygons, PAyam Version For Visibility Graph
        map1 = [ObstaclePolygon(
				[14.0, 26.0, 26.0, 14.0],
				[14.0, 14.0, 26.0, 26.0],
			),
			ObstaclePolygon(
				[74.0, 85.0, 85.0, 74.0],
				[86.0, 86.0, 96.0, 96.0],
			),
			]
        return map1

    @staticmethod
    def get_map_P2(): # Obstacles using walls
        # set walls
            ox, oy = [], []
            for i in range(-10, 110):
                ox.append(i)
                oy.append(-10)
            for i in range(-10, 111):
                ox.append(110)
                oy.append(i)
            for i in range(-10, 110):
                ox.append(i)
                oy.append(110)
            for i in range(-10, 110):
                ox.append(-10)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(39, 51):
                ox.append(i)
                oy.append(39)
            for i in range(39, 51):
                ox.append(i)
                oy.append(51)
            for i in range(39, 51):
                ox.append(39)
                oy.append(i)
            for i in range(39, 51):
                ox.append(51)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(39, 51):
                ox.append(i)
                oy.append(59)
            for i in range(39, 51):
                ox.append(i)
                oy.append(71)
            for i in range(59, 71):
                ox.append(39)
                oy.append(i)
            for i in range(59, 71):
                ox.append(51)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy
    @staticmethod
    def init_P2():
    # start and goal position
        sx = 45  # [m]
        sy = 0  # [m]
        gx = 45  # [m]
        gy = 100  # [m]
        grid_size = 2  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

    @staticmethod
    def get_map_P2A(): #Circles 
            obstacleList = [(45, 45, 5*math.sqrt(2)), (45, 65, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList

    @staticmethod
    def get_map_P2B(): #Polygons, PAyam Version For Visibility Graph
        map1 = [ObstaclePolygon(
				[39.0, 51.0, 51.0, 39.0],
				[39.0, 39.0, 51.0, 51.0],
			),
			ObstaclePolygon(
				[39.0, 51.0, 51.0, 39.0],
				[59.0, 59.0, 71.0, 71.0],
			),
			]
        return map1

#########################################################################################################
    @staticmethod
    def get_map_P3(): # Obstacles using walls
        # set walls
            ox, oy = [], []
            for i in range(-10, 110):
                ox.append(i)
                oy.append(-10)
            for i in range(-10, 111):
                ox.append(110)
                oy.append(i)
            for i in range(-10, 110):
                ox.append(i)
                oy.append(110)
            for i in range(-10, 110):
                ox.append(-10)
                oy.append(i)

        # Fisrt rectangle obstacle
            for i in range(39, 51):
                ox.append(i)
                oy.append(39)
            for i in range(39, 51):
                ox.append(i)
                oy.append(51)
            for i in range(39, 51):
                ox.append(39)
                oy.append(i)
            for i in range(39, 52):
                ox.append(51)
                oy.append(i)
        # Seconde recatngle obstacle
            for i in range(59, 71):
                ox.append(i)
                oy.append(59)
            for i in range(59, 71):
                ox.append(i)
                oy.append(71)
            for i in range(59, 71):
                ox.append(59)
                oy.append(i)
            for i in range(59, 72):
                ox.append(71)
                oy.append(i)
            #print('ox =', ox)
            return ox, oy
    @staticmethod
    def init_P3():
    # start and goal position
        sx = 0  # [m]
        sy = 0  # [m]
        gx = 100  # [m]
        gy = 100  # [m]
        grid_size = 2  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

    @staticmethod
    def get_map_P3A(): #Circles 
            obstacleList = [(45, 45, 5*math.sqrt(2)), (65, 65, 5*math.sqrt(2))]  # [x, y, radius]
            return obstacleList

    @staticmethod
    def get_map_P3B(): #Polygons, PAyam Version For Visibility Graph
        map1 = [ObstaclePolygon(
				[39.0, 51.0, 51.0, 39.0],
				[39.0, 39.0, 51.0, 51.0],
			),
			ObstaclePolygon(
				[59.0, 71.0, 71.0, 59.0],
				[59.0, 59.0, 71.0, 71.0],
			),
			]
        return map1

#########################################################################################################
#   For scenario 4, teh map is the same in P2 with different start and end points
    @staticmethod
    def init_P4():
    # start and goal position
        sx = 0  # [m]
        sy = 45  # [m]
        gx = 100  # [m]
        gy = 45  # [m]
        grid_size = 2  # [m]
        robot_radius = 1  # [m]
        return sx, sy, gx, gy, grid_size, robot_radius

