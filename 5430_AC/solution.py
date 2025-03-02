import sys
from collections import deque


def solve_ac():
    t = int(sys.stdin.readline()) # 테스트 케이스 개수
    results = []

    for _ in range(t):
        func = sys.stdin.readline().strip() # 명령어 문자열(RDD, DRD, ...)
        n = int(sys.stdin.readline().strip()) # 배열 길이

        arr_input = sys.stdin.readline().strip() # 배열 입력 문자열

        if n == 0:
            arr = deque()
        else:
            arr = deque(map(int, arr_input[1:-1].split(","))) # "[1,2,3]" -> [1,2,3]

        results.append(reverse_or_delete(func, arr))

    return results

def reverse_or_delete(funcs, arr):
    reverse_flag = False # R이 나올 때마다 방향을 바꿔줄 플래그

    for f in funcs:
        if f == 'R':
            reverse_flag = not reverse_flag

        elif f == 'D':
            if not arr: # 배열이 비어있는 경우 "error" 반환
                return "error"
            if reverse_flag:
                arr.pop() # 뒤집힌 상태면 오른쪽에서 제거
            else:
                arr.popleft() # 정상 방향이면 왼쪽에서 제거

    return f"[{','.join(map(str, reversed(arr) if reverse_flag else arr))}]"


if __name__ == '__main__':
    print("\n".join(solve_ac()))