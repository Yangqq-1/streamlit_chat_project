row = 1
while row < 10:
    col = 1
    while col <= row:
        print(f"{row} * {col} = {row*col}", end='\t')
        col += 1
    print() # 嵌套
    row += 1