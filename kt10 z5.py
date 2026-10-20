from collections import OrderedDict

capacity = 2
commands = [
    ("PUT", 1, 1),
    ("PUT", 2, 2),
    ("GET", 1),
    ("PUT", 3, 3),
    ("GET", 2),
    ("GET", 3),
    ("PUT", 4, 4),
    ("GET", 1),
    ("GET", 3),
    ("GET", 4),
]

values = {}
freq = {}
buckets = {}
min_freq = 0


def touch(key, new_value=None):
    global min_freq
    current = freq[key]
    del buckets[current][key]
    if not buckets[current]:
        del buckets[current]
        if min_freq == current:
            min_freq = current + 1
    nxt = current + 1
    freq[key] = nxt
    buckets.setdefault(nxt, OrderedDict())[key] = True
    if new_value is not None:
        values[key] = new_value


for command in commands:
    if command[0] == "GET":
        key = command[1]
        if key not in values:
            print(-1)
        else:
            touch(key)
            print(values[key])
    else:
        key, value = command[1], command[2]
        if key in values:
            touch(key, value)
            continue
        if len(values) == capacity:
            old_key = next(iter(buckets[min_freq]))
            del buckets[min_freq][old_key]
            if not buckets[min_freq]:
                del buckets[min_freq]
            del values[old_key]
            del freq[old_key]
        values[key] = value
        freq[key] = 1
        buckets.setdefault(1, OrderedDict())[key] = True
        min_freq = 1
