#pragma once 

#ifdef __cplusplus
extern "C"
{
#endif 

void * yolov5_trt_create(const char * engine_name);

const char * yolov5_trt_detect(void *h, cv::Mat &img, float threshold);

void yolov5_trt_destroy(void *h);

#ifdef __cplusplus
}
#endif 
