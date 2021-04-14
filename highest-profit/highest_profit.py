#!/usr/bin/python  
import sys
import csv
import json

def check_type(text):
    try:
        int(text)
        return int
    except ValueError:
        pass
    try:
        float(text)
        return float
    except ValueError:
        pass
    return str

def highest_profit(file):
    data = {}
    with open(file) as f:
        csv_file = csv.DictReader(f)
        count = 0
        numericRows = 0
        for row in csv_file:
            count += 1
            if not check_type(row['Profit (in millions)']) == str:
                numericRows += 1
                data[numericRows] = row
        print("Number of Rows:", count)
        print("Number of Numeric Profit Column Rows:", numericRows)

    with open('data2.json', 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))
    for i, s in enumerate(sorted(data.items(), key=lambda k_v: float(k_v[1]['Profit (in millions)']), reverse=True)[:20], start = 1):
        print(str(i) + '.', s[1])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("USAGE: python highest_profit.py data.csv")
        sys.exit(1)
    
    highest_profit(sys.argv[1])
    