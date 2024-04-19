def main():
    read_file = input("Enter the file you wish to read from: ")

    organize_text_file_words(read_file)

def organize_text_file_words(read_file):
    text_list = []
    with open(read_file, "r") as file_r:
        for line in file_r:
            for word in line.split():
                text_list.append(word)
        text_list.sort(key = str.lower)
        print(text_list)



if __name__ == "__main__":
    main()