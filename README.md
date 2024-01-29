# TowerOfLondon

## main.py file
It defines a starting and a goal tower, then it creates a Tower object with such configurations. Finally, it calls the BFS algorithm to find the optimal sequence of moves to reach the goal configuration starting from the initial one. It is possible to custom both configurations.

The towers are implemented with python lists. Both starting and goal towers are represented with a list of three lists, each one representing the tower's posts: the first element of the list represents the first post (the one with three free spots), the second element of the list represents the second post (with two free spots), and the third element represents the third post (with only one free spots).