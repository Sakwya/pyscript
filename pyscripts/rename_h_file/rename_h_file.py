import os
import tkinter as tk
from os import path as op
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class HFileRenamer:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()

    def __rename_h_dir(self, p_path):
        c_paths = os.listdir(p_path)
        for c_path in c_paths:
            n_path = op.join(p_path, c_path)

    def __rename_file(self, f_path):
        print(op.basename(f_path))

    def main(self):
        """选择目标路径"""
        mb.showinfo("", "请选择要拷贝的根目录")
        target_path = op.abspath(fd.askdirectory())
        c_paths = os.listdir(target_path)
        if 'root.info' in c_paths:
            c_paths.remove('root.info')
            root_info = open(op.join(target_path, 'root.info'), 'r+', encoding='utf-8')
            print(root_info.read())
            for c_path in c_paths:
                n_path = op.join(target_path,c_path)
                if op.isdir(n_path):
                    root_info.write(n_path)
                    root_info.write('\n')
            root_info.close()



if __name__ == '__main__':
    copier = HFileRenamer()
    copier.main()
