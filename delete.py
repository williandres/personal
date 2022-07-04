import shutil
import os

def refresh_data():
    dir = os.listdir('/home/willian/Downloads/me/')
    for file_name in dir:
        file = '/home/willian/Downloads/me/' + file_name
        os.remove(file)

def mi_fit():
    try:
        dirs = ['SPORT', 'SLEEP', 'ACTIVITY', 'HEARTRATE_AUTO', 'HEARTRATE', 'ACTIVITY_MINUTE', 'ACTIVITY_STAGE']
        for dir in dirs:
            shutil.rmtree(os.path.join('./data/', dir))
    except FileNotFoundError:
        pass

def main():
    mi_fit()
    valuate = input('Do you want to refreseh all data(non transform) [Y/n]: ')
    if valuate == 'y' or valuate == 'Y':
        refresh_data()
