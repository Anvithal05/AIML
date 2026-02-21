import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# Clear old data (avoid duplicates when re-running)
cursor.execute("DELETE FROM interns")

# Insert sample data
intern_data = [
    (1, "Ananya", "Data Science", 15000),
    (2, "Rahul", "Web Dev", 12000),
    (3, "Meera", "Data Science", 18000),
    (4, "Arjun", "Cyber Security", 14000),
    (5, "Sneha", "Web Dev", 13000)
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", intern_data)

conn.commit()

# FILTER: Data Science interns with stipend > 5000
print("Data Science Interns with stipend > 5000:")
cursor.execute("""
SELECT * FROM interns
WHERE track = 'Data Science'
AND stipend > 5000
""")

for row in cursor.fetchall():
    print(row)

# AGGREGATE: Average stipend per track
print("\nAverage Stipend per Track:")
cursor.execute("""
SELECT track, AVG(stipend) AS average_stipend
FROM interns
GROUP BY track
""")

for row in cursor.fetchall():
    print(row)

# COUNT: Number of interns per track
print("\nNumber of Interns per Track:")
cursor.execute("""
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track
""")

for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()