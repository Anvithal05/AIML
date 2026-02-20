import sqlite3

# 1️⃣ Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 2️⃣ Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# 3️⃣ Insert sample data (clear old data first to avoid duplicates)
cursor.execute("DELETE FROM interns")

intern_data = [
    (1, "Ananya", "Data Science", 15000),
    (2, "Rahul", "Web Dev", 12000),
    (3, "Meera", "Data Science", 18000),
    (4, "Arjun", "Cyber Security", 14000),
    (5, "Sneha", "Web Dev", 13000)
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", intern_data)

# Save changes
conn.commit()

# 4️⃣ Query: Retrieve only name and track
cursor.execute("SELECT name, track FROM interns")

results = cursor.fetchall()

print("Intern Name and Track:")
for row in results:
    print(row)

# 5️⃣ Close connection
conn.close()