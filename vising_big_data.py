import csv
import matplotlib.pyplot as plt
# Gathering info from user
name = input('Hi what is your name? >')
print()
print(f'Hi {name} lets look at some weather data.')

stations = ['ALTU', 'BEAV', 'NRMN', 'TISH', 'TULN']
print()
datas = input('what data do you want to see; ie: TMAX, TMIN, WSMX, HAVG, WSMN, RAIN. >')
print()
time = input('what time period like month or whole year; ie: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, all. >')
# Seting var
stored_data = []
day = []
alt =[]
bev = []
nmn = []
tsh = []
tul = []
dayas = []
# Gatering data from file\
keeptrack = 0
data = open('/home/mdolan/Desktop/git_prog/2016VizData (3).csv', newline='') 
with data as csvfile:
    reader = csv.DictReader(csvfile)
    station_list = []
    for row in reader:
        for station in stations:
            if row['STID'] == station:
                if float(row['TMIN']) == -996.00 and float(row['TMAX']) == -996.00:
                    (row['TMIN']) = 0
                    (row['TMAX']) = 0
                if row['MONTH'] == time:
                    if row['STID'] == 'ALTU':
                        alt.append(row[datas])
                        keeptrack += 1
                        dayas.append(keeptrack)
                    if row['STID'] == 'BEAV':
                        bev.append(row[datas])                           
                    if row['STID'] == 'NRMN':
                        nmn.append(row[datas])
                    if row['STID'] == 'TISH':
                        tsh.append(row[datas])
                    if row['STID'] == 'TULN':
                        tul.append(row[datas])
                if time == 'all':
                    if row['STID'] == 'ALTU':
                        alt.append(row[datas])
                        keeptrack += 1
                        dayas.append(keeptrack)
                    if row['STID'] == 'BEAV':
                        bev.append(row[datas])                           
                    if row['STID'] == 'NRMN':
                        nmn.append(row[datas])
                    if row['STID'] == 'TISH':
                        tsh.append(row[datas])
                    if row['STID'] == 'TULN':
                        tul.append(row[datas]) 
                    
plt.plot(dayas, alt, color='red', marker='o')
plt.plot(dayas, bev, color='blue', marker='o')
plt.plot(dayas, nmn, color='green', marker='o')
plt.plot(dayas, tsh, color='yellow', marker='o')
plt.plot(dayas, tul, color='purple', marker='o')
plt.title(f'the stations {datas} data for month {time}', fontsize=14)
plt.xlabel('DAY', fontsize=14)
plt.ylabel(f'{datas}', fontsize=14)
plt.grid(True)
plt.legend(['ALTU', 'BEAV', 'NRMN', 'TISH', 'TULN'], loc='upper left')
plt.show()