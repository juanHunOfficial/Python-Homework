def SearchingChallenge(strParam):
    checkBox = 0
    stringResult = "false"

    # check if the string is between 4 and 25 chars
    if len(strParam) >= 4 and len(strParam) <= 25:
        checkBox += 1

    # check if it starts with a letter
    if strParam[0].isalpha():
        checkBox += 1

    # check if it contain invalid characters
    isValid = False
    for i in range(len(strParam)):
        if strParam[i].isalnum():
            isValid = True
        elif strParam[i] == "_":
            isValid = True
        else:
            checkBox -= 1
            break

        if i == (len(strParam) - 1):
            checkBox += 1

    # check if it ends in and underscore
    if strParam[-1] == '_':
        checkBox -= 1
    else:
        checkBox += 1

    if checkBox == 4:
        stringResult = "true"
    # code goes here
    return stringResult


# keep this function call here
print(SearchingChallenge(input()))