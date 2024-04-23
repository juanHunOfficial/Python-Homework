not_sorted_list = [1,12,2,45,6,22,7]

def is_sorted(not_sorted_list):
    temp = not_sorted_list[0]
    sort_results = False

    for ind in range(len(not_sorted_list)):
        if not_sorted_list[ind] > temp:
            temp = not_sorted_list
            sort_results = True
        elif not_sorted_list[ind] < temp:
            return False
    return sort_results

print(is_sorted(not_sorted_list))