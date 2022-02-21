***Taken form an email sent by Nacho***

The **Graph of Actions** (or **Action Graph**), which is colored in ***green***. As explained, the tessellated space is obtained by calculating the centroids of the obstacles and linking them in a way that we end up having a planar graph (colored in ***red***). Each cell has exactly 3 neighbors, so we must link the obstacles' centroids with the walls when necessary. In the action graph there is also an edge (represented in light green) that must pass through an obstacle. In fact that is not even a problem, since we should consider that the edges just show the neighborhood of both cells, not the actual spline tying them. 

 Besides, this week I would like to explore the different ways we can cross each cell. I think that these depend on the path taken on the 2/3 past cells and 2/3 future cells, but maybe not further away. Hope this complements the previous explanation.


![image](https://user-images.githubusercontent.com/69277604/119097363-eb04ba80-ba14-11eb-9cd8-1b2dd81b7959.png)



