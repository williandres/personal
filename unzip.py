import zipfile

def main(file):
    with zipfile.ZipFile(file) as f:
        f.extractall('/home/willian/me/data')

