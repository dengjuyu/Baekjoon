import sys


def is_vps(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)  # 여는 괄호는 스택에 추가
        elif char == ')':
            if stack:  # 스택이 비어있지 않다면
                stack.pop()  # 짝을 맞추고 제거
            else:
                return "NO"  # 닫는 괄호가 많음 (잘못된 경우)

    return "YES" if not stack else "NO"  # 스택이 비어있으면 VPS


# 입력 처리
n = int(sys.stdin.readline().strip())  # 입력 개수
for _ in range(n):
    print(is_vps(sys.stdin.readline().strip()))