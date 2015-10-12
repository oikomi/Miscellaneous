


from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#创建一个带附件的实例
msg = MIMEMultipart()

#构造附件1
att1 = MIMEText(open('./sb-bench/sb-output.log', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="result"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)

# #构造附件2
# att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="123.txt"'
# msg.attach(att2)

#加邮件头
msg['to'] = 'miaohong@miaohong.org'
msg['from'] = 'miaohong0436104@163.com'
msg['subject'] = 'result'
#发送邮件
try:
	server = smtplib.SMTP()
	server.connect('smtp.XXX.com')
	server.login('XXX','XXXXX')#XXX为用户名，XXXXX为密码
	server.sendmail(msg['from'], msg['to'],msg.as_string())
	server.quit()
	print '发送成功'
except Exception, e:  
	print str(e) 