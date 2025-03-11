def allocate_conference_rooms(meetings):
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last_end_time = 0

    for start, end in meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count

N = int(input())
meeting_list = [list(map(int, input().split())) for _ in range(N)]
print(allocate_conference_rooms(meeting_list))