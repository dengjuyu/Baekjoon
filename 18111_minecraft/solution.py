import sys

if __name__ == '__main__':
    input_fuc = sys.stdin.readline
    n, m, b = map(int, input_fuc().split())
    counts = [0] * 257
    min_h, max_h = 256, 0

    for _ in range(n):
        for h in map(int, input_fuc().split()):
            counts[h] += 1
            if h < min_h: min_h = h
            if h > max_h: max_h = h

    best_time = float('inf')
    best_h = 0

    for h in range(min_h, max_h + 1):
        remove_blocks = 0
        add_blocks = 0

        for h2 in range(257):
            if counts[h2] == 0: continue
            diff = h2 - h
            if diff > 0:
                remove_blocks += diff * counts[h2]
            elif diff < 0:
                add_blocks += -diff * counts[h2]

        if b + remove_blocks < add_blocks:
            continue

        time = remove_blocks * 2 + add_blocks

        if time < best_time or (time == best_time and h > best_h):
            best_time = time
            best_h = h

    print(best_time, best_h)