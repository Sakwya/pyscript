"""怪猎涩涩装备复制用脚本"""
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog


class FolderCopier:
    def info(self):
        self.__
        return """怪猎涩涩装备复制用脚本"""

    def __addFolder(self, p_dic, f_path):
        f_plist = os.listdir(f_path)
        for f_p in f_plist:
            f_p = f_path + '/' + f_p
            if os.path.isdir(f_p):
                self.__addFolder(p_dic, f_p)
            else:
                p_dic.append(f_p)

    def __createFolder(self, f_path):
        if not os.path.exists(f_path[:f_path.rindex('/')]):
            print(f_path[:f_path.rindex('/')])
            self.__createFolder(f_path[:f_path.rindex('/')])
        os.mkdir(f_path)

    def __init__(self):
        root = tk.Tk()
        root.withdraw()

    def copy_folder(self):
        messagebox.showinfo("", "请选择目标文件夹")
        target_path = filedialog.askdirectory()
        path_dic = []
        new_dic = []
        self.__addFolder(path_dic, target_path)
        origin = simpledialog.askfloat(title='', prompt='输入原装备id')
        while origin != int(origin) or origin < 1 or origin > 501:
            print(origin)
            messagebox.showerror("", "请输入正确的值!")
            origin = simpledialog.askfloat(title='', prompt='输入原装备id')
        origin = str(int(origin)).zfill(3)
        new = simpledialog.askfloat(title='', prompt='输入需要替换的装备id')
        print(3)
        print(4)
        while new != int(new) or new < 1 or new > 501:
            print(new)
            messagebox.showerror("", "请输入正确的值!")
            new = simpledialog.askfloat(title='', prompt='输入需要替换的装备id')
        new = str(int(new)).zfill(3)
        for path in path_dic:
            if origin in str(path):
                new_dic.append(path.replace(origin, new))

        if len(path_dic) == len(new_dic):
            for i in range(0, len(path_dic)):
                print(str(i).zfill(2) + " " + path_dic[i])
                print("   " + new_dic[i])
                if not os.path.exists(new_dic[i][:new_dic[i].rindex("/")]):
                    self.__createFolder(new_dic[i][:new_dic[i].rindex("/")])
                shutil.copy(path_dic[i], new_dic[i])
        else:
            print(origin)
            print(new)
            print(path_dic)
            print(new_dic)
            messagebox.showerror("", "复制过程出错")


if __name__ == "__main__":
    '''
    copier = FolderCopier()
    copier.copy_folder()
    '''
    a = FolderCopier
    print(a.__doc__)
    print(a.__dict__)
    print(a.__name__)