commands = [
    ("PUSH", 3),
    ("PUSH", 1),
    ("MIN",),
    ("MAX",),
    ("PUSH", 5),
    ("MAX",),
    ("POP",),
    ("MIN",),
]

journal = []
for command in commands:
    if command[0] == "PUSH":
        value = command[1]
        if not journal:
            journal.append((value, value, value))
        else:
            journal.append((value, min(value, journal[-1][1]), max(value, journal[-1][2])))
    elif command[0] == "POP":
        journal.pop()
    elif command[0] == "MIN":
        print(journal[-1][1])
    else:
        print(journal[-1][2])
