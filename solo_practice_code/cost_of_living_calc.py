from calulations import calculate_taxes_by_state, calculate_federal_income_tax

state_requested = int(input("Select the state you wish to check from the menu:"
                        "\n 1) Florida"
                        "\n 2) North Carolina"
                        "\n 3) Tennessee \n"))

print(state_requested)

starting_salary = float(input("Enter your starting salary: "))
home_value = float(input("Enter in your desired home value: "))


net_income = calculate_federal_income_tax(starting_salary)
calculate_taxes_by_state(state_requested, starting_salary, net_income, home_value)