def MathChallenge(num):
    counter = 0

    num = str(num)

    while len(num) >= 2:
        tempFirstNum = num[0]
        tempSecondNum = num[1]

        num = str(int(tempFirstNum) * int(tempSecondNum))

        counter += 1

    # code goes here
    return counter


# keep this function call here
print(MathChallenge(input()))