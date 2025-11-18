import sqlite3

conn = sqlite3.connect("farm.db")
c = conn.cursor()

# Create a table
c.execute("""
CREATE TABLE IF NOT EXISTS crops (
    id INTEGER PRIMARY KEY,
    name TEXT,
    season TEXT,
    water_need TEXT
)
""")

# Insert sample rows
c.execute("INSERT INTO crops (name, season, water_need) VALUES ('Rice', 'Kharif', 'High')")
c.execute("INSERT INTO crops (name, season, water_need) VALUES ('Wheat', 'Rabi', 'Medium')")
c.execute("INSERT INTO crops (name, season, water_need) VALUES ('Millet', 'Kharif', 'Low')")

conn.commit()
conn.close()
