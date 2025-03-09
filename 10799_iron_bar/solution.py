import sys

def solution():
    s = sys.stdin.readline().strip()  # 문자열 입력 받기
    stack = []  # 쇠막대기의 시작을 저장하는 스택
    total_pieces = 0  # 최종 잘려진 조각 수

    for i, char in enumerate(s):
        if char == "(":  # 여는 괄호이면 스택에 추가
            stack.append("(")
        else:  # 닫는 괄호 `)`인 경우
            stack.pop()  # 스택에서 하나 제거

            if s[i - 1] == "(":  # 이전 문자가 `(`이면 레이저!
                total_pieces += len(stack)  # 스택에 남은 쇠막대기 개수만큼 조각 증가
            else:  # 이전 문자가 `)`이면 쇠막대기 끝
                total_pieces += 1  # 막대기 끝이므로 조각 1개 추가

    print(total_pieces)

if __name__ == "__main__":
    solution()
