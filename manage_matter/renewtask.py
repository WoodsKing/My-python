import csv


def renew():
    k = list()
    with open('day.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row[2] = 0
            k.append(row)
    with open('day.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(k)


renew()
