def check(temperature):
    if temperature > 37.2:
        print(f"体温为{temperature}超过37.2,危险危险")
    else:
        print(f"体温为{temperature}正常正常")


temp = 37.2
check(temp)
