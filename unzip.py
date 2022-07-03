import zipfile

def main(file_name1,file_name2):
    with zipfile.ZipFile(file_name1) as file:
        file.extractall('/home/willian/me/data')
    with zipfile.ZipFile(file_name2) as file:
        file.extractall('/home/willian/me/data')

