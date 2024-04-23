test_list = [
    [1, 12, 2, 45, 6, 22, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 45, 2, 5],
    [10, 20, 30, 40, 50]
]
def is_sorted(list_to_test):

    for index in range(len(list_to_test) - 1):
        if list_to_test[index] > list_to_test[index + 1]:
            return False
    return True

for test in test_list:
    print(is_sorted(test))

