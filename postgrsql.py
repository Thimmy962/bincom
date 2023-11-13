import csv
from collections import Counter
import psycopg2

color_data = {}

with open("color_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        day = row["Day"]
        colors = row["Colors"].split(",")
        color_data[day] = colors

all_color =[]

for colors in color_data.values():
    for color in colors:
        all_color.append(color)

color_frequency = Counter(all_color)

db_params = {
    'host': 'thimmy',
    'database': 'hello',
    'user': 'thimmy',
    'password': 'Uydnv1$1',
}


# Connect to PostgreSQL
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Create a table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS color_frequency (
            color VARCHAR(255),
            frequency INT
        )
    """)
    connection.commit()

    # Insert data into the table
    for color, frequency in color_frequency.items():
        cursor.execute("INSERT INTO color_frequency (color, frequency) VALUES (%s, %s)", (color, frequency))
    
    connection.commit()

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()