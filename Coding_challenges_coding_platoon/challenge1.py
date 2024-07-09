def StringChallenge(strParam):
    xCounter = 0
    oCounter = 0
    for i in range(len(strParam)):

        if strParam[i] == 'x':
            xCounter += 1
        elif strParam[i] == 'o':
            oCounter += 1
    if xCounter == oCounter:
        strParam = True
    elif xCounter != oCounter:
        strParam = False
    # code goes here
    return strParam


# keep this function call here
print(StringChallenge(input()))