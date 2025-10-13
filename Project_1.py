import csv
import unittest

def penguin_pullinfo(penguin_csv):
    rows = []
    with open(penguin_csv, "r", newline="") as inFile: 
        reader = csv.DictReader(inFile)   
        for row in reader:
            rows.append(row)
    return rows   

def bill_average_length(rows, species_name, island): #changed to bill, since I thought it said beak initially in the CSV file
    total = 0.0
    count = 0
    
    for row in rows:
        if row['species'] == species_name and row['island'] == island:
            length = row['bill_length_mm']
            if length != "NA":
                total += float(length)
                count += 1
    
    if count > 0:
        avg = total / count
    else:
        avg = None
    
    return [{"species": species_name,"island": island, "average_bill_length": avg,"count": count}]

    
def bill_average_depth(rows, species_name, island ):
    total = 0.0
    count = 0
    
    for row in rows:
        if row['species'] == species_name and row['island'] == island:
            depth = row['bill_depth_mm']
            if depth != "NA":
                total += float(depth)
                count += 1
    
    if count > 0:
        avg = total / count
    else:
        avg = None
    
    return [{"species": species_name,"island": island,"average_bill_depth": avg,"count": count}]

penguin_csv = r"C:/Users/User/Desktop/SI 201/Project 1 Checkpoint/penguins.csv"
data = penguin_pullinfo(penguin_csv)
adelie_torg_len = bill_average_length(data, "Adelie", "Torgersen")
adelie_torg_depth = bill_average_depth(data, "Adelie", "Torgersen")
print(adelie_torg_len)
print(adelie_torg_depth)