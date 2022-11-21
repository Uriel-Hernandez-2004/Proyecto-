i = 2
j = 1
k = 10
print(i, k/2 + i*2)

while i < 20 and j < 45:
    if k <= 10:
        j = 50 - i * 9
        i += 2
    k += i
    i += 10
    print(i, k/2 + i*2)