rows = 5
for i in range(rows, 1, -1): #top side
    print("*" * i)

print("*" + (" ") * (rows-2 ) + "*") #middle

for i in range(2, rows + 1): #bot side
    print("*" * i)
