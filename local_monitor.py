from utils import INFLUX
from pyzabbix.api import ZabbixAPI



class Zabbix:
    def __init__(self):
        self.zapi = ZabbixAPI(url='http://183.6.42.206:3031/', user='Admin', password='zabbix')
        self.host_list = ['ACC1', 'ACC2', 'CO1', 'CO2']
        self.need_list = ['ICMP response time']
        self.host_id_list = [info['hostid'] for info in \
                             self.zapi.host.get(monitored_hosts=1, output='extend') \
                                if info['host'] in self.host_list]
        self.influx = INFLUX()

    def get_item_dict(self, hostid, need_list):
        result = self.zapi.item.get(hostids=hostid)
        return {info['itemid']:info['name'] for info in result if info['name'] in need_list}

    def zabbix_monitor(self):
        for i in range(len(self.host_id_list)):
            host_id = self.host_id_list[i]
            device_name = self.host_list[i]
            item_dict = self.get_item_dict(host_id, self.need_list)
            ping_resp = self.zapi.item.get(itemids=list(item_dict.keys()))
            item_name = device_name + "_ICMP response time"
            ping_value = float(ping_resp[0]['lastvalue'])*1000
            self.influx.write('Local_'+device_name, [item_name, ping_value])

    def close(self):
        self.zapi.user.logout()