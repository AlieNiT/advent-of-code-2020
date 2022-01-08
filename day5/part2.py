import numpy as np

seats = np.ones(1024)
while True:
    inp = input()
    if inp == "end":
        break
    ID = 0
    for i in range(len(inp)):
        ID *= 2
        if inp[i] == 'B' or inp[i] == 'R':
            ID += 1
    seats[ID] = 0
for i in range(1, 1023):
    if seats[i] == 1 and seats[i - 1] == 0 and seats[i + 1] == 0:
        print(i)