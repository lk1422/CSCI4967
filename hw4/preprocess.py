import csv
from collections import Counter

f = open("pop.csv")
g = open("pop2.csv", 'w')
genres = Counter()
processed = csv.writer(g)
csv_r = csv.reader(f)
for row in csv_r:
    if row[1] == 'pop' and row[-1] == "en":
        processed.writerow(row)
f.close()
g.close()
