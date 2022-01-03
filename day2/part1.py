res = 0
# print("4-7".split("-"))
while True:
    inp = input().split()
    if inp[0] == "end":
        break
    nums = [int(x) for x in inp[0].split("-")]
    ch = inp[1][0]
    count = 0
    for c in inp[2]:
        if c == ch:
            count += 1
    if nums[0] <= count <= nums[1]:
        res += 1
print(res)