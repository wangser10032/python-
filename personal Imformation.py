# 个人信息
# Private information
import paramiko

# 服务器信息
SSH_HOST = 
SSH_PORT = 
SSH_USER = 
SSH_PASSWORD = 


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
SMTP_USER = 
SMTP_PASSWORD = 

# 邮箱信息
Email_cloud = 
Email_my = 

