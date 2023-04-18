matrix = []
for i in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

max_num = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if max_num <= matrix[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = matrix[row][col]

print(max_num)
print(max_row, max_col)