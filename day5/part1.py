max_ID = 0
while True:
    inp = input()
    if inp == "end":
        break
    ID = 0
    for i in range(len(inp)):
        ID *= 2
        if inp[i] == 'B' or inp[i] == 'R':
            ID += 1
    max_ID = max(max_ID, ID)
print(max_ID)