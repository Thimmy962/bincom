import csv
from collections import Counter



total_colors = 0
red_frequency = 0

with open("color_data.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)
    for row in reader:
        for color in row[1].split(','):
            cleaned_color = color.strip().upper()
            if cleaned_color:
                total_colors += 1
                if cleaned_color == "RED":
                    red_frequency += 1
print(f"Probability of picking red at random is {red_frequency/total_colors:.2f}")

