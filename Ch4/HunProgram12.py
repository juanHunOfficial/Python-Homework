read_file = input("Enter the file you wish to read from: ")
target_write_file = input("Enter the file in which you want to input the contents of the read file: ")

with open(read_file, "r") as file_r:
    with open(target_write_file, "a") as file_w:
        for line in file_r:
            file_w.write(line)
