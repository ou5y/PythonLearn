# encoding=utf-8
class Networkerror(RuntimeError):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2


try:
    raise Networkerror("http", "locahost")
except Networkerror, e:
    print Networkerror
    print Networkerror.args
    print e.arg1
    print e.arg2


#
# try:
#     raise Exception("你发的你发的",'dsadsa')
# except Exception:
#     print Exception.message
# else:
#     print ''
#
#
# 定义函数
def temp_convert(var):
    try:
        raise ValueError("你发的你发的")
        return int(var)
    except ValueError, e:
        print "参数没有包含数字\n", Argument
    except Argument, h:
        print "fsdfds"


# 调用函数
temp_convert("xyz");
#
#
# def functionName(level):
#     if level < 1:
#         raise Exception("Invalid level!", level)
#         # 触发异常后，后面的代码就不会再执行

# try:

#     fh = open("testfile1", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# except IOError:
#     print "Error: 没有找到文件或读取文件失败"
# else:
#     print "内容写入文件成功"
#     fh.close()
# finally:
#     print "Error: 没有找到文件或读取文件失败"
