# -*- coding: utf-8 -*-
# @Author: Mr.Yang
# @Date: 2020/5/28 pm 2:37

"""
cv2 库基本操作学习记录
参考链接 ： https://blog.csdn.net/RNG_uzi_/article/details/90034485
"""
import cv2

# 读取灰度图片
img = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)

# # 显示图片
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #dv2.destroyWindow(wname)

# # 保存图像
# # cv2.imwrite('1.png', img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
# cv2.imwrite('1.png',img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

# # 翻转图像
# flipcode = 0：沿x轴翻转
# flipcode > 0：沿y轴翻转
# flipcode < 0：x,y轴同时翻转
# imgflip = cv2.flip(img, 1)
# cv2.imshow('image', imgflip)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 复制图像
# imgcopy = img.copy()

# # 颜色空间转换

# 彩色图像转为灰度图像
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# 灰度图像转为彩色图像
img3 = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# cv2.COLOR_X2Y，其中X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS


"""
matchTemplate():
参数image:待搜索的图像(大图)
参数temple:搜索模板,需要和原图一样的数据类型且尺寸不能大于源图像
参数result:比较结果的映射图像,其必须为单通道,32位浮点型图像,如果原图(待搜索图像)尺寸为W*H,而temple尺寸为w*h,则result尺寸一定是
    (W-w+1)*(H-h+1)
参数method:指定匹配方法,有如下几种:
    CV_TM_SQDIFF:平方差匹配法
    CV_TM_SQDIFF_NORMED:归一化平方差匹配法
    CV_TM_CCORR:相关匹配法
    CV_TM_CCORR_NORMED:归一化相关匹配法
    CV_TM_CCOEFF:系数匹配法
    CV_TM_CCOEFF_NORMED:化相关系数匹配法
"""
"""
minMaxLoc()函数
作用:一维数组当作向量,寻找矩阵中最小值和最大值位置
"""