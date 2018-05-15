def sum_dig_pow(a, b):
    count = []
    arr = range(a, b + 1)
    for i in arr:
        t = 0
        for j in range(0, len(str(i))):
            t += int(str(i)[j]) ** (j + 1)
        if (t == i):
            count.append(i)
    return count



a = 89
print(a)