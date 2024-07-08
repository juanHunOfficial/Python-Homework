def ArrayChallenge(arr):
    counter = 0
    forwardCounter = 0
    reversedCounter = 0
    temp = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            temp = i
            break

    for j in range(temp, len(arr)):
        forwardCounter += 1
        if arr[j] == 2:
            break

    for k in range(temp, len(arr)):
        reversedCounter += 1
        if arr[k] == 2:
            break

    if forwardCounter <= reversedCounter:
        counter = forwardCounter
    else:
        counter = reversedCounter

    # code goes here
    return counter - 1


# keep this function call here
print(ArrayChallenge(input()))