# encoding=utf-8

def readFile():
    try:
        f = open("foo.txt", "r")
        content = f.read()
        print content
    except BaseException, e:
        print e
    finally:
        if f:
            f.close()


def readFileByWith():
    # 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
    with open("foo.txt", "r") as f:
        print f.read()


def readFileByWithAndSzie():
    with open("foo.txt", "r") as f:
        for oneline in f.readlines():
            print oneline.strip()  # 把末尾的'\n'删掉


readFile()

readFileByWith()

readFileByWithAndSzie()
