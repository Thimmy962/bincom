import csv

all_colors = []
red = 0

with open("data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        colors = row["Colors"].split(",")
        for color in colors:
            if color.strip().upper() == "RED":
                red+=1
            all_colors.append(color)

print(len(all_colors))
print(red)