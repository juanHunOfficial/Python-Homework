#Author: Hun, Juan P.


CAP_NUMBER_OF_YEARS = 11
PERCENT_INCREASE = 0.02
current_salary = 30_000

for teacher_experience in range(CAP_NUMBER_OF_YEARS):
    print(f"Years {teacher_experience} \t % Increase {PERCENT_INCREASE} \t Salary {round(current_salary, 2)}")
    teacher_experience += 1
    current_salary = current_salary + (current_salary * (teacher_experience * PERCENT_INCREASE))
