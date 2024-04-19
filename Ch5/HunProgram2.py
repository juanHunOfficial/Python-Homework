def main():
    read_file = input("Enter the file you wish to read from: ")

    display_the_chosen_file(read_file)

def display_the_chosen_file(read_file):
    count = 0  # initialize as index 1 to fix off by 1
    text_list = []
    with open(read_file, "r") as file_r:
        for line in file_r:
            text_list.append(line.strip())
            count += 1

        print(f"The number of pages in this file is: {count}")
        chosen_line = int(input("Which line would you like to look at? "))
        if chosen_line == 0:
            return
        else:
            print(text_list[chosen_line - 1])# -1 to account for the off by 1

if __name__ == "__main__":
    main()

