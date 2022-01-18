STID = []
MAXTEMP = []
import csv 
list = ['ARD2', 'BEAV', 'BOIS', 'CENT', 'NRMN', 'STIL', 'TISH', 'TULN', 'WOOD']
data = open('/home/mdolan/Desktop/git_prog/BigData2016 (1).csv', newline='') 
with data as csvfile:
    reader = csv.DictReader(csvfile)
    station_list = []
    for part in list:
        maxes = -996.0
        mins = 996.0
        data.seek(0)
        for num in reader:
            if num['STID'] == part:
                if float(num['TMAX']) != 996.00 and float(num['TMAX']) != -996.00:
                    if float(num['TMAX']) > maxes:
                        maxes = float(num['TMAX'])
                    if float(num['TMIN']) < mins:
                        mins = float(num['TMIN'])
        print(f'{part}; max:{maxes}, min:{mins}.')
        STID.append(part)
        MAXTEMP.append(maxes)
        
import matplotlib.pyplot as plt
plt.plot(STID, MAXTEMP, color='blue', marker='X')
plt.title('Maximum Temprature At Each Station', fontsize=14)
plt.xlabel('Station', fontsize=14)
plt.ylabel('Maximum Temprature', fontsize=14)
plt.grid(True)
plt.show()s