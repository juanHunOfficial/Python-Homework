def calculate_taxes_by_state(state_requested, starting_salary, home_value):
    state = ["Florida", "North Carolina", "Tennessee"]
    categories = ["State Income Tax", "Sales Tax"]
    property_tax_by_state = [0.008, 0.007, 0.0067]
    property_tax_by_state = property_tax_by_state[state_requested]

    if state_requested == 1:
        chosen_taxes_by_state = [0, 0.06]#Florida taxes in order according to categoires[]
    elif state_requested == 2:
        chosen_taxes_by_state = [0.0475, 0.0475]#North Carolina taxes in order according to categoires[]
    elif state_requested == 3:
        chosen_taxes_by_state = [0, 0.07]#Tennessee taxes in order according to categoires[]
    else:
        print("ERROR: Invalid response!")

    state_to_display = state[state_requested - 1]
    net_income = starting_salary

    for index in range(len(categories)):
        net_income = net_income - (starting_salary * chosen_taxes_by_state[index])
        print(f"For the state of {state_to_display} your income after {categories[index]} is: ${round(net_income, 2)}")

    net_income = net_income - (home_value * property_tax_by_state)
    print(f"Your net income after your annual property taxes is: {net_income}")