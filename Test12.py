def m1():
    file1 = open("test.txt", "w+")
    try:
        read_content = file1.read()
        print(read_content)

    finally:
        # close the file
        file1.close()

m1()