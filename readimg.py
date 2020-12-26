import matplotlib.image as mpimg
from PIL import Image
import math
import os
import operator
from functools import reduce
import win32gui,win32ui,win32api
from ctypes import windll
import win32con
import numpy as np
import time
import cv2
import pyautogui
from numpy.linalg import *
LEFT = 65
DOWN = 83
UP = 87
RIGHT = 68
x=[400,520]
y=[255,375,495,615]
def press(key):
    MapKey = windll.user32.MapVirtualKeyA
    win32api.keybd_event(key, MapKey(key, 0), 0, 0)
    time.sleep(0.02)
    win32api.keybd_event(key, MapKey(key, 0), win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.02)    
def pressn(n):
    if n <=4 :
        n-=1
        for i in range(0,n):
            press(DOWN)
        press(13)
        for i in range(0,n):
            press(UP)
    if n > 4 :
        n=n-5
        press(RIGHT)
        for i in range(0,n):
            press(DOWN)
        press(13)
        for i in range(0,n):
            press(UP)
        press(LEFT)
    if n==8 or sn==4 : press(9)
def imggrey(image1,image2):
    n = 0 
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE) 
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE) 
    height, width = img1.shape 
    for line in range(height): 
        for pixel in range(width): 
            if img1[line][pixel] != img2[line][pixel]: 
                n = n + 1
    return n
def imgdiff(image1,image2):
    nofz=0
    img1=cv2.imread(image1)
    img2=cv2.imread(image2)
    diff=cv2.subtract(img1,img2)
    for i in diff:
        for j in i:
            for k in j:
                if k!=0 :
                    if(nofz>=130001):break
                    nofz+=k
    return nofz
while True:
    hWnd = win32gui.FindWindow("grcWindow","Grand Theft Auto V")
    left,top,right,bot = win32gui.GetWindowRect(hWnd)
    width = right - left
    height = bot - top
    #返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hWnd)
    #创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    #创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    #创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    #为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    #将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    #保存bitmap到内存设备描述表
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)

    #如果要截图到打印设备：
    ###最后一个int参数：0-保存整个窗口，1-只保存客户区。如果PrintWindow成功函数返回值为1
    #result = windll.user32.PrintWindow(hWnd,saveDC.GetSafeHdc(),0)
    #print(result) #PrintWindow成功则输出1

    #保存图像
    ##方法一：windows api保存
    ###保存bitmap到文件
    saveBitMap.SaveBitmapFile(saveDC,"img_Winapi.bmp")

    #下面开始解析图片
    mat= mpimg.imread('img_Winapi.bmp')
    fp_mat=mat[156:595,783:1143]
    mpimg.imsave('test.jpg',fp_mat)
    pn=0
    sn=0
    skey=[]
    if(imggrey('test.jpg','fp1.jpg')<140000):
        for i in x:
            for j in y:
                if(sn==4):continue
                if(sn==3 and pn==7):
                    pressn(8)
                    continue
                pn+=1
                part=mat[j:j+95,i:i+95]
                mpimg.imsave('cache/part_'+str(pn)+'.jpg',part)
                for k in os.listdir(r'part1/'):
                    if(imgdiff('cache/part_'+str(pn)+'.jpg','part1/'+k)<130000):
                        #print(str(pn)+str(imgdiff('cache/part_'+str(pn)+'.jpg','part1/'+k)))
                        pressn(pn)
                        sn+=1
        press(9)
                
    if(imggrey('test.jpg','fp2.jpg')<140000):
        for i in x:
            for j in y:
                if(sn==4):continue
                if(sn==3 and pn==7):
                    pressn(8)
                    continue
                pn+=1
                part=mat[j:j+95,i:i+95]
                mpimg.imsave('cache/part_'+str(pn)+'.jpg',part)
                for k in os.listdir(r'part2/'):
                    if(imgdiff('cache/part_'+str(pn)+'.jpg','part2/'+k)<130000):
                        #print(str(pn)+str(imgdiff('cache/part_'+str(pn)+'.jpg','part2/'+k)))
                        pressn(pn)
                        sn+=1
        press(9)

    if(imggrey('test.jpg','fp3.jpg')<140000):
        for i in x:
            for j in y:
                if(sn==4):continue
                if(sn==3 and pn==7):
                    pressn(8)
                    continue
                pn+=1
                part=mat[j:j+95,i:i+95]
                mpimg.imsave('cache/part_'+str(pn)+'.jpg',part)
                for k in os.listdir(r'part3/'):
                    if(imgdiff('cache/part_'+str(pn)+'.jpg','part3/'+k)<130000):
                        #print(str(pn)+str(imgdiff('cache/part_'+str(pn)+'.jpg','part3/'+k)))
                        pressn(pn)
                        sn+=1
        press(9)
                        
    if(imggrey('test.jpg','fp4.jpg')<140000):
        for i in x:
            for j in y:
                if(sn==4):continue
                if(sn==3 and pn==7):
                    pressn(8)
                    continue
                pn+=1
                part=mat[j:j+95,i:i+95]
                mpimg.imsave('cache/part_'+str(pn)+'.jpg',part)
                for k in os.listdir(r'part4/'):
                    if(imgdiff('cache/part_'+str(pn)+'.jpg','part4/'+k)<130000):
                        #print(str(pn)+str(imgdiff('cache/part_'+str(pn)+'.jpg','part4/'+k)))
                        pressn(pn)
                        sn+=1
        press(9)

