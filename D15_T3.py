import random

# Theoretical Bayes Calculation

P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

# Bayes Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("Theoretical Probability P(Spam | Free):")
print(round(P_spam_given_free, 4))


# Simulation to Verify

trials = 100000
free_count = 0
spam_and_free_count = 0

for _ in range(trials):
    # Step 1: Decide if email is spam or ham
    if random.random() < P_spam:
        email_type = "Spam"
        if random.random() < P_free_given_spam:
            contains_free = True
        else:
            contains_free = False
    else:
        email_type = "Ham"
        if random.random() < P_free_given_ham:
            contains_free = True
        else:
            contains_free = False

    # Count occurrences
    if contains_free:
        free_count += 1
        if email_type == "Spam":
            spam_and_free_count += 1

# Experimental probability
experimental = spam_and_free_count / free_count

print("\nExperimental Probability P(Spam | Free):")
print(round(experimental, 4))
