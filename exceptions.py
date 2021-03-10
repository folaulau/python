
def show():
    print("exceptions handling")

    try:
        result = 12 / 0
        print(result)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("all good")
    print("done!")

    # name = input("what is your name? ")
    # if name == None or len(name) ==0 :
    #     raise ValueError("invalid name")

    try:
        f = open("test.txt", encoding='utf-8')
        # perform file operations
    finally:
        f.close()
        print("file closed")
