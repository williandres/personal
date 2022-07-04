import csv
import os

def read_csv(file_name):
    with open(f"{file_name}","r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        tittles_buses = next(reader)
        file = []
        for row in reader:
            file.append(row)
    return file

def write_csv(csv_name, list):
    with open(f"{csv_name}","w", encoding = "utf-8", newline='') as f:
        writer = csv.writer(f)
        for row in list:
            writer.writerow(row)

def excercise():
    file = read_csv('./data/SPORT/' + os.listdir('./data/SPORT/')[0])
    list = [['startTime','sportTime(s)','exercise_type','calories(kcal)']]
    for row in file:
        line = [row[1], row[2], row[0], row[7]]
        list.append(line)
    write_csv('./data/health/exercise.csv', list )

    return 'Exercise file done'

def steps():
    file = read_csv('./data/ACTIVITY/' + os.listdir('./data/ACTIVITY//')[0])
    list = [['date', 'steps', 'calories(kcal)']]
    for row in file:
        line = [row[0], row[2], row[5]]
        list.append(line)
    write_csv('./data/health/steps.csv', list )

    return 'Steps file done'

def sleep():
    file = read_csv('./data/SLEEP/' + os.listdir('./data/SLEEP/')[0])
    list = [['date','deepSleepTime(mins)','shallowSleepTime(mins)','wakeTime(mins)', 'totalTime(mins)']]
    for row in file:
        line = [row[0], row[2], row[3], row[4], ((int(row[6])-int(row[5]))-int(row[4]))/60]
        list.append(line)
    write_csv('./data/health/sleep.csv', list )

    return 'Sleep time file done'

def main():
    print(excercise())
    print(steps())
    print(sleep())
