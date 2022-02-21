> ***Taken form the Google doc file uploaded in the Teamwork platform***

### **GPP SCENARIOS (definitions):**



#### **SCENARIO 1**



1- The obstacles are assumed in a 10* 10 squares in a 100 * 100 square search space as shown below. 

2- I assumed three different scenarios in which obstacles are placed in (a) parallel, (b) behind each other, and (c) at the corners.

3- start and end point places are adopted based on the obstacles position in the assumed search space as illustrated below. 

4- X and Y coordinates are discretized in a 1 * 1 squares so that the A* algorithm will move along them to get to the goal point (endpoint) starting from the bottom left corner of the considered search space. 

5- size of the obstacles are based on the number of 1 * 1 squares in the search space, which by the way are flexible for any change on pre assumed (basic geometry shape of rectangular or square obstacles). (obstacles can be shaped as triangles or any other specific requested geometry). the developed A* algorithm is positively responsive to any considered geometry shape as obstacles. 

5.1 - Positioning of the obstacles in the first scenario: 

Bottom left obstacle (X(15:25) and Y(15:25)), and top right obstacle (X(75:85) and Y(85:95)).

5.2 - Positioning of the obstacles in the second scenario:

Bottom obstacle (X(40:50) and Y(40:50)), and the top obstacle (X(40:50) and Y(60:70)).

5.3 - Positioning of the obstacles in the third scenario:

Bottom obstacle (X(40:50) and Y(40:50)), and top obstacle (X(60:70) and Y(60:70)).

#### **SCENARIO 2**





### **SOLUTIONS**



SOLUTION APPROACH (A* algorithm in different scenarios):

Different scenarios are considered in this solution approach so that it can be used as a reference for further investigation of the global path planning. I explain the first, second, and third scenario and provide you with the achieved results in matlab. I used a heuristic A* algorithm for different scenarios of this proposed solution approach. Below you can find the results explained in details:

1- The obstacles are assumed in a 10* 10 squares in a 100 * 100 square search space as shown below. 

2- I assumed three different scenarios in which obstacles are placed in parallel, behind each other, and at the corners.

3- start and end point places are adopted based on the obstacles position in the assumed search space as illustrated below. 

4- X and Y coordinates are dicritized in a 1 * 1 squares so that the A* algorithm will move along them to get to the goal point (endpoint) starting from the bottom left corner of the considered search space. 

5- size of the obstacles are based on the number of 1 * 1 squares in the search space, which by the way are flexible for any change on pre assumed (basic geometry shape of rectangular or square obstacles). (obstacles can be shaped as triangles or any other specific requested geometry). the developed A* algorithm is positively responsive to any considered geometry shape as obstacles. 



Please take a look at the solution approach and see how obstacles are avoided in finding the shortest path between the start and end points in different scenarios. 

![img](https://lh6.googleusercontent.com/wxsU3Chc9u1teMZERQjmx4Sk6nncrgto3Npi-RSWS2TWBwmUhA8NwIacxyXOttkeLXUX0eZpBKJLPHg6t1-FZSEVZ0QBiwYqsHB27HD2UJ1Sne0IIV-loQ10Y_adECGlaltXon6s)



![img](https://lh4.googleusercontent.com/wcmdXNpN4fKbQxsQ7x1TUCC4kWAS4oCTDmNTC2zKaXM-w92uGYNmUwjRuVUZAEwKDgGaacA1VnWCCEQDjW4nKNNboqwuL_0cPprgCgB5sYGpqrjhuwZubj2v2KSRd0Dw5KAW0U1p)



![img](https://lh4.googleusercontent.com/hIRy11bWP6aYHvmvwPPU4_IH8qL90LnkzUIlDKS-8ii41UiyposUAfRWd4ZtXGYQkbsvSkwoTcKsF7HYT4gH933wQQahLUsgaNglZpvfKX5-rznb5chkHD_fn68gqd4VV8hNSBt_)



![img](https://lh5.googleusercontent.com/0Vz65yvwGGQY2f_aeSt1IfXA23W0EQ1jU99Wa3fyOuAhMThyizV8tVqV8kYlZORR94pNbCPxetugaLkOBJcQ-562NEnKtfx9bCiJc6nL4Ki-eklSslw9EXk_2tEH8Xn4pOGhvhoH)





### **ALGORITHMS COMPARISON**



**Scenario 1a**

|      | Criteria 1 | Criteria 2 | Criteria .. |      | Criteria n |
| ---- | ---------- | ---------- | ----------- | ---- | ---------- |
| A*   |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |



**Scenario 1b**

|      | Criteria 1 | Criteria 2 | Criteria .. |      | Criteria n |
| ---- | ---------- | ---------- | ----------- | ---- | ---------- |
| A*   |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |



**Scenario 1c**

|      | Criteria 1 | Criteria 2 | Criteria .. |      | Criteria n |
| ---- | ---------- | ---------- | ----------- | ---- | ---------- |
| A*   |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |
|      |            |            |             |      |            |



