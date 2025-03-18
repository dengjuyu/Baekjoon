from collections import deque

def bfs(N, K):
    MAX = 100000  # 문제에서 주어진 최대 범위
    visited = [-1] * (MAX + 1)  # 방문한 위치를 체크 & 걸린 시간을 저장하는 배열

    queue = deque([N])
    visited[N] = 0  # 시작 위치는 0초

    while queue:
        x = queue.popleft()

        # 동생의 위치 K에 도착하면 return
        if x == K:
            return visited[x]

        # 가능한 이동: x-1, x+1, x*2
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and visited[nx] == -1:  # 범위 내 & 방문하지 않은 곳
                visited[nx] = visited[x] + 1  # 시간 증가
                queue.append(nx)  # 큐에 추가

# 입력
N, K = map(int, input().split())
print(bfs(N, K))
