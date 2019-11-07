# -*- coding: utf-8 -*-
# -----------
# User Instructions:
#
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid
# you return has the value 0.
# ----------


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right


delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    expand = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    expand[init[0]][init[1]] = 0
    closed = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0
    open = [[g, x, y]]

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
            g = next[0]
            x = next[1]
            y = next[2]
            expand[x][y] = count
            count += 1
            if next[1] == goal[0] and next[2] == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]

                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1


    for i in range(len(expand)):
        print(expand[i])
    return expand

search(grid,init,goal,cost)