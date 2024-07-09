def StringChallenge(strArr):
    string = strArr[0]
    numberOfRows = strArr[1]
    numberOfSkips = 0

    # cast int because its a string
    numberOfRows = int(numberOfRows)
    # no zig or zagging when it is 1 so we just return the string as is
    if numberOfRows == 1:
        return string

    # empty string for concat
    resultString = ""

    # number of skips needed to get to the next letter in the pattern(goes up by 2)
    for i in range(len(string)):
        numberOfSkips = (numberOfRows - 1) * 2
        for itemAdded in range(i, len(string), numberOfSkips):
            resultString += string[itemAdded]
            # if your in the middle section, depending on the distance it decreases by two
            if i > 0 and i < numberOfRows and itemAdded + numberOfSkips - 2 * i < len(string):
                # this if else statement was to stop the string from wrapping
                if len(resultString) == len(string):
                    return resultString
                else:
                    resultString += string[i + numberOfSkips - 2 * itemAdded]

    # code goes here
    return resultString


# keep this function call here
print(StringChallenge(input()))