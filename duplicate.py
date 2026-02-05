raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

is_present = "ID05" in unique_users
print("Is ID05 present?", is_present)

print("Total login entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))

print("\nUnique User IDs:")
print(unique_users)