def my_range(start, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0

    current = start
    lyst = []
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        lyst.append(current)
        current += step
    return lyst

for x in my_range(5):
    print(x)

for x in range(5):
    print(x)

print(my_range(5))
print(range(5))# i found that it says to retrun a range function but im not
               #sure what that means. Would i have to define an entire range class?