#!/usr/bin/python# -*- coding: utf-8 -
# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost, heuristic):
    expand = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    expand[init[0]][init[1]] = 0
    closed = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h
    open = [[f, x, y, g, h]]

    found = False
    resign = False
    count = 0
    while not found and not resign:
        if len(open) == 0:
            resign == True
            break
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            f = next[0]
            x = next[1]
            y = next[2]
            g = next[3]
            h = next[4]
            expand[x][y] = count
            count += 1

            if next[1] == goal[0] and next[2] == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    #为
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, x2, y2, g2, h2])
                            closed[x2][y2] = 1


    for i in range(len(expand)):
            print(expand[i])
    return expand

search(grid, init, goal, cost,heuristic)
