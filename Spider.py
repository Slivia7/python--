import queue
import re
import threading

import requests
from urllib import error
from bs4 import BeautifulSoup
import os
from tkinter import *
import easygui
import _thread
import time
import tkinter as tk
from PIL import ImageTk, Image

class search(object):
 def __init__(self,):
     self.num = 0
     self.numPicture = 0
     self.List = []
     self.file = ''
     self.urls = []
     self.q = queue.Queue()
     self.Recommend=''


 def Find(self,url):
    print('正在检测图片总数，请稍等.....')
    t = 0
    i = 1
    s = 0
    while t < 100:
        Url = url + str(t)
        try:
            Result = requests.get(Url, timeout=7) #超时设置-136
        except BaseException:
            t = t + 60 #向后滑动60个图-一页60个图
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url-147
            s += len(pic_url)
            # print(s)
            if len(pic_url) == 0:
                break
            else:
                self.List.append(pic_url)
                t = t + 60


    print(s)
    return s


 def recommend(self,url):
    Re = []
    try:
        html = requests.get(url)
    except error.HTTPError as e:
        return
    else:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text,'html.parser')
        # print(bsObj)
        div = bsObj.find('div', id='topRS') #定位
        if div is not None:
            listA = div.findAll('a')#定位a标签
            for i in listA:
                if i is not None:
                    Re.append(i.get_text())#取出标签内的推荐标题放入列表中
        return Re


 def dowmloadPicture(self,html, keyword):

    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    # print(pic_url)
    print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
    for each in pic_url:
        # print('正在下载第' + str(self.num + 1) + '张图片')
        self.q.put(each)
    start = time.time()
    while True:
      for i in range(self.numPicture):
        print('正在下载第' + str(self.num + 1) + '张图片')
        try:
            url = self.q.get_nowait()  # 不阻塞的读取队列数据
            # i = self.q.qsize()
        except Exception as e:
            print(e)
            break

        # if each is not None:

        pic = requests.get(url, timeout=7)



        # except BaseException:
        #     easygui.msgbox('错误，当前图片无法下载')
        #     continue
        # else:
        if pic.status_code == 200:
            string = self.file + r'\\' +  str(self.num) + '.png'
            fp = open(string, 'wb')
            fp.write(pic.content)#-125-content是二进制形式（text打印的是str形式）
            fp.close()
            self.num += 1

      if self.num >= self.numPicture: #控制下载的图片数
            return
 def mainn(self,word1,fs,name):

        word = word1
        # add = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%BC%A0%E5%A4%A9%E7%88%B1&pn=120'
        urls = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
        tot = self.Find(urls)
        self.Recommend = self.recommend(urls)  # 记录相关推荐
        print('经过检测%s类图片共有%d张' % (word, tot))
        self.numPicture = fs
        self.file = name
        y = os.path.exists(self.file)
        if y == 1:
            easygui.msgbox('该文件已存在，请重新输入')
            self.file=name
            os.mkdir(self.file)
        else:
            os.mkdir(self.file)
        m = 0
        tmp = urls
        while m < self.numPicture:
            try:
                urls = tmp + str(m)
                result = requests.get(urls, timeout=10)  # 超时设置
                # print(url)
            except error.HTTPError as e:
                print('网络错误，请调整网络后重试')
                m = m + 60
            else:
                num = 10  # 线程数
                threads = []
                for i in range(num):
                    t = threading.Thread(target=self.dowmloadPicture, args=(result.text, word), name="child_thread_%s" % i)
                    threads.append(t)
                for t in threads:
                    t.start()
                for t in threads:
                    t.join()

                # self.dowmloadPicture(result.text, word)
                m = m + 60

        easygui.msgbox('下载完成！')



 def intere(self):
     root = tk.Toplevel()
     canvas = tk.Canvas(root, width=730, height=400, bd=0, highlightthickness=0)

     photo = tk.PhotoImage(file='images/time.gif')

     canvas.create_image(350, 190, image=photo)

     canvas.pack()
     r1 = tk.Label(root, text='请输入搜索关键词', font=("华文行楷", 20), fg='black').place(x=50, y=20)
     v1 = tk.StringVar()
     e1 = tk.Entry(root, textvariable=v1, width=30).place(x=400, y=30)

     r2 = tk.Label(root, text='请输入想要下载的图片数量', font=("华文行楷", 20), fg='black').place(x=10, y=70)
     v2 = tk.StringVar()
     e2 = tk.Entry(root, textvariable=v2, width=30).place(x=400, y=70)

     r3 = tk.Label(root, text='请输入文件夹名', font=("华文行楷", 20), fg='black').place(x=70, y=120)
     v3 = tk.StringVar()
     e3 = tk.Entry(root, textvariable=v3, width=30).place(x=400, y=130)

     r4 = tk.Label(root, text='猜你喜欢', font=("华文行楷", 20), fg='black', ).place(x=100, y=200)
     var = tk.StringVar()
     r5=tk.Label(root, textvariable=var, bg='white', fg='black', font=('Arial', 12), width=30, height=5).place(x=400,y=170)


     def prefer():
             print('猜你喜欢')
             for re in self.Recommend:
              var.set(re)

     tk.Button(root, text='开始下载', width=20, command=lambda: self.mainn(v1.get(), int(v2.get()), v3.get())).place(x=20,y=330)
     tk.Button(root,text='查看相关',width=10,command=prefer).place(x=300,y=330)
         # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 .
     tk.Button(root, text='退出', width=10, command=root.destroy).place(x=580,y=330)

     mainloop()

def PGet():  # 主函数入口
    rs=search()
    rs.intere()

