import time
from local_monitor import Zabbix

def run():
    local_ins = Zabbix()
    local_ins.zabbix_monitor()

if __name__ == "__main__":
    while True:
        run()
        time.sleep(30)