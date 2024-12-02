left, right = [], []
with open("data.txt", "r") as fopen:
    for line in fopen:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

left = sorted(left, reverse=True)
right = sorted(right, reverse=True)

total = 0
for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)