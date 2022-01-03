nums = []
while True:
    inp = int(input())
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and inp + nums[i] + nums[j] == 2020:
                print(inp * nums[i] * nums[j])
    nums.append(inp)
