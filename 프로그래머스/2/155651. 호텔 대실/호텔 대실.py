from collections import deque

def solution(book_time):
    
    def int_time(time):
        return int(time[0:2]) * 60 + int(time[3:])

    book_times = deque(sorted([[int_time(i[0]), int_time(i[1]) + 10] for i in book_time]))
    room = 0
    out_times = []
    while book_times:
        start, end = book_times.popleft()
        if not out_times:
            room += 1
            out_times.append(end)
        else:
            if start >= min(out_times):
                out_times.remove(min(out_times))
            else:
                room += 1
            out_times.append(end)
        
    return room