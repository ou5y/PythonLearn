# coding=utf-8



dict = {('Name', 'namele'): 'Zara', 'Age': 7};

for temp in dict.keys():
    print dict[temp]

for temp in dict.items():
    print temp

list1 = ['physics', 'chemistry', 1997, 2000];

print list1;
del list1[1];
print "After deleting value at index 2 : "
print list1;
var1 = 'Hello World!'
var2 = 'Hello World!'
print var1 is var2
print var1 == var2

print "更新字符串 :- ", var1[:6] + 'Runoob!'

str = "nihao".decode(encoding='UTF-8', errors='strict')

print str

print "My name is %s and weight is %d kg!" % ('Zara', 21)

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=BackD
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''

# print errHTML

# print u'Hello World !'
