import heapq

N = int(input())
heap = []
for i in range(N):
    data = int(input())
    heapq.heappush(heap, data)

answer = 0

while len(heap) != 1:

    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_val = one + two
    heapq.heappush(heap, sum_val)
    answer += sum_val

print(answer)