import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd


def re_by_name(path):
    folder = os.listdir(path)
    for paths in folder:
        if paths[-1] == "删":
            new_path = path + '/' + paths
            os.rename(new_path, new_path.rstrip('删'))
        elif paths.split('.')[-1]=="png":
            new_path = path + '/' + paths
            os.rename(new_path, new_path.rstrip("png")+"7z")
            


def re_by_folder(path):
    folder = os.listdir(path)
    for paths in folder:
        new_path = path + '/' + paths
        if os.path.isfile(new_path):
            os.rename(new_path, new_path.replace(" 1.mp4", '.mp4'))
            continue
        files = os.listdir(new_path)
        for file in files:
            shutil.move(new_path + '/' + file, path + '/' + paths + ' ' + file.rstrip('删'))
        os.rmdir(new_path)


c = fd.askdirectory()
re_by_name(c)

'''
if __name__ == '__main__':
    mmm = mMm()
    mmm.mainloop()
'''
