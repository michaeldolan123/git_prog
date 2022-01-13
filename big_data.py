import csv 
with open('BigData2016(1).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    station_list = []
    for station in reader:
        if station['STID'] 
