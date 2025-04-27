import sys
import copy
input = sys.stdin.readline

# 방향: 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 타입별 가능한 방향 조합
cctv_dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}

def watch(grid, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < N and 0 <= ny < M): break
            if grid[nx][ny] == 6:  # 벽
                break
            if grid[nx][ny] == 0:
                grid[nx][ny] = -1  # 감시 표시

def dfs(depth, grid):
    global ans
    if depth == len(cctvs):
        cnt = sum(row.count(0) for row in grid)
        ans = min(ans, cnt)
        return

    x, y, ctype = cctvs[depth]
    for dirs in cctv_dirs[ctype]:
        new_grid = copy.deepcopy(grid)
        watch(new_grid, x, y, dirs)
        dfs(depth+1, new_grid)

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))

ans = N * M  # 최댓값으로 초기화
dfs(0, office)
print(ans)
