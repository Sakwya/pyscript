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
        video_tag = ['wmv', 'asf', 'asx', 'rm', 'rmvb', 'mpg', 'mpeg', 'mpe', '3gp', 'mov', 'mp4', 'm4v', 'avi', 'dat',
                     'mkv', 'flv', 'vob']
        if paths.split(".")[-1] in video_tag:
            os.rename(new_path, path + '/' + paths.replace(" 1", '').replace(" 2", '').replace(" 3", '').replace(" 4",
                                                                                                                 '').replace(
                " 5", '').replace(" 6", ''))


c = fd.askdirectory()
re_by_name(c)

'''
if __name__ == '__main__':
    mmm = mMm()
    mmm.mainloop()
'''
