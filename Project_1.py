import csv



def penguin_pullinfo(penguin_csv):
    d = []
    with open(penguin_csv, "r") as inFile:
        reader = csv.DictReader(inFile)   

        for row in reader:
            d.append(row)
        return d
    

def beak_average(d):
    total = 0
    count = 0
    
    for row in d:  
        beak_len = row['bill_length_mm']
        if beak_len != "NA":              
            total += float(beak_len)      
            count += 1                  
    
    if count > 0:
        return total / count              
    else:
        return None
