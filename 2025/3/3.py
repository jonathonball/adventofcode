import sys
result = 0
for line in sys.stdin.readlines():
    line = line.strip()
    largest = 0
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            num = int(str(line[i]) + str(line[j]))
            if num > largest:
                largest = num
    result += largest            
print(result)
