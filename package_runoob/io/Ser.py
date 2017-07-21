# encoding=utf-8
try:
    import cPickle as pickle
except ImportError:
    import pickle


class Dict(dict):
    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)


d = Dict(name='Bob', age=20, score=88)
# **********序列化**********
# 把任意对象序列化成一个str，然后，就可以把这个str写入文件:
sdata = pickle.dumps(d)
print sdata  # sdata需要自己单独写入文件

# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
with open("ser.data", "wb") as f:
    print pickle.dump(d, f)

# **********反序列化**********
with open("ser.data", "rb") as f:
    newD = pickle.load(f)
    print newD
    print newD.__str__() == d.__str__()  # True
