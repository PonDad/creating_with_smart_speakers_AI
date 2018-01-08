import requests
import time, sys

request_emotion = ({0:'red',1:'green',2:'magenta',3:'yellow',
        4:'blue',5:'skyblue',6:'ivory'})

url = 'https://maker.ifttt.com/trigger/request_emotion/with/key/'
your_api_key = 'dnpZ7UmDsU9CK11t1CYOY_'

def change_light(predict):
    light_color = request_emotion[int(predict)]
    light_brightness = 50
    payload = {"value1":light_color,"value2":light_brightness}
    requests.post(url + your_api_key, data=payload)
    print(light_color, light_brightness)
    time.sleep(5)
    light_color = request_emotion[6]
    payload = {"value1":light_color,"value2":light_brightness}
    requests.post(url + your_api_key, data=payload)
    print(light_color, light_brightness)

if __name__== '__main__':
    change_light()
