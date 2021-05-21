while True:
    try:
        x = int(input("number: "))
    except ValueError:
        print("input data error")
    else:
        print(x)
        break