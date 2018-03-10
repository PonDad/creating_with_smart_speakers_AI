import requests
import time

hue_api = 'http://192.168.0.3/api/jXEIOF3MgghGTlyJfuwKSpHyo1mcwpf2npYGVK2R/lights'

red = {"on":True, "bri":127,"hue":64618,"sat":248}
green = {"on":True, "bri":127,"hue":31937,"sat":227}
magenta = {"on":True, "bri":127,"hue":50633,"sat":223}
yellow = {"on":True, "bri":127,"hue":12049,"sat":254}
blue = {"on":True, "bri":127,"hue":45852,"sat":252}
skyblue = {"on":True, "bri":127,"hue":39462,"sat":174}
ivory = {"on":True, "bri":127,"hue":9032,"sat":75}

request_emotion = ({0:red,1:green,2:magenta,3:yellow,
        4:blue,5:skyblue,6:ivory})

def change_light(predict):
    light_color = request_emotion[int(predict)]
    requests.put(hue_api + '/1/state', json = light_color)
    time.sleep(1)
    requests.put(hue_api + '/1/state', json = {"on":True, "bri":127,"hue":41442,"sat":75})
    time.sleep(1)

if __name__ == '__main__':
    main()
