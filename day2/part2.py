res = 0
# print("4-7".split("-"))
while True:
    inp = input().split()
    if inp[0] == "end":
        break
    nums = [int(x) - 1 for x in inp[0].split("-")]
    ch = inp[1][0]
    count = 0
    if inp[2][nums[0]] == ch: count += 1
    if inp[2][nums[1]] == ch: count += 1
    if count == 1:
        res += 1
print(res)