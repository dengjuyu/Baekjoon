import sys
from collections import deque

def get_end_time(n, directions, apples):
    # 이동 방향: 동, 남, 서, 북 (오른쪽으로 회전하면 +1, 왼쪽으로 회전하면 -1)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    time = 0
    direction = 0
    snake = deque([(0, 0)])  # 초기 뱀 위치
    board = [[0] * n for _ in range(n)]
    board[0][0] = 2  # 뱀의 초기 위치 표시

    while True:
        # 1. 시간 증가
        time += 1

        # 2. 다음 머리 위치 계산
        head_x, head_y = snake[-1]
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]

        # 3. 충돌 검사 (벽 또는 자기 몸)
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            return time

        # 4. 머리 이동
        if (nx, ny) in apples:
            apples.remove((nx, ny))  # 사과 제거
        else:
            # 사과가 없으면 꼬리 제거
            tail_x, tail_y = snake.popleft()
            board[tail_x][tail_y] = 0  # 꼬리 자리 비우기

        # 머리를 다음 위치로 이동
        snake.append((nx, ny))
        board[nx][ny] = 2  # 뱀의 머리 표시

        # 5. 방향 전환 확인
        if time in directions:
            if directions[time] == 'D':  # 오른쪽 회전
                direction = (direction + 1) % 4
            elif directions[time] == 'L':  # 왼쪽 회전
                direction = (direction - 1) % 4

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().strip())  # 보드 크기
    k = int(input().strip())  # 사과 개수

    # 사과 위치 입력
    apples = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
    l = int(input().strip())  # 방향 전환 수
    directions = {}
    for _ in range(l):
        x, c = input().split()
        directions[int(x)] = c

    # 결과 출력
    print(get_end_time(n, directions, apples))
