import csv

def penguin_pullinfo(penguin_csv):
    rows = []
    with open(penguin_csv, "r", newline="") as inFile: 
        reader = csv.DictReader(inFile)   
        for row in reader:
            rows.append(row)
    return rows   

def beak_average(rows, species_name):
    total = 0.0
    count = 0
    
    for row in rows:  
        if row['species'] == species_name:
            beak_len = row['bill_length_mm']
            if beak_len != "NA":
                total += float(beak_len)
                count += 1
    
    if count > 0:
        return total / count
    else:
        return None


penguin_csv = r"C:/Users/User/Desktop/SI 201/Project 1 Checkpoint/penguins.csv"
data = penguin_pullinfo(penguin_csv)
adelie_avg = beak_average(data, "Adelie")
print("Adelie avg bill length:", adelie_avg)
gentoo_avg = beak_average(data, "Gentoo")
print("Gentoo avg bill length:", gentoo_avg)
