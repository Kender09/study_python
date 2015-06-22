size = list(map(int, input().split()))

# y, x
now_pos = [0, 0]
start_pos = [0, 0]
goal_pos = [0, 0]
#4方向移動ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

d = [[99999 for i in range(size[1])] for i in range(size[0])]

meiro_map = [[] for i in range(size[1])]
for i in range(size[1]):
    a = input()
    meiro_map[i].extend(a)

for i in range(size[1]):
    if meiro_map[i].count('S'):
        now_pos[0], now_pos[1] =  i, meiro_map[i].index('S')

for i in range(size[1]):
    if meiro_map[i].count('G'):
        goal_pos[0], goal_pos[1] =  i, meiro_map[i].index('G')

start_pos = now_pos

que = []
que.append(start_pos)
d[start_pos[0]][start_pos[1]] = 0
while len(que):
    p = que.pop(0)
    print (p, d[p[0]][p[1]])
    if (p == goal_pos):
        break;
    #４方向にループ
    for i in range(4):
        ny, nx = p[0] +dy[i], p[1] + dx[i]
        if 0 <=nx and nx < size[0] and 0 <= ny and ny < size[1] and meiro_map[ny][nx] != '#' and d[ny][nx] == 99999:
            #print('push', ny,nx)
            que.append([ny, nx])
            d[ny][nx] = d[p[0]][p[1]] + 1


print (d[goal_pos[0]][goal_pos[1]])
