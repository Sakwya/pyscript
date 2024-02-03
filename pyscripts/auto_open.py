import sys
from os import system

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(0)

    file_name = sys.argv[1]
    file_type = file_name.split('.')[-1]
    if file_type == 'zip' or 'rar':
        try:
            system('F:\\Winrar\\WinRAR.exe "{0}"'.format(file_name))
        except Exception:
            print('ERROR: F:\\Winrar\\WinRAR.exe "{0}"'.format(file_name))
    system("pause")
