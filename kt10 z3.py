import random

numbers = [7, 2, 5, 3, 9]
k = 3

left = 0
right = len(numbers) - 1
target = k - 1
while True:
    pivot = numbers[random.randint(left, right)]
    i = left
    j = right
    while i <= j:
        while numbers[i] < pivot:
            i += 1
        while numbers[j] > pivot:
            j -= 1
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
    if target <= j:
        right = j
    elif target >= i:
        left = i
    else:
        print(numbers[target])
        break
