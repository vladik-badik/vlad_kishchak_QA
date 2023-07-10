lst = [['a', 'c', 'd'],
       ['f', 'b', 'a'],
       ['a', 'n', 'k'],
       ['e', 'l', 'i']]

for col in range(len(lst[0])):
    column = []
    for row in range(len(lst)):
        column.append(lst[row][col])
    column.sort()
    for row in range(len(lst)):
        lst[row][col] = column[row]

print(lst)
