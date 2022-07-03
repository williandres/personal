import unzip as extract
import health as hp
import os

def main():
    file1 = '/home/willian/Downloads/me/' + os.listdir('/home/willian/Downloads/me')[0]
    file2 = '/home/willian/Downloads/me/' + os.listdir('/home/willian/Downloads/me')[1]
    extract.main(file1, file2)
    print('Extracted files')
    hp.main()


if __name__ == '__main__': main()