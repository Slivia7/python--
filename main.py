import tkinter as tk
import tkinter.messagebox
import pickle  #引用Tk模块
from UI import main 
from PIL import Image,ImageTk
from Info import user
from Info import Message
from Info import Service
from time import *
from Spider import PGet
#新建图片查看界面[必须在按钮之前设定]

        
def mainRun(user):
        ##run()
        #窗口
    window=tk.Tk()
    window.title('欢迎进入图像信息系统')
    window.geometry('550x300')
    #画布放置图片
    canvas=tk.Canvas(window,height=300,width=550)
    imagefile=tk.PhotoImage(file='images/bg2.png')
    image=canvas.create_image(0,0,anchor='nw',image=imagefile)
    canvas.pack(side='top')
    def imageLook():
        imageWindow=tk.Toplevel(window)
        imageWindow.geometry('600x500')
        imageWindow.title('图片查看')
        rmegs=user.received
        smegs=user.send
##        s=tk.Label(imageWindow, text='发送的信息', bg='yellow', font=('Arial', 12), width=30, height=2)
##        s.pack()
##        for meg in smegs:
##            tk.Label(imageWindow, text="发送给"+meg.getUserTo(),font=('Arial', 12), width=10).pack()
##            img_open = Image.open(meg.getImage())
##            img_png = ImageTk.PhotoImage(img_open)
##            label_img = tk.Label(imageWindow, image = img_png)
##            label_img.pack()
        r=tk.Label(imageWindow, text='收到的信息', bg='blue', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
# 第5步，放置标签
        r.pack()
        for meg in rmegs:
            tk.Label(imageWindow, text="来自"+meg.getUserFrom(),font=('Arial', 12), width=10).pack()
            img_open = Image.open(meg.getImage())
            img_png = ImageTk.PhotoImage(img_open)
            label_img = tk.Label(imageWindow,image = img_png)
            label_img.pack()
        tk.Button(imageWindow,text='删除已读信息',command=user.removeReceivedAll()).place(x=200,y=450)
        tk.Button(imageWindow,text='删除已发送信息',command=user.removeSendAll()).place(x=300,y=450)
        tk.Button(imageWindow,text='退出',width=10,command=imageWindow.destroy).place(x=420,y=450)
        imageWindow.mainloop()
    def sendMessage():
        messageW=tk.Toplevel(window)
        messageW.geometry('500x500')
        messageW.title('信息发送')
        #标签 接收方
        tk.Label(messageW,text='接收者:').place(x=100,y=150)
        tk.Label(messageW,text='图片:').place(x=100,y=190)
        #用户名输入框
        var_usr_name=tk.StringVar()
        entry_usr_name=tk.Entry(messageW,textvariable=var_usr_name)
        entry_usr_name.place(x=160,y=150)
        print(var_usr_name.get())
        #图片输入框
        var_img_name=tk.StringVar()
        entry_usr_img=tk.Entry(messageW,textvariable=var_img_name)
        entry_usr_img.place(x=160,y=190)
        def send():
            m=Message(var_img_name.get(),user.getName(),var_usr_name.get())
            print("消息图片"+m.getUserTo())
            s=Service(m)
            re=s.service()
            tk.messagebox.showinfo(re)
        sure=tk.Button(messageW,text='发送',command=send)
        sure.place(x=210,y=230)
        messageW.mainloop()
    def getImage():
##        tk.messagebox.showerror("hh")
        PGet()
    bt1=tk.Button(window,text='图片处理',command=main)
    bt1.place(x=140,y=230)
    bt2=tk.Button(window,text='信息查看',command=imageLook)
    bt2.place(x=210,y=230)
    bt3=tk.Button(window,text='信息发送',command=sendMessage)
    bt3.place(x=280,y=230)
    bt4=tk.Button(window,text='获取图片',command=getImage)
    bt4.place(x=350,y=230)
    bt5=tk.Button(window,text='退出',command=window.destroy)
    bt5.place(x=420,y=230)
    window.mainloop()

#测试
##try:
##   with open('usr_info.pickle','rb') as usr_file:
##        usrs_info=pickle.load(usr_file)
##        usr_file.close()
##except FileNotFoundError:
##    print("服务器异常！")
##u=usrs_info["小明"]
##mainRun(u)
