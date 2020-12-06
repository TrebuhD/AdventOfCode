nums = open("./input.txt", "r").read().splitlines()

nums = list(map(int, nums))

for i, numA in enumerate(nums):
    for j, numB in enumerate(nums[i+1:]):
        for k, numC in enumerate(nums[j+1:]):
            if numA + numB + numC == 2020:
                print("Result: ", numA * numB * numC)
                break
