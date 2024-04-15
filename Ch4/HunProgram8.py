read_file = input("Enter the name of the file you wish to read from: ")
target_write_file = input("Enter the name of the file you wish to write to: ")

with open(read_file, "r") as file_r:
    with open(target_write_file, "w") as file_w:
        for line in file_r:
            file_w.write(line)




file_r.close()