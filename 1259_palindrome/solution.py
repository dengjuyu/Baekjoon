import sys

def solve():
    while True:
        num = sys.stdin.readline().strip()
        if num == "0":  # 입력이 "0"이면 종료
            break
        print("yes" if num == num[::-1] else "no")

if __name__ == '__main__':
    solve()