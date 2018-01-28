import requests
import time

hue_api = 'http://192.168.0.3/api/jXEIOF3MgghGTlyJfuwKSpHyo1mcwpf2npYGVK2R/lights'

study_on = {"on":True, "bri":127,"hue":41442,"sat":75}
study_off = {"on":False}

def hue_on():
    requests.put(hue_api + '/1/state', json = study_on)

def hue_off():
    requests.put(hue_api + '/1/state', json = study_off)

if __name__ == '__main__':
    hue_on()
    hue_off()
