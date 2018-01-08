import os
import cv2

input_folder = "input_mika"
output_folder = "mika"
#input_folder = "input_rika"
#output_folder = "rika"
cascade_path = "./trained_models/haarcascade_frontalface_alt2.xml"

files = os.listdir("./" + input_folder + "/")

for i in range(0, len(files)):
    print (files[i])
    root, extension = os.path.splitext(files[i])
    if files[i] == ".DS_Store":
        print("This is no image.")
    elif extension == ".png" or ".jpeg" or ".jpg":
        portrait = "./" + input_folder + "/" + files[i]
        cv_image = cv2.imread(portrait)
        gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)

        facerect = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=2, minSize=(150, 150))

        if len(facerect) > 0:
            for rect in facerect:
                x, y, w, h = rect[0], rect[1], rect[2], rect[3]
                dst = cv_image[y:y + h, x:x + w]
            dst = cv2.resize(dst, (150, 150))
            cv2.imwrite("./" + output_folder + "/" + output_folder + "_" + str(i + 1) + ".jpg", dst)
            print("crop done > " + output_folder + "_" + str(i + 1) + ".jpg")

        else:
            print("can't crop")
