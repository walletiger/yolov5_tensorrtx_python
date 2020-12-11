import cv2 
import TRTYolov5 as t

engine = t.create('../yolov5s.engine')

img = cv2.imread('/workspace/data/x3.jpg')

b = t.detect(engine, img, 0.45)

#t.destroy(engine)

print(b)

