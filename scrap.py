import requests
import datetime

period = 1

base = datetime.datetime.today()
date_list = [(base - datetime.timedelta(days = x)).strftime('%d-%m-%Y') for x in range(period)]

print(date_list)