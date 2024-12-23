import re

input = open(0).read().strip()

part1 = 0

for m in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', input):
    x,y = m
    part1 += int(x)*int(y)

print(part1)

for m in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input):
    x,y = m
    part1 += int(x)*int(y)


part2 = 0
do = True
for m in re.findall(r'(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))', input):
    mstr,x,y = m
    if mstr == 'do()':
        do = True
    elif mstr == 'don\'t()':
        do = False
    elif do:
        part2 += int(x)*int(y)

print(part2)

