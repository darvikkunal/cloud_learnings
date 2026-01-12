import csv

with open('/Users/darvikkunalbanda/DATA_ENGINEERING/python/data/CanadaFSA_2016.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    
    count = 0
    fsa = []

    for row in reader:
        count+=1
        print(row['Geo Code'])
        fsa.append(row['Geo Code'])
        if count > 10:
            break
print(fsa)