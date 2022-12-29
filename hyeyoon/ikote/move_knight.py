input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0

for step in steps:
    new_r = row + step[0]
    new_c = column + step[1]
    if new_c > 0 and new_c <= 7 and new_r > 0 and new_r <= 7:
        result += 1
print(result)
