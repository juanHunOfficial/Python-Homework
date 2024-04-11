with open("test.txt", "r") as file_r:
    text = file_r.read()
    print(text)

file_r.close()