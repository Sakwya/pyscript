"""怪猎涩涩装备复制用脚本"""
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

'''原文件目录id与目的替换装备的id'''
old = "124"
new = "075"

messagebox.showinfo("", "请选择目标文件夹")
target_path = filedialog.askdirectory()


def addFolder(p_dic, f_path):
    f_plist = os.listdir(f_path)
    for f_p in f_plist:
        f_p = f_path + '/' + f_p
        if os.path.isdir(f_p):
            addFolder(p_dic, f_p)
        else:
            p_dic.append(f_p)


def createFolder(f_path):
    if not os.path.exists(f_path[:f_path.rindex('/')]):
        print(f_path[:f_path.rindex('/')])
        createFolder(f_path[:f_path.rindex('/')])
    os.mkdir(f_path)


path_dic = []
new_dic = []
addFolder(path_dic, target_path)

for path in path_dic:
    if old in str(path):
        new_dic.append(path.replace(old, new))

if len(path_dic) == len(new_dic):
    for i in range(0, len(path_dic)):
        print(str(i).zfill(2) + " " + path_dic[i])
        print("   " + new_dic[i])
        if not os.path.exists(new_dic[i][:new_dic[i].rindex("/")]):
            createFolder(new_dic[i][:new_dic[i].rindex("/")])
        shutil.copy(path_dic[i], new_dic[i])
