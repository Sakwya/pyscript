import os
import re
import tkinter as tk
from os import path as op
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def is_num(data):
    """判断字符串是否为数字"""
    try:
        int(data)
        return True
    except:
        return False


def go_split(s, symbol):
    # 拼接正则表达式
    symbol = "[" + symbol + "]+"
    # 一次性分割字符串
    result = re.split(symbol, s)
    # 去除空字符
    return [x for x in result if x]


def takeSecond(elem):
    return elem[1]


class HFileRenamer:
    def __init__(self):
        root = tk.Tk()
        root.withdraw()
        self.root_path = None
        self.routes = []
        self.keys = {}
        self.change_root()

    def change_root(self):
        """选择目标路径"""
        mb.showinfo("", "请选择目标根目录")
        self.root_path = op.abspath(fd.askdirectory())

    def __rename_h_dir(self, p_path):
        c_paths = os.listdir(p_path)
        for c_path in c_paths:
            n_path = op.join(p_path, c_path)

    def __rename_file(self, f_path):
        print(op.basename(f_path))

    def __judge_root(self, r_path):
        c_paths = os.listdir(r_path)
        if 'root.info' in c_paths:
            c_paths.remove('root.info')
            root_info = open(op.join(r_path, 'root.info'), 'r+', encoding='utf-8')
            routes = root_info.read().split('\n')
            for c_path in c_paths:
                c_path = op.join(r_path, c_path)
                if c_path in routes:
                    self.__judge_root(c_path)
                else:
                    if op.isdir(c_path):
                        self.__rename_h_dir(c_path)
                    else:
                        self.__rename_file(c_path)

    def get_route(self):
        self.routes = []
        self.__get_route_(self.root_path)
        self.routes.sort()
        route_memo = open(op.join(self.root_path, "route_memo.info"), 'w+', encoding='utf-8')
        for route in self.routes:
            route_memo.write(route + '\n')
        route_memo.close()
        kk = []
        for key in self.keys.keys():
            kk.append([key, self.keys[key]])
        kk.sort(reverse=True, key=takeSecond)
        for k in kk:
            print(k[0], k[1])

    def __get_route_(self, p_path):
        c_paths = os.listdir(p_path)
        for c_path in c_paths:
            keys = go_split(c_path, ' 　_.()【】\n')
            for key in keys:
                if is_num(key):
                    key = int(key)
                if key in self.keys:
                    self.keys[key] = self.keys[key] + 1
                else:
                    self.keys[key] = 1
            c_path = op.join(p_path, c_path)
            if op.isdir(c_path):
                self.__get_route_(c_path)
            self.routes.append(c_path)

    def main(self):
        self.__judge_root(self.root_path)


if __name__ == '__main__':
    copier = HFileRenamer()
    copier.get_route()
