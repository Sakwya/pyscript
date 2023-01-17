"""用于产生pyscript的目录内容"""
import os
from os import path as op


class Generator:
    path = ""
    pyscript_list = []
    pyscript_dic = {}

    def __generator_pyscript_list(self):
        path = op.join(os.getcwd(), "pyscripts")
        self.path = path
        print(self.path)
        file_list = os.listdir(path)
        pyscript_list = []
        for file in file_list:
            if op.isdir(op.join(path, file)):
                pyscript_list.append(file)
        self.pyscript_list = pyscript_list
        self.pyscript_dic

    def __init__(self):
        self.__generator_pyscript_list()

    def generator_pyscript(self, pyscript):
        path = op.join(self.path, pyscript)
        if not op.isdir(path):
            return 'EOF'
        file_list = os.listdir(path)
        script_list =[]
        for file in file_list:
            if file.split('.')[-1]=='py':
                script_list.append(file)
        return script_list

    '''==='''


if __name__ == "__main__":
    generator = Generator()
