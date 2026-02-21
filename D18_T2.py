import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# Create mentors table

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT NOT NULL,
    track TEXT NOT NULL
)
""")

# Clear old data (safe re-run)
cursor.execute("DELETE FROM interns")
cursor.execute("DELETE FROM mentors")

# Insert sample data

intern_data = [
    (1, "Ananya", "Data Science", 15000),
    (2, "Rahul", "Web Dev", 12000),
    (3, "Meera", "Data Science", 18000),
    (4, "Arjun", "Cyber Security", 14000),
    (5, "Sneha", "Web Dev", 13000)
]

mentor_data = [
    (1, "Dr. Sharma", "Data Science"),
    (2, "Mr. Kapoor", "Web Dev"),
    (3, "Ms. Iyer", "Cyber Security")
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", intern_data)
cursor.executemany("INSERT INTO mentors VALUES (?, ?, ?)", mentor_data)

conn.commit()

# INNER JOIN Query

join_query = """
SELECT interns.name AS intern_name,
       interns.track,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

# Load JOIN result into Pandas DataFrame
df = pd.read_sql_query(join_query, conn)

print("Interns with Their Mentors:")
print(df)

# Close connection
conn.close()