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
        self.root_path = ""
        self.routes = []
        self.route_memo = None
        self.change_root()

    def __del__(self):
        self.route_memo.close()

    def change_root(self):
        """选择目标路径"""
        messagebox.showinfo("", "请选择要拷贝的根目录")
        self.root_path = op.abspath(fd.askdirectory())

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
            self.routes.append(n_n_path)

    def main(self):
        if not os.path.exists(self.root_path + "_copy"):
            os.mkdir(self.root_path + "_copy")
        if self.route_memo:
            self.route_memo.close()
            print("成功关闭")
        self.route_memo = open(op.join(self.root_path + "_copy", "route_memo.info"), 'w+', encoding='utf-8')
        self.routes = []
        self.__copy_child_folder(self.root_path, self.root_path + "_copy")
        self.routes.sort()
        for route in self.routes:
            print(route)
            self.route_memo.write(route + '\n')


if __name__ == '__main__':
    copier = FolderTreeCopier()
    copier.main()
