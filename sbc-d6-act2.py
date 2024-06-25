row = 5
col = 5

# Top row
print("*" * col)

# Middle rows
current_row = 1
while current_row <= row - 2:
    if current_row == 1 or current_row == row - 2:
        print("*" + " " * (col - 2) + "*")
    else:
        print("*" + " " * (col - 2) + "*")
    current_row += 1

# Bottom row
if row > 1:
    print("*" * col)
