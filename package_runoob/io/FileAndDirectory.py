# encoding=utf-8
import os
import shutil

print os.name  # 系统名称，如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print os.environ  # 环境变量
print os.getenv("Path")  # Path环境变量
print os.path.abspath('.')  # 查看当前目录的绝对路径

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
print os.path.join("D:/WORK", "workspace_qingshu")  # 拼接路径 (Windows下：D:/WORK\workspace_qingshu)
print os.path.split("D:/WORK/workspace_qingshu")  # 拆分路径 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print os.path.splitext("D:/WORK/workspace_qingshu/a.txt")  # 拆分路径 可以直接让你得到文件扩展名

print os.mkdir('D:/WORK/workspace_qingshu/PythonLearn/package_runoob/io/testdir')  # 创建一个目录
print os.rmdir('D:/WORK/workspace_qingshu/PythonLearn/package_runoob/io/testdir')  # 删掉一个目录

print os.rename('foo.txt', 'fool.txt')  # 重命名
print os.remove("fool.txt")  # 删除文件

print shutil.copyfile("foo.txt", "foo_copy.txt")  # 复制
print shutil.move("res", "target")  # 移动

# 当前目录所有的文件或目录
print [x for x in os.listdir('.')]

# 当前目录所有的py文件或目录
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
