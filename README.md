#1  download tensorrtx 
git clone https://github.com/wang-xinyu/tensorrtx 
git reset --hard 4089c64

#2 convert your  "yolov5s.pt" to yolov5s.wts  ( yolov5 3.0, yolov5 3.1 )
cp tensorrtrtx/gen_wts.py  yolov5-3.1/
cd yolov5-3.1 && python3 gen_wts.py  # output : yolov5s.wts 
# 3 patch tensorrtx 
cp -a  CMakeList.txt python yolov5_lib.cpp yolov5_lib.h tensorrtx/

# 4 build tesorrtx 
# 4.1 modify your net model  INPUT_W , INPUT_H , class_num in yolo_layer.h 
# 4.2 and then 
cd tesorrtx && mkdir build && cd build && cmake ../ && make 

#5 convert wts to tensorRT 
cp yolov5s.wts tesorrtx/
cd tesorrtx/build  && yolov5 -s  # this will generate yolov5s.engine 
# 6 test 
yolov5 -d img_path 
#7 build python nodules 
cd tesorrtx/python && python3 setup.py install 
# 8 test python modules 
export LD_LIBRAR_PATH=$PWD/../build  # path for libyolov5_trt.so
./python3 test.py 



