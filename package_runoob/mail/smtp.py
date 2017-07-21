#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


smtp_server = 'smtp.sina.com.cn'  # 输入SMTP服务器地址
from_addr = 'baipan_kobe@sina.com'  # 输入Email地址和口令
password = 'usb125800'  # 输入Email地址和口令
to_addr = '977945732@qq.com'  # 输入收件人地址

# 第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
# 如果要发送HTML邮件，而不是普通的纯文本文件，在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
server.set_debuglevel(1)  # 可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

print 'SUCCESS'
