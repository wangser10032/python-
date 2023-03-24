# 发送邮件
import smtplib
from email.mime.text import MIMEText
import Monitor05_4 as PI
# import Monitor03_3 as RES  # resouces
# import Monitor03_4 as PI  # Private Information

# 系统资源邮件编辑
def Email_system_create(usage, pi):
    body = ''
    for key,value in usage.items():
        body = body + key +': ' + str(value) + '\n'
    esg_system = MIMEText(body)
    subject = 'Resource usage alert'
    esg_system['Subject'] = subject
    esg_system['From'] = pi.Email_cloud
    esg_system['To'] = pi.Email_my
    return esg_system

# 自动化告警系统邮件编辑
def Email_alarm_create():
    subject = '自动化告警系统'
    content = '系统发生异常，请及时处理！'
    esg_alarm = MIMEText(content)
    esg_alarm['Subject'] = subject
    esg_alarm['From'] = PI.Email_cloud
    esg_alarm['To'] = PI.Email_my
    return esg_alarm

# 发送邮件
def Email_send(esg, pi):
    smtp = smtplib.SMTP(pi.SMTP_HOST,
                        pi.SMTP_PORT)
    smtp.starttls()
    smtp.login(pi.SMTP_USER, pi.SMTP_PASSWORD)
    smtp.send_message(esg)
    smtp.quit()
    print('Email sent successfully')
