#make from statistics import mean

def fill_the_list():
    read_file = "test_number.txt"
    list_to_compare = []

    with open(read_file, "r") as file_r:
        for line in file_r:
            list_to_compare.append(int(line))

    return list_to_compare

def calculate_the_mean(fill_the_list):
    print(mean(fill_the_list))

def main():
    calculate_the_mean(fill_the_list())


if __name__ == "__main__":
    main()
