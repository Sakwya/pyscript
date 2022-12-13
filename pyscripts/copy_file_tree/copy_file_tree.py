"""文件树目录拷贝脚本"""
import os
import shutil
from tkinter import filedialog as fd


class FolderTreeCopier:
    def info(self):
        return """文件树目录拷贝脚本"""




c = fd.askdirectory()
re_by_folder(c)

'''
if __name__ == '__main__':
    mmm = mMm()
    mmm.mainloop()
'''
