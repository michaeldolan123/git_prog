import csv 
with open('Norman2016.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    maxes = -996.00
    mins = 996.00
    num_max_sum = 0.00
    num_min_sum = 0.00
    sum = 0
    for num in reader:
        if float(num['TMAX']) != 996.00 and float(num['TMAX']) != -996.00:
            if float(num['TMAX']) > maxes:
                maxes = float(num['TMAX'])
            if float(num['TMIN']) < mins:
                mins = float(num['TMIN'])
            num_max_sum += float(num['TMAX'])
            num_min_sum += float(num['TMIN'])
            sum += 1
    min_av = num_min_sum / sum
    max_av = num_max_sum / sum
    print(f' Your maximun temprature is {maxes} your minumum temprature is {mins}.')
    print(f'Your max average is {round(max_av, 2)} your min average is {round(min_av, 2)}.')