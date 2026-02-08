my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
basic_slice = my_list[2:6]
print("Basic slice:", basic_slice)
start_not_specified = my_list[:4]
print("Slice with start not specified:", start_not_specified)
end_not_specified = my_list[7:]
print("Slice with end not specified:", end_not_specified)
step_slice = my_list[1:8:2]
print("Slice with step value:", step_slice)
negative_indexes = my_list[-5:-1]
print("Slice with negative indexes:", negative_indexes)
