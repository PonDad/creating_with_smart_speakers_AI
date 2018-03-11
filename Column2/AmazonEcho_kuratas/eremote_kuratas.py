import subprocess

path = "python3 rm2_controller/BlackBeanControl.py -c "

cmd = ["fire","right","left","reload"]

def fire():
    subprocess.call(path + cmd[0],shell=True)

def right():
    subprocess.call(path + cmd[1],shell=True)

def left():
    subprocess.call(path + cmd[2],shell=True)

def filling():
    subprocess.call(path + cmd[3],shell=True)

if __name__ == '__main__':
    fire()
    right()
    left()
    filling()
