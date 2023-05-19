import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd


def re_by_name(path):
    folder = os.listdir(path)
    for paths in folder:
        if paths.split('.')[-1] == "C":
            new_path = path + '/' + paths
            os.rename(new_path, new_path.replace('.C.C','.tar'))
'''c = fd.askdirectory()'''

c="G:\pan4.27\.hmoe\！Geass"
re_by_name(c)

'''
if __name__ == '__main__':
    mmm = mMm()
    mmm.mainloop()
'''
