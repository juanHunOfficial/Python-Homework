def ArrayChallenge(arr):
    stringResponse = "false"

    arr.sort()

    runningTotal = 0
    for i in range(len(arr) - 1):
        runningTotal += arr[i]

    if runningTotal == arr[-1]:
        stringResponse = "true"

    if runningTotal > arr[-1]:
        runningTotal = 0
        for j in range(len(arr) - 1):
            runningTotal = arr[j]
            for k in range(len(arr) - 1):
                runningTotal += arr[k]
                if runningTotal == arr[-1]:
                    return "true"

    # code goes here
    return stringResponse


# keep this function call here
print(ArrayChallenge(input()))