#Inventory manager
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current Inventory:", inventory)
inventory.append("Eggs")
inventory.remove("Carrots")
inventory.sort()
print("Final Updated Inventory:", inventory)

#Data Slicer
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])
afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)
last_3_hours = temperatures[-3:]
print("Last 3 Hours Readings:", last_3_hours)

#Immutable Config
screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
print("Tuples cannot be modified!")

