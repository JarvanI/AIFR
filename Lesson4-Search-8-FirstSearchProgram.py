# -*- coding: utf-8 -*-
# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go left
         [ 0,-1], # go up
         [ 1, 0], # go rigth
         [ 0, 1]] # go down

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------

    #To check the cells once they are expanded, and to not expand them again
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    #or closed = [[0] * len(grid[0]) for i in grid]

    #set the value of the starting cell to 1, since you are expanding it.
    closed[init[0]][init[1]] = 1

    #Set the initial values for x, y and g and initialize open like this:
    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]

    #set two flag values:
    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand , important when you can not find a path to a goal after searching all possible locations.

    while not found and not resign:
        #遍历完所有表格后仍找不到路径，返回fail
        if len(open) == 0:
            resign = True
            return "fail"

        #当还有路走时
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

        #当前已经找到终点
        if x == goal[0] and y == goal[1]:
            found = True

        #有路走，且还没找到终点
        else:
            for i in range(len(delta)):
                x2 = x + delta[i][0]
                y2 = y + delta[i][1]

                #还在表格范围内，上下左右各走一步并记录
                if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                    if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                        g2 = g + cost
                        open.append([g2, x2, y2])
                        closed[x2][y2] = 1
    print(next)
    return next

search(grid,init,goal,cost)