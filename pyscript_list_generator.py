"""用于产生pyscript的目录内容"""
import os


class Generator:
    path = ""
    pyscript_list = []

    def __generator_pyscript_list(self):
        path = os.getcwd()
        self.path = path
        file_list = os.listdir(path)
        pyscript_list = []
        for file in file_list:
            if (file.split('.')[-1]) == "py":
                pyscript_list.append("".join(file.split('.')[0:-1]))

        pyscript_list.remove("pyscript_list_generator")
        pyscript_list.remove("__init__")
        pyscript_list.remove("server")
        self.pyscript_list = pyscript_list

    def __init__(self):
        self.__generator_pyscript_list()

    def generator_pyscript(self, pyscript):
        return None

    '''==='''


if __name__ == "__main__":
    generator = Generator()
