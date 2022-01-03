nums = []
while True:
    inp = int(input())
    for num in nums:
        if inp + num == 2020:
            print(inp * num)
            exit()
    nums.append(inp)