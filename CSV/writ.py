import csv

with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['my','name','age'])
    writer.writerow(['1001','Mike','a20'])
    writer.writerow(['1002','Bob','10'])
    writer.writerow(['1003','shoe','2'])
