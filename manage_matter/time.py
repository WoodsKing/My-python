import datetime
import csv
k = datetime.date(2021,2,2)
today = datetime.date.today()
if k == today:
    print('yes')
print(k>today)
print(today)