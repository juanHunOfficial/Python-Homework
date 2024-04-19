def mean(numbers):
    sum = 0
    count = 0
    if len(numbers) == 0:
        return 0
    for count in range(len(numbers)):
        sum += numbers[count]
        count += 1

    mean = sum / count
    return mean

def median(numbers):
    numbers.sort()

    if len(numbers) == 0:
        return 0

    if len(numbers) % 2 == 1:
        med = numbers[len(numbers) // 2] #if odd take the middle number
    else:
        med = numbers[len(numbers) // 2 + 1] / numbers[len(numbers) // 2 - 1] # if even take the average
                                                                              # of the two middle numbers

    return med

def main():
    numbers = [12, 4, 56, 2, 100, 41]
    print(mean(numbers))
    print(median(numbers))




if __name__ == "__main__":
    main()