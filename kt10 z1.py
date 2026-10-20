requests = [
    (1, 3),
    (2, 4),
    (3, 5),
    (0, 2),
]

requests.sort(key=lambda item: item[1])
count = 0
last_end = -10 ** 18
for start, finish in requests:
    if start >= last_end:
        count += 1
        last_end = finish

print(count)
