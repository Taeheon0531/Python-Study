N, M = map(int, input().split())

arr = [int(i+1) for i in range(N)]

for n in range(M):
    i, j = map(int, input().split())
    value = []
    for x in range(i, j+1):
        value.append(arr[x-1])
    value.reverse()
    count = 0
    for y in range(i, j+1):
        arr[y-1] = value[count]
        count += 1

for k in range(len(arr)):
    print(arr[k], end=" ")