import time
import json
from tinydb import TinyDB,Query

db = TinyDB("db.json")
sensor = Query()

def start():
    start_time = time.time()
    db.update({"value":start_time},sensor.key == "read_start")

def stop():
    stop_time = time.time()
    db.update({"value":stop_time},sensor.key == "read_stop")

    start_time = db.search(sensor.key == "read_start")[0]["value"]

    result_time = stop_time - start_time
    if result_time > 3600:
        h = int(result_time / 3600)
        m = int((result_time - h)/600)
        read_time = (str(h) + "時間",str(m) + "分")
        print(read_time)
        return read_time
    elif result_time < 3600:
        m = int(result_time / 600)
        read_time = str(m) + "分"
        print(str(m) + "分")
        return read_time

if __name__ == '__main__':
    start()
    stop()
