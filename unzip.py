import zipfile
import pyzipper

def main(file):
    try:
        with zipfile.ZipFile(file) as f:
            f.extractall('/home/willian/me/data')
    except RuntimeError:
        wrong_pswd = True
        with pyzipper.AESZipFile(file) as f:
            while wrong_pswd:
                try:
                    f.extractall(path='/home/willian/me/data', pwd = bytes(input(f'Password to unzip a file ({file}): '), 'utf-8'))
                    wrong_pswd = False
                except RuntimeError:
                    pass