def main():
    count = 0
    with open("data.txt", "r") as fopen:
        for line in fopen:
            safe = 2
            nums = [int(num) for num in line.split()]
            ascend = True
            asc_count = 0
            for i in range(1, len(nums)):
                if nums[i-1] < nums[i]:
                    asc_count += 1
                else:
                    asc_count -= 1
            if asc_count < 0:
                ascend = False
            if ascend:
                i = -1
                while True:
                    i += 1
                    if i >= len(nums) - 1:
                        break
                    if 1 <= (nums[i+1] - nums[i]) <= 3:
                        continue
                    if safe == 2 and (is_safe(nums[:i]+nums[i+1:]) or is_safe(nums[:i+1]+nums[i+2:])):
                        safe -= 1
                        i += 1
                        continue
                    safe = 0
                    break
            else:
                i = -1
                while True:
                    i += 1
                    if i >= len(nums) - 1:
                        break
                    if 1 <= (nums[i] - nums[i+1]) <= 3:
                        continue
                    if safe == 2 and (is_safe(nums[:i]+nums[i+1:]) or is_safe(nums[:i+1]+nums[i+2:])):
                        safe -= 1
                        i += 1
                        continue
                    safe = 0
                    break
            if safe > 0:
                count += 1

    print(count)

def is_safe(nums: list[int]) -> int:
    ascend = True
    asc_count = 0
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            asc_count += 1
        else:
            asc_count -= 1
    if asc_count < 0:
        ascend = False
    if ascend:
        for i in range(len(nums)-1):
            if 1 <= (nums[i+1] - nums[i]) <= 3:
                continue
            return 0
    else:
        for i in range(len(nums)-1):
            if 1 <= (nums[i] - nums[i+1]) <= 3:
                continue
            return 0
        
    return 1

main()