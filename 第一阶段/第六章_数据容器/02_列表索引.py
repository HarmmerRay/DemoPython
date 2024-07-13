name_list = ["Tome", "John", "Smith"]

print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])

name_list = [["Tom", "Lily"], "John", "Smith"]

print(name_list[0][0])
print(name_list[0][1])

def get_data():
    data = {
        "aaa": 100,

    }
    return data["aaa"],data["bbb"]

if __name__ == "__main__":
    (a,b) = get_data()
    print(a)
    print(b)