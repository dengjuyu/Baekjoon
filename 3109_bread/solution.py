import sys

sys.setrecursionlimit(10**6)
input_func = sys.stdin.read

data = input_func().split()
R, C = map(int, data[:2])
grid = [list(data[i + 2]) for i in range(R)]

dx = [-1, 0, 1]
dy = [1, 1, 1]

count = 0

def dfs(x, y):
    if y == C - 1:
        return True

    for d in range(3):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':
            grid[nx][ny] = 'x'
            if dfs(nx, ny):
                return True

    return False

for i in range(R):
    if grid[i][0] == '.':
        if dfs(i, 0):
            count += 1

print(count)
