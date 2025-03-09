from collections import deque

m,n = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
wall = [1, 2, 4, 8]

visited = [[False] * m for _ in range(n)]
room_sizes = []
room_map = [[-1] * m for _ in range(n)]
room_id = 0

def bfs(sx, sy):
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    room_map[sx][sy] = room_id
    room_size = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if not (castle[x][y] & wall[d]):
                    visited[nx][ny] = True
                    room_map[nx][ny] = room_id
                    queue.append((nx, ny))
                    room_size += 1

    return room_size

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            room_sizes.append(bfs(i, j))
            room_id += 1

room_count = len(room_sizes)
print(room_count)

max_room_size = max(room_sizes)
print(max_room_size)

max_combined_size = 0
for x in range(n):
    for y in range(m):
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if room_map[x][y] != room_map[nx][ny]:
                    combined_size = room_sizes[room_map[x][y]] + room_sizes[room_map[nx][ny]]
                    max_combined_size = max(max_combined_size, combined_size)
print(max_combined_size)