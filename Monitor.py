# 连接到服务器
import psutil
import Monitor05_4 as PI
import time


class Monitor:
    def __init__(self, pi):
        self.pi = pi
        # 建立资源空白列表
        self.usage = {}
        # 建立cpu,mem,io字典
        self.CPU_usage = {}
        self.MEM_usageNET_usage = {}
        self.SYSTEM_usage = {}
        self.PROCESS_usage = {}

    # 字典保存数据
    def update(self):
        CPU_usage, MEM_usage, NET_usage, SYSTEM_usage, PROCESS_usage = self.get_information()
        self.usage['cpu'] = CPU_usage
        self.usage['mem'] = MEM_usage
        self.usage['net'] = NET_usage
        self.usage['sys'] = SYSTEM_usage
        self.usage['pc'] = PROCESS_usage
        return self.usage

    # 获取资源利用率
    def get_information(self):
        #self.user_connect()
        self.pi.user_connect()
        CPU_usage = self.get_cpu()
        MEM_usage = self.get_mem()
        NET_usage = self.get_net()
        SYSTEM_usage = self.get_system()
        PROCESS_usage = self.get_process()
        # 返回皆为字典
        return CPU_usage, MEM_usage, NET_usage, SYSTEM_usage, PROCESS_usage

    # CPU使用情况
    def get_cpu(self):
        # 定义字典获取CPU信息
        cpu = {}
        # 获取cpu使用率并将其转换为字符串
        # cpu_usage = str(psutil.cpu_percent())
        # 获取之前和现在的cpu时间
        pre_cpu_times = psutil.cpu_times()
        psutil.cpu_percent(interval=1)
        cur_cpu_times = psutil.cpu_times()
        pre_total_time = sum(pre_cpu_times)
        cur_total_time = sum(cur_cpu_times)
        # 计算时间间隔
        time_interval = cur_total_time - pre_total_time
        # 获取空闲时间间隔
        pre_idle_time = pre_cpu_times.idle
        cur_idle_time = cur_cpu_times.idle
        idle_time_interval = cur_idle_time - pre_idle_time
        # 计算cpu使用率
        cpu_usage = 100.0 - (idle_time_interval / time_interval) * 100.0
        cpu_count = psutil.cpu_count()
        # f = open("/proc/loadavg")  # 打开文件获取负载open( self._load_avg_info_path, 'r' )
        # with open('/proc/loadavg') as f: # 失败
        # cin = f.read().split()  # CPU_information
        try:
            f = open("/proc/loadavg")
            cin = f.read().split()
            cpu['cpuload_1'] = cin[0]
            cpu['cpuload_5'] = cin[1]
            cpu['cpuload_15'] = cin[2]
            f.close()
        except FileNotFoundError:
            print("Failed to open path:'/proc/loadavg', We pass cpuload!")

        cpu['cpu_count'] = cpu_count
        cpu['cpu_usage'] = round(cpu_usage,2)
        # cpu['cpuload_1'] = cin[0]
        # cpu['cpuload_5'] = cin[1]
        # cpu['cpuload_15'] = cin[2]
        return cpu

    # 内存使用情况
    def get_mem(self):
        mem = {}
        # 内存使用率/内存总计/剩余内存/used/free
        mem_usage = psutil.virtual_memory().percent
        mem_total = psutil.virtual_memory().total
        mem_available = psutil.virtual_memory().available
        mem_used = psutil.virtual_memory().used
        mem_free = psutil.virtual_memory().free
        mem['mem_usage'] = mem_usage
        # 处理数据将其单位转化为MB字符串化并保存
        mem['mem_total'] = str(round(mem_total / (1024 * 1024), 2))
        mem['mem_available'] = str(round(mem_available / (1024 * 1024), 2))
        mem['mem_used'] = str(round(mem_used / (1024 * 1024), 2))
        mem['mem_free'] = str(round(mem_free / (1024 * 1024), 2))
        return mem

    # 取得网络信息
    def get_net(self):
        net = {}
        bytes_sent = psutil.net_io_counters()[0]
        bytes_recv = psutil.net_io_counters()[1]
        net['bytes_sent'] = str(round(bytes_sent / (1024 * 1024), 2))
        net['bytes_recv'] = str(round(bytes_recv / (1024 * 1024), 2))
        io_usage = psutil.disk_usage('/').percent
        net['io_usage'] = io_usage
        return net

    # 获取系统信息
    def get_system(self):
        system = {}
        # 用户名/终端信息/远程主机信息/登陆时间
        # psutil.users()返回的是字典
        system['user'] = psutil.users()[0].name
        system['terminal'] = psutil.users()[0].terminal
        system['host'] = psutil.users()[0].host
        # 获取时间为时间戳
        time_cuo = psutil.users()[0].started
        time_local = time.localtime(time_cuo)
        Local_time = time.strftime('%Y-%m-%d %H:%M:%S', time_local)
        system['time'] = Local_time
        return system

    def get_process(self):
        # 获取进程信息(name)
        Process = {}
        iter_list = list(psutil.process_iter())[:3]  # 输出的是列表
        # 列表元素之一形式：psutil.Process(pid=0, name='System Idle Process', status='running')
        # 初始化，只取三个

        # 赋值并转化为字符串
        process_0 = 'name: ' + iter_list[0].name() + '; status: ' + iter_list[0].status()
        process_1 = 'name: ' + iter_list[1].name() + '; status: ' + iter_list[1].status()
        process_2 = 'name: ' + iter_list[2].name() + '; status: ' + iter_list[2].status()

        # 赋给字典
        Process['process_01'] = process_0
        Process['process_02'] = process_1
        Process['process_03'] = process_2
        return Process

    # 连接到远程Linux服务器
    # def user_connect(self):
    #     user = paramiko.SSHClient()
    #     user.set_missing_host_key_policy(
    #         paramiko.AutoAddPolicy())
    #     user.connect(
    #         self.pi.SSH_HOST,
    #         self.pi.SSH_PORT,
    #         self.pi.SSH_USER,
    #         self.pi.SSH_PASSWORD
    #     )


monitor = Monitor(PI)
