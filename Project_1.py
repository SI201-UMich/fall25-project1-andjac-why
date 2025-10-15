import csv
import unittest
import os

def penguin_pullinfo(penguin_csv):
    rows = []
    file_path = os.path.join(os.getcwd(), "fall25-project1-andjac-why", penguin_csv) #if this does not working, remove fall25-project1-andjac-why
    with open(file_path, mode = "r", newline="", encoding="utf-8") as inFile:
        reader = csv.DictReader(inFile)
        for row in reader:
            rows.append(row)
    return rows


def bill_average_length(rows, species_name, island):
    total = 0.0
    count = 0
    for row in rows:
        if row["species"] == species_name and row["island"] == island:
            length = row["bill_length_mm"].strip()
            if length != "NA" and length != "":
                total += float(length)
                count += 1
    if count > 0:
        avg = total / count
    else:
        avg = None
    return [{
        "species": species_name,
        "island": island,
        "average_bill_length": avg,
        "count": count
    }]

def bill_average_depth(rows, species_name, island):
    total = 0.0
    count = 0
    for row in rows:
        if row["species"] == species_name and row["island"] == island:
            depth = row["bill_depth_mm"].strip()
            if depth != "NA" and depth != "":
                total += float(depth)
                count += 1
    if count > 0:
        avg = total / count
    else:
        avg = None
    return [{
        "species": species_name,
        "island": island,
        "average_bill_depth": avg,
        "count": count
    }]

def main():
    # penguin_csv = "C:/Users/User/Desktop/SI 201/Project 1 Checkpoint/penguins.csv" 
    penguin_csv = "test.csv"
    data = penguin_pullinfo(penguin_csv)
    adelie_torg_len = bill_average_length(data, "Adelie", "Torgersen")
    adelie_torg_depth = bill_average_depth(data, "Adelie", "Torgersen")
    print(adelie_torg_len)
    print(adelie_torg_depth)

class TestPenguinAverages(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        cls.rows = penguin_pullinfo(
            "test.csv"
        )
        print(f"[tests] loaded {len(cls.rows)} rows from test.csv")

    def _expected_avg(self, rows, species, island, column_key):
        total = 0.0
        count = 0
        for r in rows:
            if r["species"] == species and r["island"] == island:
                v = str(r[column_key]).strip()
                if v != "NA" and v != "":
                    total += float(v)
                    count += 1
        if count == 0:
            return None, 0
        return total / count, count

    
    def test_bill_average_length_general_adelie_torgersen(self):
        out = bill_average_length(self.rows, "Adelie", "Torgersen")[0]
        exp_avg, exp_cnt = self._expected_avg(self.rows, "Adelie", "Torgersen", "bill_length_mm")
        if exp_avg is None:
            self.assertEqual(out["average_bill_length"], None)
        else:
            self.assertEqual(round(out["average_bill_length"], 6), round(exp_avg, 6))
        self.assertEqual(out["count"], exp_cnt)
        self.assertGreater(out["count"], 0)

    def test_bill_average_length_general_gentoo_biscoe(self):
        out = bill_average_length(self.rows, "Gentoo", "Biscoe")[0]
        exp_avg, exp_cnt = self._expected_avg(self.rows, "Gentoo", "Biscoe", "bill_length_mm")
        if exp_avg is None:
            self.assertEqual(out["average_bill_length"], None)
        else:
            self.assertEqual(round(out["average_bill_length"], 6), round(exp_avg, 6))
        self.assertEqual(out["count"], exp_cnt)
        self.assertTrue(out["count"] >= 1)

    def test_bill_average_length_edge_no_pair(self):
        out = bill_average_length(self.rows, "Chinstrap", "Biscoe")[0]
        self.assertEqual(out["average_bill_length"], None)
        self.assertEqual(out["count"], 0)

    def test_bill_average_length_edge_case_sensitivity(self):
        out = bill_average_length(self.rows, "Adelie", "torgersen")[0]
        self.assertEqual(out["average_bill_length"], None)
        self.assertEqual(out["count"], 0)

    
    def test_bill_average_depth_general_adelie_torgersen(self):
        out = bill_average_depth(self.rows, "Adelie", "Torgersen")[0]
        exp_avg, exp_cnt = self._expected_avg(self.rows, "Adelie", "Torgersen", "bill_depth_mm")
        if exp_avg is None:
            self.assertEqual(out["average_bill_depth"], None)
        else:
            self.assertEqual(round(out["average_bill_depth"], 6), round(exp_avg, 6))
        self.assertEqual(out["count"], exp_cnt)
        self.assertGreater(out["count"], 0)

    def test_bill_average_depth_general_gentoo_biscoe(self):
        out = bill_average_depth(self.rows, "Gentoo", "Biscoe")[0]
        exp_avg, exp_cnt = self._expected_avg(self.rows, "Gentoo", "Biscoe", "bill_depth_mm")
        if exp_avg is None:
            self.assertEqual(out["average_bill_depth"], None)
        else:
            self.assertEqual(round(out["average_bill_depth"], 6), round(exp_avg, 6))
        self.assertEqual(out["count"], exp_cnt)

    def test_bill_average_depth_edge_no_pair(self):
        out = bill_average_depth(self.rows, "Gentoo", "Dream")[0]
        self.assertEqual(out["average_bill_depth"], None)
        self.assertEqual(out["count"], 0)

    def test_bill_average_depth_edge_case_sensitivity(self):
        out = bill_average_depth(self.rows, "Gentoo", "biscoe")[0]
        self.assertEqual(out["average_bill_depth"], None)
        self.assertEqual(out["count"], 0)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
    main()

