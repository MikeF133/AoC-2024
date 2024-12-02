left, right = [], []
with open("data.txt", "r") as fopen:
    for line in fopen:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

right_count = dict()
for num in right:
    right_count[num] = right_count.get(num, 0) + 1

total = 0
for num in left:
    total += num * right_count.get(num, 0)

print(total)