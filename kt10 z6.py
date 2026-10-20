import random

points = [
    (1, 1),
    (-2, 2),
    (0, 1),
    (3, 0),
]
k = 2

items = []
for index, (x, y) in enumerate(points, 1):
    items.append((x * x + y * y, x, y, index))

left = 0
right = len(items) - 1
target = k - 1
while left < right:
    pivot = items[random.randint(left, right)]
    i = left
    j = right
    while i <= j:
        while items[i] < pivot:
            i += 1
        while items[j] > pivot:
            j -= 1
        if i <= j:
            items[i], items[j] = items[j], items[i]
            i += 1
            j -= 1
    if target <= j:
        right = j
    elif target >= i:
        left = i
    else:
        break

chosen = sorted(items[:k])
for dist, x, y, index in chosen:
    print(x, y, index)
