import pandas as pd


# Load data form the CSV file on a pandas container
df_test = pd.read_csv('AlgorithmData_Test.csv', 
                            sep=',', 
                            header=0) # header=0 --> the header is in the first line (line[0])

# Limpieza y correccion de datos
# eliminamos todos los registros vacios. Las lineas vacias que se crearon en la generacion de los datos
# Aplico la eliminacion para todos los registros que tengan NaN en el campo Algorithm

df_test = df_test[df_test['Algorithm'].notna()]
# Corregir el dato P1_B por P1B
df_test.Map = df_test.Map.replace({"P1_B": 'P1B'})
# print (df_test)

# Elimino los registros que tienen posiciones de star y/o end diferentes de cero
df_test = df_test.drop(df_test[df_test['start_x'] == 45 ].index)
df_test = df_test.drop(df_test[df_test['start_y'] == 45 ].index) 
df_test = df_test.drop(df_test[df_test['goal_x'] == 45 ].index)
df_test = df_test.drop(df_test[df_test['goal_y'] == 45 ].index)

# crear nueva columna a partir de las existentes. Con condicionales
df_test['Obstacle_type'] = df_test['Map'].apply(lambda x: 'Concave' if x == 'C3' or x == 'C3A' or x == 'C3B'
                                                    or x == 'C4' or x == 'C4A' or x == 'C4B'
                                                    or x == 'C5' or x == 'C5A' or x == 'C5B'
                                                    else 'Convex')

df_test['Algorithm Type'] = df_test['Algorithm'].apply(lambda x: 'Deterministic' if (x == 'A_Star' or 
                                                    x == 'Bidirectional_A_Star' or x == 'Bidirectional_BFS' 
                                                    or x == 'BFS' or x == 'DFS' or x == 'Dijkstra'
                                                    or x == 'D_Star' or x == 'Greedy_BFS' or 
                                                    x == 'Visibility_Road_Map') else 'Probabilistic')

# Agrego campo Q_obst (cantidad de cuadros -nodos- ocupados por los obstaculosen cada scenario)
df_test['Q_obstacle'] = df_test['Map'].apply(lambda x: 0 if x == 'P_empty' or x == 'P1A_empty' or x == 'P1B_empty' 
                                                    else (242 if x == 'P1' or x == 'P1A' or x == 'P1B'
                                                    or x == 'P2' or x == 'P2A' or x == 'P2B'
                                                    or x == 'P3' or x == 'P3A' or x == 'P3B' 
                                                    else (1692 if x == 'C1' or x == 'C1A' or x == 'C1B'
                                                    else (1342 if x == 'C2' or x == 'C2A' or x == 'C2B'
                                                    else (2952 if x == 'C3' or x == 'C3A' or x == 'C3B'
                                                    else 2431)))))

# Save new data in a file csv
df_test.to_csv('dataBase_final.csv')


