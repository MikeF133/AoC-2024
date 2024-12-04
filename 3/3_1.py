import re

def main():
    fopen = open("data.txt", "r")
    total = 0
    for line in fopen:
        muls = re.findall(r'mul\((\d{1,3},\d{1,3})\)', line)
        for mul in muls:
            nums = [int(i) for i in mul.split(",")]
            total += nums[0] * nums[1]
    print(total)

main()