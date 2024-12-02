count = 0

with open("data.txt", "r") as fopen:
    for line in fopen:
        safe = True
        nums = [int(num) for num in line.split()]
        ascend = True
        if nums[1] < nums[0]:
            ascend = False
        if ascend:
            for i in range(len(nums)-1):
                if 1 <= (nums[i+1] - nums[i]) <= 3:
                    continue
                safe = False
                break
        else:
            for i in range(len(nums)-1):
                if 1 <= (nums[i] - nums[i+1]) <= 3:
                    continue
                safe = False
                break
        if safe:
            count += 1

print(count)
