from statistics import mean, stdev

#get the name
bmiDict = {}
for individual in range(10):

  name = input("Enter your name: ")

#get the body weight
  bodyWeight = float(input("Enter your body weight in pounds with a maximum of one one digit to the right of the "
                         "decimal point: "))

  bmiWeight = bodyWeight * 703

#get the height
  heightForFeet = int(input("Enter your height in feet: "))
  heightForInches = int(input("Enter your height for the inches: "))

  totalHeightInInches = (heightForFeet * 12) + heightForInches

  bmiResult = bmiWeight / (totalHeightInInches ** 2)
  bmiDict.update({name: bmiResult})

bmiList = []
for name, bmiResult in bmiDict.items():

  print(f"{name}: your BMI is about: {bmiResult: .2f}")
  bmiList.append(bmiResult)

#min and max
bmiList.sort()
print(f"The lowest BMI is {bmiList[0]: .2f}")
print(f"The highest BMI is {bmiList[-1]: .2f}")

#mean and std
bmiListMean = mean(bmiList)
bmiListStd = stdev(bmiList)
print(f"The mean BMI is {bmiListMean: .2f}")
print(f"The standard deviation is {bmiListStd: .2f}")
