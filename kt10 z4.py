import heapq

orders = [
    (2, 100),
    (1, 19),
    (2, 27),
    (1, 25),
    (3, 15),
]

orders.sort()
chosen = []
for deadline, profit in orders:
    if len(chosen) < deadline:
        heapq.heappush(chosen, profit)
    elif chosen and chosen[0] < profit:
        heapq.heapreplace(chosen, profit)

print(sum(chosen))
