mass = float(input("Enter the mass of the object: "))
velocity = float(input("Enter the velocity of the object: "))

momentum = mass * velocity

kinetic_energy = 0.5 * mass * (velocity ** 2)

print("The momentum is:", momentum, "The kinetic energy is:", kinetic_energy)
