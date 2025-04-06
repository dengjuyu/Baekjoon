import sys
from collections import deque

# 방향 벡터 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y, visited, graph, n, l, r):
    queue = deque([(x, y)])
    visited[x][y] = True
    union = [(x, y)]
    population = graph[x][y]
    count = 1

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 인구 차이 조건 검사
                if l <= abs(graph[cx][cy] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    population += graph[nx][ny]
                    count += 1

    # 인구 이동이 필요한 경우
    if count > 1:
        new_population = population // count
        for ux, uy in union:
            graph[ux][uy] = new_population

    return count > 1  # 인구 이동 발생 여부


if __name__ == '__main__':
    input_func = sys.stdin.readline
    n, l, r = map(int, input_func().split())
    graph = [list(map(int, input_func().split())) for _ in range(n)]
    days = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        moved = False

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    # 연합이 형성되면 인구 이동 발생
                    if bfs(i, j, visited, graph, n, l, r):
                        moved = True

        if not moved:
            break  # 인구 이동이 없는 경우 종료
        days += 1

    print(days)
