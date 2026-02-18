import random

#Independent Events

# Theoretical Probability
P_heads = 1 / 2
P_six = 1 / 6
P_independent = P_heads * P_six

print("Independent Event (Heads AND 6)")
print("Theoretical Probability:", P_independent)


# Simulation
trials = 100000
success = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)

    if coin == "H" and die == 6:
        success += 1

experimental_independent = success / trials
print("Experimental Probability:", experimental_independent)

# Dependent Events

# Theoretical Probability
P_first_red = 5 / 10
P_second_red_given_first = 4 / 9
P_dependent = P_first_red * P_second_red_given_first

print("\nDependent Event (Two Reds without replacement)")
print("Theoretical Probability:", P_dependent)


# Simulation
success = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)

    if first == "R" and second == "R":
        success += 1

experimental_dependent = success / trials
print("Experimental Probability:", experimental_dependent)
