# 程序功能鼠标按下，拖拽生成矩形框
# 缺陷：拖过的区域涂黑，而且不彻底--后期换写法测试
# 基本逻辑：鼠标按下松开，获取坐标，绘制矩形等------未看明白如何获取到的初始坐标和结束坐标，x,y从哪获取的值
# import numpy as np
# import cv2
#
# drawing = False  # 鼠标按下为真
# mode = True  # 如果为真，画矩形，按m切换为曲线
# ix, iy = -1, -1
# px, py = -1, -1
#
#
# def draw_circle(event, x, y, flags, param):
#     global ix, iy, drawing, px, py
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             cv2.rectangle(img, (ix, iy), (px, py), (0, 0, 0), 0)  # 将刚刚拖拽的矩形涂黑
#             cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0)
#             px, py = x, y
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 0)
#         px, py = -1, -1
#
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
#
# while (1):
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('q'):
#         break
#     elif k == 27:
#         break
# cv2.destroyAllWindows()

import numpy as np
import cv2
drawing = False #鼠标按下为真
mode = True #如果为真，画矩形，按m切换为曲线
ix,iy=-1,-1
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m') :
        mode = not mode
    elif k == ord('q'):
        break
    elif k == 27:
        break
cv2.destroyAllWindows()