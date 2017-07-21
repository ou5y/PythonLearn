# encoding=utf-8
import json

d = dict(name='Bob', age=20, score=88)
# 序列化    dict到json
print json.dumps(d)  # dumps()方法返回一个str，内容就是标准的JSON。

with open("json.data", "w") as f:  # 类似的，dump()方法可以直接把JSON写入一个file-like Object
    json.dump(d, f)

# 反序列化   json到dict
# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。
loadsDict = json.loads(json.dumps(d))  # 用loads()把JSON的字符串反序列化
print loadsDict  # {u'age': 20, u'score': 88, u'name': u'Bob'}

with open("json.data", "r") as f:
    loadDict = json.load(f)  # 从file-like Object中读取字符串并反序列化
    print loadDict  # {u'age': 20, u'score': 88, u'name': u'Bob'}
    print type(loadDict)  # <type 'dict'>
    print loadDict["age"]  # 20
    print loadDict.get("name")  # Bob


# class的序列化与反序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob校长', 20, 88)
print json.dumps(s, default=student2dict, ensure_ascii=False)  # 显示用函数转{"age": 20, "score": 88, "name": "Bob校长"}
print json.dumps(s, default=lambda obj: obj.__dict__)  # 用匿名函数简写{"age": 20, "score": 88, "name": "Bob\u6821\u957f"}


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob小红"}'
print json.loads(json_str, object_hook=dict2student, encoding='utf-8')
