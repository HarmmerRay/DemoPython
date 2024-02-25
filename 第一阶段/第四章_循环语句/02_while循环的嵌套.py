import sys

i = 1
j = 1
while i < 10:
    while j <= i:   
        sys.stdout.write(f"{j} * {i} = {j * i}  ")
        j += 1
    print()
    i += 1
    j = 1