N = int(input())

lines = 2 * N - 1
eachline = ''

for i in range(lines//2):
    eachline = ' ' * (lines//2 - i) + '*' * (2 * i + 1)
    print(eachline)

for i in range(lines//2 + 1):
    eachline = ' ' * i + '*' * (lines - 2 * i )
    print(eachline)