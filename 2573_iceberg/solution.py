import sys
from collections import deque

input = sys.stdin.readline

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

def count_icebergs(ice, N, M):
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0 and not visited[i][j]:
                cnt += 1
                queue = deque([(i,j)])
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if ice[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx,ny))
    return cnt

def melt_ice(ice, N, M):
    melt = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] > 0:
                water_count = 0
                for dx, dy in dirs:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] == 0:
                        water_count += 1
                melt[i][j] = water_count

    for i in range(N):
        for j in range(M):
            ice[i][j] = max(0, ice[i][j] - melt[i][j])

def main():
    N, M = map(int, input().split())
    ice = [list(map(int, input().split())) for _ in range(N)]
    year = 0

    while True:
        parts = count_icebergs(ice, N, M)
        if parts >= 2:
            print(year)
            return
        if parts == 0:
            print(0)
            return

        melt_ice(ice, N, M)
        year += 1

if __name__ == "__main__":
    main()
