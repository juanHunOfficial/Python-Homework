def ArrayChallenge(arr):
    counter = 0
    goingUp = True
    for i in range(len(arr) - 1):

        if arr[i] < arr[i + 1]:
            counter += 1
            if goingUp == False:
                break
        elif arr[i] > arr[i + 1]:
            if goingUp == False:
                counter += 1
            goingUp = False

        if counter == len(arr) - 1:
            counter = -1

    # code goes here
    return counter


# keep this function call here
print(ArrayChallenge(input()))