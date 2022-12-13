"""文件树目录拷贝脚本"""
import os
from os import path as op
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox


class FolderTreeCopier:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()

    def __copy_child_folder(self, p_path, n_path):
        c_paths = os.listdir(p_path)
        for c_path in c_paths:
            n_p_path = op.join(p_path, c_path)
            n_n_path = op.join(n_path, c_path)
            if op.isdir(n_p_path):
                if not op.exists(n_n_path):
                    os.mkdir(n_n_path)
                self.__copy_child_folder(n_p_path, n_n_path)
            else:
                os.open(n_n_path, os.O_CREAT)


    def copy_folder_tree(self):
        """选择目标路径"""
        messagebox.showinfo("", "请选择要拷贝的根目录")
        target_path = fd.askdirectory()
        if not os.path.exists(target_path + "_"):
            os.mkdir(target_path + "_")
        self.__copy_child_folder(target_path, target_path + "_")


if __name__ == '__main__':
    copier = FolderTreeCopier()
    copier.copy_folder_tree()
