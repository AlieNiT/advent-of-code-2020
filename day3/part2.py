import math

import numpy as np

trees = []
while True:
    inp = input()
    if inp == "end":
        break
    trees.append([int(ch == '#') for ch in inp])
trees = np.array(trees)
m_res = 1
for r in range(1, 9, 2):
    res = 0
    for i in range(len(trees)):
        res += trees[i, (i * r) % trees.shape[1]]
    m_res = m_res * res
res = 0
for i in range((len(trees) - 1)//2):
    res += trees[i * 2, i % trees.shape[1]]
m_res = m_res * res
print(m_res)
