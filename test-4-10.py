# -*- coding: utf-8 -*-
# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------
#注意的是，“怎么到这一格的动作”和“到下一格的动作”意义是不同的。
#我们在每一个格子中要输出的是“到下一格的动作”，所以最后要从终点往起点逆推
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0], # go left
         [ 0,-1], # go up
         [ 1, 0], # go rigth
         [ 0, 1]] # go down


delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    expand = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    expand[init[0]][init[1]] = 0
    closed = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    closed[init[0]][init[1]] = 1
    action = [['' for i in range(len(grid[0]))] for i in range(len(grid))]
    action[goal[0]][goal[1]] = '*'

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
                            action[x2][y2] = i

    policy = [[' '] * len(grid[0]) for i in grid]
    x = goal[0]
    y = goal[1]
    policy[x][y] = '*'
    while x != init[0] and y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2

    for i in range(len(policy)):
        print(policy[i])

search(grid,init,goal,cost)