# Main File to test Path Planning Algorithms 
import csv
import os
from pathlib import Path
import os.path as path
import pandas as pd


def create_csv_file():
    if ~path.exists('AlgorithmData.csv'):
        with open('AlgorithmData.csv', mode='a+') as csv_file:
            fieldnames = ['Algorithm', 'Map', 'start_x', 'start_y', 'goal_x', 'goal_y', 'x_coord', 'y_coord', 'Path_length', 'Iteration', 'Setup']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()



    
def main():
    create_csv_file()



if __name__ == '__main__':
    main()

 
 





