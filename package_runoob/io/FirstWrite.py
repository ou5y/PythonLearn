# encoding=utf-8

def writeFile():
    # 没有try except finally
    f = open("hooker.txt", "w")
    f.write("你嗨一个瓜袜子")
    f.close()


def writeFileByWith():
    with open("hooker.txt", "a") as f:
        f.write("hp")


writeFile()

writeFileByWith()
