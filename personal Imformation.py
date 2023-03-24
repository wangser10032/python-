# 个人信息
# Private information
import paramiko

# 服务器信息
SSH_HOST = '120.27.210.113'
SSH_PORT = 22
SSH_USER = 'root'
SSH_PASSWORD = '@w3016927834'


# 服务器连接
def user_connect():
    user = paramiko.SSHClient()
    user.set_missing_host_key_policy(
        paramiko.AutoAddPolicy()
    )
    user.connect(
        SSH_HOST,
        SSH_PORT,
        SSH_USER,
        SSH_PASSWORD
    )


# SMTP信息
SMTP_HOST = 'smtp.163.com'
SMTP_PORT = 25
SMTP_USER = 'zuisui163@163.com'
SMTP_PASSWORD = 'JDZTUPUPNDYBHRPX'

# 邮箱信息
Email_cloud = 'zuisui163@163.com'
# Email_my = 'xxxpcsc@163.com'
Email_my = '1942415139@qq.com'
# Email_my = '1638937277@qq.com'
