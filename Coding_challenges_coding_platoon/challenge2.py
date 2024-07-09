def StringChallenge(strParam):
    placementCounter = 0
    countingFromA = False

    for i in range(len(strParam)):
        if countingFromA == True:
            placementCounter += 1

        if strParam[i] == 'a':
            if countingFromA == True:
                placementCounter = 0
            countingFromA = True
        elif strParam[i] == 'b':
            placementCounter -= 1
            break

    if placementCounter == 3:
        strParam = True
    else:
        strParam = False

    # code goes here
    return strParam


# keep this function call here
print(StringChallenge(input()))