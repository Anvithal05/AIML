import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

months = [1, 2, 3, 4, 5]
monthly_sales = [500, 700, 650, 900, 1100]

#Subplot 1: Bar Chart
plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

#Subplot 2: Line Plot
plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()
