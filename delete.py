import shutil
import os

def move_data():
    dir = os.listdir('./info')
    week = 'Week ' + str(int(dir[-1][-3:]) + 1)
    os.mkdir(f'./info/{week}')

    for file_name in os.listdir('./data/'):
        source = './data/' + file_name
        destination = './info/'+ week + '/' + file_name
        shutil.move(source, destination)

def refresh_data():
    dir = os.listdir('/home/willian/Downloads/me/')
    for file_name in dir:
        file = '/home/willian/Downloads/me/' + file_name
        os.remove(file)

def mi_fit():

        dirs = ['SPORT', 'SLEEP', 'ACTIVITY', 'HEARTRATE_AUTO', 'HEARTRATE', 'ACTIVITY_MINUTE', 'ACTIVITY_STAGE']
        for dir in dirs:
            try:
                shutil.rmtree(os.path.join('./data/', dir))
            except FileNotFoundError:
                pass

def main():
    valuate = input('Do you want to delete all Mi fit extracted data? [Y/n]: ')
    if valuate == 'y' or valuate == 'Y':
        mi_fit()
    valuate = input('Do you want to refreseh all data(non transform)? [Y/n]: ')
    if valuate == 'y' or valuate == 'Y':
        refresh_data()
    valuate = input('Move data(transformed) to a new week dir [Y/n]: ')
    if valuate == 'y' or valuate == 'Y':
        move_data()
