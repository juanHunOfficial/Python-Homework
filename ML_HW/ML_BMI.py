#formula --- (200 X 703) / (72^2) ≈ 27.14
#get the name
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

print(f"{name} your BMI is about: {bmiResult: .2f}")