OVERTIME_MULTIPLIER = 1.5

hourly_wages = float(input("Enter your hourly wages: "))
total_regular_hours = float(input("Enter the number of regular hours you've worked: "))
total_overtime_hours = float(input("Enter the number of overtime hours worked: "))
total_pay = ((hourly_wages * total_regular_hours) +
             ((hourly_wages * OVERTIME_MULTIPLIER) * total_overtime_hours))

print("Your total pay for the month is:", total_pay)