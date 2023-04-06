dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
count = 0
for i in range(len(a)):
    for j in dial:
        if a[i] in j:
            count += dial.index(j)+3
print(count)