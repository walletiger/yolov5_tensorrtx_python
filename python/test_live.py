#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys

#sys.path.append('/workspace/hugo_py')

import cv2
import numpy as np
import time
from camera import JetCamera
import traceback
import TRTYolov5 as fd

cap_w = 640
cap_h = 360
cap_fps = 30


def main():
    cam = JetCamera(cap_w, cap_h, cap_fps)

    engine = fd.create('../build/yolov5s.engine')


    out_win = "foo"
    cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    cam.open()

    cnt = 0
    sum_time = 0
    while True:
        try:
            ret, frame = cam.read()
            #print("camera read one frame ")
            if not ret:
                break

            t0 = time.time()
            ret = fd.detect(engine, frame, 0.4)
            res = eval(ret)
            t1 = time.time()

            sum_time += t1 - t0
            cnt += 1

            if cnt % 150 == 0:
                print("frame cnt [%d] retina face  detect delay = %.1fms" % (cnt, (sum_time) * 1000/ cnt ))
                sum_time = 0
                cnt = 0 

            print(res)
            if   res['num_det'] > 0:
                for ret in res['objects']:
                    cls_id, x1, y1, x2, y2 = ret 

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0 , 255 ))

            #    r = ret[2]
            #    #print("ret = %s, %s" % (ret, r))
            #    #cv2.rectangle(frame, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255, 255, 0))

            cv2.imshow(out_win, frame)
            cv2.waitKey(1)
        except:
            traceback.print_exc()
            break

    cam.close()


if __name__ == '__main__':
    main()


