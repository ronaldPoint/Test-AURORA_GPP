from numpy import equal
import pandas as pd


# Load data from experiment results file

pd.options.display.max_columns = None   # Shows all columns of DataFrame

df_PP = pd.read_csv('AlgorithmData_Test.csv', 
                            sep=',', 
                            header=0) # header=0 --> the header is in the first line (line[0])

# Data clean and correction
# Drop all empty records. Empty lines that appears in the data generation
# Drop all registers with NaN values in the Algorithm field

df_PP = df_PP[df_PP['Algorithm'].notna()]
# Change data P1_B by P1B to have an homogenious pattern
df_PP.Map = df_PP.Map.replace({"P1_B": 'P1B'})

# Drop registers with values distinct from zero in start and goal fields
df_PP = df_PP.drop(df_PP[df_PP['start_x'] == 45 ].index) 
df_PP = df_PP.drop(df_PP[df_PP['start_y'] == 45 ].index) 
df_PP = df_PP.drop(df_PP[df_PP['goal_x'] == 45 ].index) 
df_PP = df_PP.drop(df_PP[df_PP['goal_y'] == 45 ].index)

# Drops the columns with zero or constant values

df_PP.drop(['start_x', 'start_y', 'goal_x', 'goal_y','x_coord', 'y_coord'], 1, inplace=True)

# Add new columns with information generated from existing data
# Create new column with conditionals
df_PP['Obstacle_type'] = df_PP['Map'].apply(lambda x: 'Concave' if x == 'C3' or x == 'C3A' or x == 'C3B'
                                                    or x == 'C4' or x == 'C4A' or x == 'C4B'
                                                    or x == 'C5' or x == 'C5A' or x == 'C5B'
                                                    else 'Convex')

df_PP['Algorithm_Type'] = df_PP['Algorithm'].apply(lambda x: 'Deterministic' if (x == 'A_Star' or 
                                                    x == 'Bidirectional_A_Star' or x == 'Bidirectional_BFS' 
                                                    or x == 'BFS' or x == 'DFS' or x == 'Dijkstra'
                                                    or x == 'D_Star' or x == 'Greedy_BFS' or 
                                                    x == 'Visibility_Road_Map') else 'Probabilistic')

# Agrego campo Q_obst (cantidad de cuadros -nodos- ocupados por los obstaculosen cada scenario)
df_PP['Q_obstacle'] = df_PP['Map'].apply(lambda x: 0 if x == 'P_empty' or x == 'P1A_empty' or x == 'P1B_empty' 
                                                    else (242 if x == 'P1' or x == 'P1A' or x == 'P1B'
                                                    or x == 'P2' or x == 'P2A' or x == 'P2B'
                                                    or x == 'P3' or x == 'P3A' or x == 'P3B' 
                                                    else (1692 if x == 'C1' or x == 'C1A' or x == 'C1B'
                                                    else (1342 if x == 'C2' or x == 'C2A' or x == 'C2B'
                                                    else (2952 if x == 'C3' or x == 'C3A' or x == 'C3B'
                                                    else 2431)))))

# Split the Dataframe in two. The first one is for the Scenarios with Convex obstacles and the second one 
# with the Concave obstacles

groups = df_PP.groupby(df_PP.Obstacle_type)
groups2 = df_PP.groupby(df_PP.Setup)

df_setup_0 = groups2.get_group(0)
df_setup_not_0 = df_PP.drop(df_PP[df_PP['Setup'] == 0].index)

df_convex = groups.get_group('Convex')
df_convex = df_convex.drop_duplicates(['Setup', 'Algorithm', 'Map'], keep="last")
# df_convex
df_concave = groups.get_group('Concave')
df_concave = df_concave.drop_duplicates(['Setup', 'Algorithm', 'Map'], keep="last")


# Save new data in a file csv
df_PP.to_csv('dataBase_final.csv')


#  PLOTS FOR ANALYSIS
#  Import needed libraries, to plot with seaborn 
import warnings
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import seaborn as sns

# Bar plot
# tips = sns.load_dataset("df_PP")
# sns.FacetGrid(tips)
# g = sns.FacetGrid(df_convex, col="Algorithm", row="Algorithm_Type", margin_titles=True)
# g.map_dataframe(sns.scatterplot, x="Iteration", y="Path_length")
# It is possible to analyze by groups
degrees = 45
plt.xticks(rotation=degrees)
plt.title('Probabilistic Algorithms with Concave Obstacle Shapes \nInfluence of Expand Distance Parameter')

sns.boxplot(x="Algorithm", y="Iteration", hue="Setup", data=df_setup_not_0)

fig.tight_layout()
fig.savefig('BoxPlot_setup_not0_Iteration.svg', bbox_inches='tight')