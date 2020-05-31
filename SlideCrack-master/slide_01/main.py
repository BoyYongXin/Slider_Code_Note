# -*- coding: utf-8 -*-

import cv2

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

class SlideCrack(object):
    def __init__(self, gap, bg, out):
        """
        init code
        :param gap: 缺口图片
        :param bg: 背景图片
        :param out: 输出图片
        """
        self.gap = gap
        self.bg = bg
        self.out = out

    @staticmethod
    def clear_white(img):
        # 清除图片的空白区域，这里主要清除滑块的空白
        img = cv2.imread(img)
        rows, cols, channel = img.shape
        min_x = 255
        min_y = 255
        max_x = 0
        max_y = 0
        for x in range(1, rows):
            for y in range(1, cols):
                t = set(img[x, y])
                if len(t) >= 2:
                    if x <= min_x:
                        min_x = x
                    elif x >= max_x:
                        max_x = x

                    if y <= min_y:
                        min_y = y
                    elif y >= max_y:
                        max_y = y
        img1 = img[min_x:max_x, min_y: max_y]
        return img1

    def template_match(self, tpl, target):
        # shape[0] = 图像的高
        # shape[1] = 图像的宽
        # shape[2] = 图像的图像通道数量
        th, tw = tpl.shape[:2]
        result = cv2.matchTemplate(target, tpl, cv2.TM_CCOEFF_NORMED)

        # 寻找矩阵(一维数组当作向量,用Mat定义) 中最小值和最大值的位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        # 绘制矩形边框，将匹配区域标注出来
        # target：目标图像
        # tl：矩形定点
        # br：矩形的宽高
        # (0,0,255)：矩形边框颜色
        # 1：矩形边框大小
        cv2.rectangle(target, tl, br, (0, 0, 255), 2)
        cv2.imwrite(self.out, target)
        return tl[0]

    @staticmethod
    def image_edge_detection(img):
        """
        #边缘检测
        :param img:
        :return:
        """
        edges = cv2.Canny(img, 100, 200)
        return edges

    def discern(self):
        img1 = self.clear_white(self.gap)
        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        slide = self.image_edge_detection(img1)
        back = cv2.imread(self.bg, 0)
        back = self.image_edge_detection(back)

        slide_pic = cv2.cvtColor(slide, cv2.COLOR_GRAY2RGB) #输出三维数组
        back_pic = cv2.cvtColor(back, cv2.COLOR_GRAY2RGB)

        x = self.template_match(slide_pic, back_pic)
        # 输出横坐标, 即 滑块在图片上的位置
        print(x)

    def wacth_img(self, imgflip):
        """
        展示图片，以供查看
        :param imgflip:
        :return:
        """
        cv2.imshow('image', imgflip)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # 滑块图片
    image1 = "img/1_1.png"
    # 背景图片
    image2 = "img/1_2.png"

    # 处理结果图片,用红线标注
    image3 = "img/3_3.png"
    sc = SlideCrack(image1, image2, image3)
    sc.discern()
