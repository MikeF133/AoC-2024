import re

def main():
    fopen = open("data.txt", "r")
    total = 0
    for line in fopen:
        line = "".join(str_generator(line))
        print(len(line))
        muls = re.findall(r'mul\((\d{1,3},\d{1,3})\)', line)
        for mul in muls:
            nums = [int(i) for i in mul.split(",")]
            total += nums[0] * nums[1]
    print(total)

def str_generator(s: str):
    action = 1
    for i in range(len(s)):
        if action == 1:
            yield s[i]
            if s[i+1:i+8] == "don't()":
                action = 0
        if action == 0:
            if s[i+1:i+5] == "do()":
                action = 1

main()