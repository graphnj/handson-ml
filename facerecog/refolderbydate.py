# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:43:13 2018

@author: zhujinhua
"""

#coding: gbk

import shutil
import os
import stat
import time
##图像的exif,百度知道:http://baike.baidu.com/view/22006.htm
import exifread as exif

def getDate(filename):
    try:
        fd = open(filename, 'rb')
    except:
        raise "unopen file[%s]\\n" % filename 
    data = exif.process_file( fd )
    if data:
        #获取图像的 拍摄日期
        try:
            t = data['EXIF DateTimeOriginal']
            #转换成 yyyy-mm-dd 的格式
            return str(t).replace(":","-").replace(" ","-")[:20]+'S'
        except:
            pass
    #如果没有取得 exif ，则用图像的创建日期，作为拍摄日期
    state = os.stat(filename)
    return time.strftime("%Y-%m-%d", time.localtime(state[-2]))+'C'

def showFileProperties(path):
    '''显示文件的属性。包括路径、大小、创建日期、最后修改时间，最后访问时间'''
    import time,os
    #遍历目录下的所有文件
    for root,dirs,files in os.walk(path,True):
        dirs[:] = []
        print("位置：" + root)
        
        for filename in files:
            fullfilename = os.path.join(root, filename)
            #如果文件名是 'jpg','png' 就处理，否则不处理
            f,e = os.path.splitext(filename)
            if e.lower() not in ('.jpg','.png','JPG'):
                continue
            info = "文件名: " + filename + " "
            #文件的拍摄日期
            t = getDate( fullfilename )
            info = info + "拍摄时间：" + t + " "
            pwd = 'v:\\zhujingyidate' +'\\\\'+ t[0:7]
            dst = pwd + '\\\\' + t+e.lower()
            #按照图片的拍摄日期创建目录，把每个图片放到相应的目录中去
            if not os.path.exists(pwd ):
                os.mkdir(pwd)
                print('info:'+info, 'dst:'+dst)
            
            #用 copy2 会保留图片的原始属性
            shutil.copy2( fullfilename, dst )
            #os.remove( filename )

if __name__ == "__main__":
    path = "V:\\静宜整理\\20180603"
    paths=["V:/静宜整理/20130811/", "V:/静宜整理/20140101/", "V:/静宜整理/20140319/", "V:/静宜整理/20140330/", "V:/静宜整理/20140601/", "V:/静宜整理/20140627毕业/", "V:/静宜整理/20141004/", "V:/静宜整理/2017仲秋", "V:/静宜整理/20170318/", "V:/静宜整理/20170318Video/", "V:/静宜整理/20170326/", "V:/静宜整理/20170401/", "V:/静宜整理/20170618Camera/", "V:/静宜整理/201708/", "V:/静宜整理/20171001/", "V:/静宜整理/20171029/", "V:/静宜整理/20180101/", "V:/静宜整理/201805/", "V:/静宜整理/20180603/", "V:/静宜整理/galaxy/", "V:/静宜整理/galaxy2013-2014/", "V:/静宜整理/train/", "V:/静宜整理/WeiXin/", "V:/静宜整理/静静/", "V:/静宜整理/九叶网/", "V:/静宜整理/朱静宜/", "V:/静宜整理/"]
    for path in paths:
        showFileProperties(path)