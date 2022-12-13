import os
from os import path as op

path = "G:\\BAIDU DISK_copy\\root.info"
info = open(path,'r+',encoding='utf-8')
i =info.read()
info.write(i)
info.seek(0,0)
print(info.read(),'end')
info.close()