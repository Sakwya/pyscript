import os

for filename in os.listdir(os.getcwd()):
    if '_' in filename:
        os.rename(filename, filename.split('_', 1)[1])
