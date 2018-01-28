import time
import json

def start():
    start_time = time.time()
    print(start_time)
    data = {
    "start_time":start_time
    }
    file = open("time.json", "w")
    json.dump(data, file)

def stop():
    stop_time = time.time()
    file = open("time.json", "r")
    json_dict = json.load(file)
    start_time = json_dict["start_time"]
    result = stop_time - start_time
    if(result>3600):
        h = int(result/3600)
        m = int((result-h)/600)
        study_time = (str(h) + "時間",str(m) + "分")
        print(study_time)
        return study_time
    elif(result<3600):
        m= int(result/600)
        study_time = str(m) + "分"
        print(str(m) + "分")
        return study_time

if __name__ == '__main__':
    main()
