import unzip as extract
import health
import delete
import os
import shutil

def extract_data():
    dir_name = '/home/willian/Downloads/me/'
    dir = os.listdir(dir_name)
    for file_name in dir:
        file = dir_name + file_name
        extract.main(file)

    return 'Files extracted'

def main():
    execute = False
    while execute:
        valuate = input('All data (non*transformed) are ready in the entry dir? [Y/n]: ')
        if valuate == 'y' or valuate == 'Y':
            execute = True
    print(extract_data())
    health.main()
    delete.main()
    print('Work done')


if __name__ == '__main__': main()