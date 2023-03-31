lst = [int(n+1) for n in range(30)]

for i in range(28):
    lst.remove(int(input()))

lst.sort()

print(lst[0])
print(lst[1])