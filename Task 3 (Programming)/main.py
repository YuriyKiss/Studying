n = 10
a = [[0] * n for i in range(n)]

for i in range(0, n):
    k = 1
    for j in range(i, n):
        a[i][j] = k
        k += 1

for i in range(n):
    print(a[i])
