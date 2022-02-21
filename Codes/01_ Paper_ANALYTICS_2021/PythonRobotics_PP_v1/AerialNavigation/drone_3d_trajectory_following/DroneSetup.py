# Simulation parameters

class DroneSetup():
    def __init__(self):
        return 

    def get_drone_parameters():
    # Simulation parameters
        g = 9.81
        m = 0.2
        Ixx = 1
        Iyy = 1
        Izz = 1
        T = 5

        # Proportional coefficients
        Kp_x = 1
        Kp_y = 1
        Kp_z = 1
        Kp_roll = 25
        Kp_pitch = 25
        Kp_yaw = 25

        # Derivative coefficients
        Kd_x = 10
        Kd_y = 10
        Kd_z = 1
        return g, m, Ixx, Iyy, Izz, T, Kp_x, Kp_y, Kp_z, Kp_roll, Kp_pitch, Kp_yaw, Kd_x, Kd_y, Kd_z


