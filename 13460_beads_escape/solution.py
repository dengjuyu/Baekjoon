from collections import deque

import sys

# 상, 하, 좌, 우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, dx, dy):
    move_count = 0
    while strs[x + dx][y + dy] != '#' and strs[x][y] != 'O':
        x += dx
        y += dy
        move_count += 1
    return x, y, move_count


def bfs():
    queue = deque([(red_pos[0], red_pos[1], blue_pos[0], blue_pos[1], 0)])
    visited[red_pos[0]][red_pos[1]][blue_pos[0]][blue_pos[1]] = True

    while queue:
        rx, ry, bx, by, count = queue.popleft()

        # 이동 횟수가 10을 넘어가면 실패
        if count >= 10:
            return -1

        for i in range(4):
            nrx, nry, r_moves = move(rx, ry, dx[i], dy[i])
            nbx, nby, b_moves = move(bx, by, dx[i], dy[i])

            # 파란 구슬이 구멍에 빠지면 무효
            if strs[nbx][nby] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠지면 성공
            if strs[nrx][nry] == 'O':
                return count + 1

            # 두 구슬이 같은 위치에 있을 경우 처리
            if (nrx, nry) == (nbx, nby):
                if r_moves > b_moves:  # 이동거리가 더 큰 쪽이 뒤로 감
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 방문하지 않은 상태라면 큐에 추가
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, count + 1))

    # 실패 시
    return -1


if __name__ == '__main__':
    input_func = sys.stdin.readline
    n, m = map(int, input_func().split())

    strs = []
    red_pos, blue_pos = None, None

    for i in range(n):
        line = list(input_func().strip())
        for j in range(m):
            if line[j] == 'R':
                red_pos = (i, j)
                line[j] = '.'
            elif line[j] == 'B':
                blue_pos = (i, j)
                line[j] = '.'
        strs.append(line)

    # 방문 배열 초기화
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    # 결과 출력
    print(bfs())
