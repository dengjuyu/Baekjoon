import sys
input_func = sys.stdin.readline

s = input_func().rstrip()
stack = []

pairs = {
    ')': ('(', 2),
    ']': ('[', 3),
}

for ch in s:
    if ch in '([':
        stack.append(ch)
    else:
        if ch not in pairs or not stack:
            print(0)
            sys.exit()

        open_br, val = pairs[ch]

        tmp = 0
        while stack and isinstance(stack[-1], int):
            tmp += stack.pop()

        if not stack or stack[-1] != open_br:
            print(0)
            sys.exit()

        stack.pop()
        stack.append(tmp * val if tmp else val)

if any(isinstance(x, str) for x in stack):
    print(0)
else:
    print(sum(stack))
