import numpy as np

trees = []
while True:
    inp = input()
    if inp == "end":
        break
    trees.append([int(ch == '#') for ch in inp])
trees = np.array(trees)
res = 0
m_res = 0
for i in range(len(trees)):
    res += trees[i, (i * 3) % trees.shape[1]]
print(res)