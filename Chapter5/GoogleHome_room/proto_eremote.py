import subprocess

path = "python3 rm2_controller/BlackBeanControl.py -c "

cmd = ["temp_on","temp_off","hum_on","hum_off"]

def temp_on():
    subprocess.call(path + cmd[0],shell=True)

def temp_off():
    subprocess.call(path + cmd[1],shell=True)

def hum_on():
    subprocess.call(path + cmd[2],shell=True)

def hum_off():
    subprocess.call(path + cmd[3],shell=True)

if __name__ == '__main__':
    temp_on()
    temp_off()
    hum_on()
    hum_off()
