import sys
def multiple_table():
    for i in range(1, 10):
        for j in range(1, 1 + i):
            sys.stdout.write(f"{i} * {j} = {i * j}\t")
        print()

if __name__ == '__main__':
    multiple_table()
