import unzip as extract
import health
import delete
import os

def extract_data():
    dir_name = '/home/willian/Downloads/me/'
    dir = os.listdir(dir_name)
    for file_name in dir:
        file = dir_name + file_name
        extract.main(file)

    return 'Files extracted'

def main():
    print(extract_data())
    health.main()
    delete.main()


if __name__ == '__main__': main()