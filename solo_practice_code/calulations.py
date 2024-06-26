def calculate_taxes_by_state(state_requested, starting_salary, net_income, home_value):
    state = ["Florida", "North Carolina", "Tennessee"]
    property_tax_by_state = [0.008, 0.007, 0.0067]
    state_income_tax = [0, 0.0475, 0]

    state_income_tax = state_income_tax[state_requested]
    property_tax_by_state = property_tax_by_state[state_requested]
    state_to_display = state[state_requested]

    net_income = net_income - (home_value * property_tax_by_state)
    print(f"Your net income after your annual property taxes is: ${net_income}")
    net_income = net_income - (starting_salary * state_income_tax)
    print(f"For the state of {state_to_display} your income after the state income tax is: "
          f"${round(net_income, 2)}")

    print(f"Living in this state will cost you: ${(starting_salary - net_income)} per year")
    return net_income

def calculate_federal_income_tax(starting_salary):
    #This will be for married filing jointly 2023 taxes
    federal_income_range = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
    federal_income_limit = [11_000, 44_725, 95_375, 182_100, 231_250, 346_875, 346_876]

    salary_index = 0
    if starting_salary < federal_income_limit[0]:
        salary_index = 0
    elif starting_salary < federal_income_limit[1]:
        salary_index = 1
    elif starting_salary < federal_income_limit[2]:
        salary_index = 2
    elif starting_salary < federal_income_limit[3]:
        salary_index = 3
    elif starting_salary < federal_income_limit[4]:
        salary_index = 4
    elif starting_salary < federal_income_limit[5]:
        salary_index = 5
    elif starting_salary >= federal_income_limit[6]:
        salary_index = 6


    net_income = starting_salary
    net_income = net_income - (starting_salary * federal_income_range[salary_index])

    print(f"Based on your income for married filing jointly, you fall under the "
          f"{(federal_income_range[salary_index] * 100)}% bracket")
    print(f"Your net income after federal taxes have been removed is: ${net_income}")

    return net_income

def display_cost_of_living_stats(state_requested, net_income):
    city_of_state = ["Tampa", "Raleigh", "Nashville"]
    average_col_family_of_4 = [4_759.6, 4_550.5, 4_449.6]#fl(tampa), nc(raleigh), tn(nashville)
    average_col_single = [1_339.5, 1_290.2, 1_234.5]#fl(tampa), nc(raleigh), tn(nashville)

    print(f"The average cost of living in {city_of_state[state_requested]} is ${average_col_family_of_4[state_requested]} for "
          f"a family of four, and ${average_col_single[state_requested]} for a single person.")
    NUMBER_OF_MONTHS = 12
    estimated_monthly_income = round((net_income / NUMBER_OF_MONTHS), 2)
    estimated_monthly_surplus_fam4 = estimated_monthly_income - average_col_family_of_4[state_requested]
    estimated_monthly_surplus_single = estimated_monthly_income - average_col_single[state_requested]

    print(f"Based on your net income of ${net_income} you will have about ${estimated_monthly_income} "
          f"with an estimated ${estimated_monthly_surplus_fam4} in surplus per month for a family of 4, and "
          f"${estimated_monthly_surplus_single} for a single person")
