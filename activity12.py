matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)

element_00 = matrix[0][0]
element_12 = matrix[1][2]
element_21 = matrix[2][1]

print("Element at [0][0]:", element_00)
print("Element at [1][2]:", element_12)
print("Element at [2][1]:", element_21)

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()