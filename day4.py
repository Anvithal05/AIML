#Personal Contact Book

contacts = {
    "Alice": "9876542310",
    "Bob": "9124578789",
    "Charlie": "9988776655"
}

contacts["Diana"] = "9112345678"

contacts["Bob"] = "9000000120"

existing_contact = contacts.get("Alice", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")

print("Safe Lookup Results:")
print("Alice:", existing_contact)
print("Eve:", missing_contact)

print("Contact List:")

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")


#duplicate cleaner

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

is_present = "ID05" in unique_users
print("Is ID05 present?", is_present)

print("Total login entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))

print("\nUnique User IDs:")
print(unique_users)


#interest matcher

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}

shared_interests = friend_a & friend_b

all_interests = friend_a | friend_b

unique_to_a = friend_a - friend_b

print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Interests Unique to Friend A:", unique_to_a)
