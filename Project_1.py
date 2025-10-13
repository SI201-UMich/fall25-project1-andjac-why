import csv
import unittest

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

class TestPenguinFunctions(unittest.TestCase):

    def setUp(self):
        
        self.rows = [
            {"species": "Adelie", "bill_length_mm": "39.1", "bill_depth_mm": "18.7"},
            {"species": "Adelie", "bill_length_mm": "40.0", "bill_depth_mm": "19.0"},
            {"species": "Adelie", "bill_length_mm": "NA",   "bill_depth_mm": "NA"},
            {"species": "Gentoo", "bill_length_mm": "50.0", "bill_depth_mm": "14.0"}
        ]

    
    def test_bill_average_length_general(self):
        avg = bill_average_length(self.rows, "Adelie")[0]['average_bill_length']
        self.assertEqual(avg, (39.1 + 40.0) / 2) 


if __name__ == "__main__":
    unittest.main()
