import datetime
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class INFLUX:
    # Class of influx DB
    def __init__(self):
        self.token = "noTJY-a4xdFxn-P_WJmmhT9BA-Pvue4Q9Xi_qQwfKgWuPCtVYS3qAEz6xQnec2uYrHMW8xj39Jk6pOhB-AVDuA=="
        self.org = "test"
        self.bucket = "core"
        self.influx_server = "http://172.16.130.22:8086"
        self.client = influxdb_client.InfluxDBClient(url=self.influx_server, token=self.token, org=self.org)
        self.api_writer = self.client.write_api(write_options=SYNCHRONOUS)
        self.api_query = self.client.query_api()

    def write(self, pname, field_tup, time_ay=False):
        if time_ay:
            time_v = datetime.datetime.fromtimestamp(time_ay/1000)
            data_point = influxdb_client.Point(pname).field(field_tup[0], field_tup[1]).time(time_v)
        else:
            data_point = influxdb_client.Point(pname).field(field_tup[0], field_tup[1])
        self.api_writer.write(bucket=self.bucket, org=self.org, record=data_point)
        
    def query(self, flux):
        return self.api_query.query(org=self.org, query=flux)