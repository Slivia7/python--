
from tkinter import *
from tkinter.filedialog import *
from PIL import Image
import tkinter.messagebox as messagebox
from 图片隐写 import encodeDataInImage, decodeImage

# 美化：https://zmister.com/archives/477.html?tdsourcetag=s_pctim_aiomsg



def Encryption():
    '''加密程序'''
    root1 = Tk()
    root1.title("加密")

    def show1():
        data = e1.get()
        url1 = e2.get()
        url2 = e3.get()
        try:
            image = Image.open(url1)
        except:
            messagebox.showinfo("注意", '无法打开图片')
        try:
            encodeDataInImage(image, data).save(url2)
            messagebox.showinfo('', "加密成功")
            root1.destroy()
        except:
            messagebox.showinfo('注意', "加密失败")
            pass

    def filefound(entry):
        filepath = askopenfilenames()
        filepath = str(filepath)[2:-3]
        # print(filepath)
        entry.delete(0, END)  # 将输入框里面的内容清空
        entry.insert(0, filepath)    #输入框内显示路径

    Label(root1, text='要传输的内容 :').grid(row=0, column=0)  # 对Label内容进行 表格式 布局
    Label(root1, text='原图片图片地址 :').grid(row=1, column=0)
    Label(root1, text='加密后图片保存至 :').grid(row=2, column=0)

    v1 = StringVar()  #加密内容
    v2 = StringVar()  #原图片地址
    v3 = StringVar()  #加密后的图片地址

    e1 = Entry(root1, textvariable=v1)  # 用于储存 输入的内容
    e2 = Entry(root1, textvariable=v2)
    e3 = Entry(root1, textvariable=v3)
    e1.grid(row=0, column=1, padx=10, pady=5)  # 进行表格式布局 .
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    Button(root1, text='加密', width=10, command=show1).grid(row=3, column=0, sticky=W, padx=10,pady=5)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 .
    Button(root1, text="浏览", command=lambda :filefound(e2)).grid(row=1, column=3)#选择原图片地址
    Button(root1, text="浏览", command=lambda :filefound(e3)).grid(row=2, column=3)#选择保存位置地址，使用此按钮只能实现另存为功能，要新建文件需手动输入
    Button(root1, text='退出', width=10, command=root1.destroy).grid(row=3, column=1, sticky=E, padx=10, pady=5)


def Decrypt():
    '''解密程序'''
    root2 = Tk()
    root2.title("解密")

    def show2():
        url = e.get()
        print(url)
        try:
            image = Image.open(url)
        except:
            messagebox.showinfo("注意", '无法打开图片')
        try:
            data = decodeImage(image)
            messagebox.showinfo("解密成功", data)
            root2.destroy()
        except:
            messagebox.showinfo("解密失败")

    def filefound(entry):
        filepath = askopenfilenames()
        filepath = str(filepath)[2:-3]
        # print(filepath)
        entry.delete(0, END)  # 将输入框里面的内容清空
        entry.insert(0, filepath)    #输入框内显示路径

    Label(root2, text='图片地址 :').grid(row=0, column=0)  # 对Label内容进行 表格式 布局
    filepath = StringVar()  # 图片路径
    e = Entry(root2, textvariable=filepath)  # 用于储存 输入的内容
    e.grid(row=0, column=1, padx=10, pady=5)  # 进行表格式布局 .
    Button(root2, text="浏览", command=lambda :filefound(e)).grid(row=0, column=3)
    Button(root2, text='解密', width=10, command=show2).grid(row=3, column=0, sticky=W, padx=10, pady=5)
    Button(root2, text='退出', width=10, command=root2.destroy).grid(row=3, column=1, sticky=E, padx=10, pady=5)

def main():
    root = Tk()
    root.title("图片隐写")
    Button(root, text='加密信息', width=10, command=Encryption).grid(row=3, column=0, sticky=W, padx=10,pady=5)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 .
    Button(root, text='解密信息', width=10, command=Decrypt).grid(row=3, column=1, sticky=W, padx=10, pady=5)
    Button(root, text='退出', width=10, command=root.destroy).grid(row=3, column=2, sticky=E, padx=10, pady=5)
    mainloop()

##if __name__ == '__main__':
##    main()
