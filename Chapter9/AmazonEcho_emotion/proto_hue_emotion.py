import requests
import time

hue_api = 'http://192.168.0.3/api/jXEIOF3MgghGTlyJfuwKSpHyo1mcwpf2npYGVK2R/lights'

request_emotion = ({0:'64800',1:'23895',2:'52707',3:'11356',
        4:'46014,',5:'38539',6:'8595'})

def change_light(predict):
    light_color = request_emotion[int(predict)]
    requests.put(hue_api + '/1/state', json = {"on":True, "bri":127,"hue":light_colo ,"sat":200})

def neutral_light():
    requests.put(hue_api + '/1/state', json = {"on":True, "bri":127,"hue":41442,"sat":75})

if __name__ == '__main__':
    main()
