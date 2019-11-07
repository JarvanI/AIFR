max = 99999
map = [[max for i in range(6)] for j in range(6)]
for i in range(6):
    map[i][i] = 0
map[0][1]=12
map[1][0]=12
map[2][3]=3
map[3][2]=3
map[1][2]=10
map[2][1]=10
map[3][4]=4
map[4][3]=4
map[2][5]=6
map[5][2]=6
map[0][5]=16
map[5][0]=16
map[4][5]=2
map[5][4]=2
map[1][5]=7
map[5][1]=7
map[2][4]=5
map[4][2]=5

init, goal = input().split()
init = ord(init)-65
goal = ord(goal)-65
lenth = len(map)
path = [0] * 6
cost = [0] * 6

v = [0]*lenth
for i in range(lenth):
    if i == init:
        v[init] = 1
    else:
        cost[i] = map[init][i]
        path[i] = (init if(cost[i]<max) else -1)
    for i in range(1,lenth):
        mincost = max
        curnode = -1
        for w in range(lenth):
            if v[w] == 0 and cost[w] < mincost:
                mincost = cost[w]
                curnode = w
        if curnode == -1: break
        v[curnode] = 1
        for w in range(lenth):
            if v[w] == 0 and (map[curnode][w] + cost[curnode] < cost [w]):
                cost[w] = map[curnode][w] + cost[curnode]
                path[w] = curnode

print(path)
#print(ord(init)-65,ord(goal)-65)
#for i in range(6):b
    #print(map[i])