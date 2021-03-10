

def show():
    writeToFile()
    readFromFile()


def writeToFile():
    """
    writing to file
    """

    testFile = open("test.txt", "wt")

    try:
        # write strings to file
        about_me = str("I am a developer.\nI am nice.\nI am tall.")

        testFile.write(about_me)

        testFile.close()
    except:
        testFile.close()

    # use with
    with open("test.txt", "at") as test2File:
        # write strings to file
        about_me = str("I am a developer2.\nI am nice2.\nI am tall2.")

        names = ["folau ","lau ","kiddy "]

        test2File.write(about_me)
        test2File.writelines(names)


def readFromFile():
    """
        reading from file
        """
    print("reading test.txt file...")
    with open("test.txt", "r") as reader:
        # read all content
        #print(reader.read())

        # read line by line
        print("read line by line")
        for line in reader.readlines():
            print(line,end="")