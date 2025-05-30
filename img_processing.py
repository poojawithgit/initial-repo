#image processing
#code of red,green,blue=255,255,255
#opencv===stands for computer vision 
#cv2.waitKey(0) #we are passing zero bcoz 0 miles sec mai check hote rehga ki keyboard se koi key press  toh n hori hai

import cv2
import cv2.data
modelPath=cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
trainedMachine=cv2.CascadeClassifier(modelPath)
image=cv2.imread("imgpro.jpg")
faces=trainedMachine.detectMultiScale(image)
for face in faces:
    x,y,w,h=face
    image=cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Image Detection",image) 
    cv2.waitKey(0)
