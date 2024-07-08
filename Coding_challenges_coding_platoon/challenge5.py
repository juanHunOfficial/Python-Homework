def ArrayChallenge(arr):
    # testing first two variables
    firstList = []
    secondList = []
    counter = 0
    for i in range(arr[0], arr[1] + 1):
        firstList.append(i)

    for j in range(arr[2], arr[3] + 1):
        secondList.append(j)

    # get the range value for the higher list
    if len(firstList) < len(secondList):
        greaterRangeValue = secondList
        lesserRangeValue = firstList
    else:
        greaterRangeValue = firstList
        lesserRangeValue = secondList

    for k in range(len(greaterRangeValue)):
        for g in range(len(lesserRangeValue)):
            if k == g:
                counter += 1
            else:
                continue

    if counter >= arr[4]:
        return "true"
    else:
        return "false"


# keep this function call here
print(ArrayChallenge(input()))