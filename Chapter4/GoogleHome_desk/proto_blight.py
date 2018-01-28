import json

def blight_result():
    file = open("blight.json", "r")
    json_dict = json.load(file)
    result = json_dict["blight_lux"]
    return result

if __name__ == '__main__':
    blight_result()
