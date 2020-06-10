from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def sendemail(report):
    # 读取报告内容
    with open(report,'rb') as file:
        mail_content = file.read()
    # 邮箱smtp服务器
    smtpserver='smtp.qq.com'
    # 用户名smtp服务的密码
    user='2821644642@qq.com'
    password='acrcpkjqxbckdfbc'
    # 发送和接收邮箱用户
    sender = '2821644642@qq.com'
    receiver = '583870243@qq.com'
    # 发送给多人
    # receiver = ['123@qq.com','23432@qq.com','719584032@qq.com']
    # 定义邮件内容
    title = 'UI自动化测试报告(详细见附件)'
    msg=MIMEMultipart()
    # 邮件标题
    msg['subject'] = Header(title, 'utf-8').encode()
    # 发送人
    msg['from'] = sender
    # 接收人
    msg['to'] = receiver
    # 邮件内容
    body = MIMEText(mail_content, 'html', 'utf-8')
    msg.attach(body)
    # 邮件附件
    att=MIMEText(mail_content,'base64','utf-8')
    att['Content-type']='application/octet-stream'
    att['Content-Disposition']='attachment;filename="IeAllReport.html"'
    msg.attach(att)
    # 连接SMTP服务
    smtp = SMTP(smtpserver,25)
    # 登陆用户
    smtp.login(user,password)
    # 发送邮件
    smtp.sendmail(sender,receiver,msg.as_string())
    # 关闭连接
    smtp.quit()