# 主函数运行
from Email import *  # 导入所有函数
from Monitor import Monitor  # resouces
import personal imformation as PI  # Private Information
import time


def run_Monitor(PI):
    monitor = Monitor(PI)
    usage = monitor.update()  # 此时返回的是字典
    ESG = Email_system_create(usage, PI)
    Email_send(ESG, PI)
    # 获取目前的cpu和内存使用情况
    cpu_check = monitor.get_cpu()
    mem_check = monitor.get_mem()
    # 设置CPU，内存使用率阈值
    cpu_alarm = 1.0
    mem_alarm = 90.0
    while True:
        # 检查cpu使用率是否超过阈值
        if cpu_check['cpu_usage'] > cpu_alarm:
            ESG = Email_alarm_create()
            Email_send(ESG, PI)
        # 检查内存使用率是否超过阈值
        if mem_check['mem_usage'] > mem_alarm:
            ESG = Email_alarm_create()
            Email_send(ESG, PI)
        time.sleep(7200)


run_Monitor(PI)
