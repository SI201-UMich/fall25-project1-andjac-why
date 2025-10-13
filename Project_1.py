import csv

def penguin_pullinfo(penguin_csv):
    rows = []
    with open(penguin_csv, "r", newline="") as inFile: 
        reader = csv.DictReader(inFile)   
        for row in reader:
            rows.append(row)
    return rows   

def bill_average_length(rows, species_name): #changed to bill, since I thought it said beak initially in the CSV file
    total = 0.0
    count = 0
    
    for row in rows:  
        if row['species'] == species_name:
            beak_len = row['bill_length_mm']
            if beak_len != "NA":
                total += float(beak_len)
                count += 1
    
    if count > 0:
        avg = total / count
    else:
        avg = None
    
    return [{"species": species_name, "average_bill_length": avg, "count": count}]

    
def bill_average_depth(rows, species_name):
    total = 0.0
    count = 0
    
    for row in rows:
        if row['species'] == species_name:
            depth = row['bill_depth_mm']
            if depth != "NA":
                total += float(depth)
                count += 1
    
    if count > 0:
        avg = total / count
    else:
        avg = None
    
    return [{"species": species_name, "average_bill_depth": avg, "count": count}]


penguin_csv = r"C:/Users/User/Desktop/SI 201/Project 1 Checkpoint/penguins.csv"
data = penguin_pullinfo(penguin_csv)
adelie_avg = bill_average_length(data, "Adelie")
print("Adelie avg bill length:", adelie_avg)
gentoo_avg = bill_average_length(data, "Gentoo")
print("Gentoo avg bill length:", gentoo_avg)
