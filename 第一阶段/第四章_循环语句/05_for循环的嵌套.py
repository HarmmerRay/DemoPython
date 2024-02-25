for x in range(1, 10):
    tmp = ""
    for y in range(0, x):
        tmp += f"{y+1} * {x} = {(y+1) * x}  "
    print(tmp)
    tmp = ""
