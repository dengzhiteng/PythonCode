# importing os module 
import os

# 处理当前工作目录
# cwd = os.getcwd()
# print("Current working directory:", cwd)

# 回到上一级
# os.chdir('../')

# 当前位置
def current_path():
    return os.getcwd()

# 创建单个文件夹
def creatFolder(directory):
    parent_dir = current_path()
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

# 创建多个文件夹
def creatMoreFolder(directory):
    parent_dir = current_path()
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)

# 列出文件和目录
# os.chdir('../')
# print(os.listdir())

# 删除空文件
def removedir(fileName):
    os.removedirs(fileName)

# 删除文件
def removeFile(fileName):
    parent_dir = current_path()
    path = os.path.join(parent_dir, fileName)
    os.remove(path)

# creatFolder('111')
# removedir('111')
# removeFile('test.txt')

# os name
# os.chdir('../')
# print(os.name)

print(os.unlink())
