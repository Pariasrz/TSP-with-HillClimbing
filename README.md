# TSP-with-HillClimbing

Travelling Salesman Problem implementation with Hill Climbing Algorithm

##Input
Input of this algorithm is a 2D array of coordinate of cities. For example: 

```
coordinate = np.array([[1,2], [30,21], [56,23], [8,18], [20,50], [3,4], [11,6], [6,7], [15,20], [10,9], [12,12], [46,17], [60,55], [100,80], [16,13]])
```

##Output
Output of the algorithm is a list of integers which indicates numbers of cities order(starts from zero) and the lenght of the path. For example: 

```
The solution is 
 [3, 7, 5, 0, 6, 9, 10, 14, 8, 1, 11, 2, 13, 12, 4] 
The path length is 
 283.8355158499078
 ```
 
 There is a function names "graph" which can draw the graph of the cities. (nodes are the numbers of the cities. The first city's node color is green.) For example:
 
 ![Graph](https://github.com/Pariasrz/TSP-with-HillClimbing/blob/main/Figure.png)

                       
