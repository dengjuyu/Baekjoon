import sys
input = sys.stdin.readline

# 입력
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
purifiers = []
for i in range(R):
    if board[i][0] == -1:
        purifiers.append(i)
# purifiers = [위쪽_행, 아래쪽_행]

# 확산 함수
def spread():
    d = [( -1,0 ), (1,0), (0,-1), (0,1)]
    temp = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] > 0:
                amount = board[x][y] // 5
                cnt = 0
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        temp[nx][ny] += amount
                        cnt += 1
                board[x][y] -= amount * cnt
    # 확산된 먼지 더하기
    for x in range(R):
        for y in range(C):
            board[x][y] += temp[x][y]

# 공기청정기 작동 함수
def purify():
    up, down = purifiers

    # 위쪽: 반시계 방향
    # 위쪽 칸부터 위쪽 끝, 오른쪽 끝, 청정기 바로 위까지
    # 위쪽 루트
    # 1) 위로
    for i in range(up-1, 0, -1): board[i][0] = board[i-1][0]
    # 2) 왼→오
    for j in range(C-1): board[0][j] = board[0][j+1]
    # 3) 아래로
    for i in range(up): board[i][C-1] = board[i+1][C-1]
    # 4) 오→왼
    for j in range(C-1, 1, -1): board[up][j] = board[up][j-1]
    board[up][1] = 0  # 청정기로 들어오는 먼지

    # 아래쪽: 시계 방향
    # 1) 아래로
    for i in range(down+1, R-1): board[i][0] = board[i+1][0]
    # 2) 왼→오
    for j in range(C-1): board[R-1][j] = board[R-1][j+1]
    # 3) 위로
    for i in range(R-1, down, -1): board[i][C-1] = board[i-1][C-1]
    # 4) 오→왼
    for j in range(C-1, 1, -1): board[down][j] = board[down][j-1]
    board[down][1] = 0  # 청정기로 들어오는 먼지

# 시뮬레이션
for _ in range(T):
    spread()
    purify()

# 결과 출력
result = 0
for x in range(R):
    for y in range(C):
        if board[x][y] > 0:
            result += board[x][y]
print(result)
