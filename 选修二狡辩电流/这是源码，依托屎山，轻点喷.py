import tkinter as tk
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import messagebox as mbx
import turtle as t
import math as m
#坚持用turtle库手搓函数图像awa


Aog = tk.Tk()
Aog.title("物理玩具-狡辩电流")
Aog.geometry("500x500")


#父窗口页面UwU
label = tk.Label(Aog, 
                 text=" turtle交流电画图                          ",  #觉得淡蓝色块突出一点很有设计感
                 bg="lightblue",                                     #淡蓝色是真好看
                 font=("微软雅黑", 18))
label.pack(anchor="nw",pady=0.5,padx=0.5)
label1 = tk.Label(Aog,
                  text="  画图用matplotlib库真的太逊了,老艺术家还得用Turtle~",
                  font=("微软雅黑", 10))
label1.pack(anchor="nw",pady=0.5,padx=0.5)
#懒得麻烦就当空行使了
label1 = tk.Label(Aog,
                  text="  ",
                  font=("微软雅黑", 10))
label1.pack(anchor="nw",pady=0.5,padx=0.5)


#=========功能=========


#画坐标轴
def drawr():
    #准备工作（坐标轴）
    t.penup()
    t.goto(-500,0)
    t.pendown()
    t.goto(500,0)
    t.penup()
    t.goto(0,-500)
    t.pendown()
    t.goto(0,500)
    t.penup()
    t.goto(0,0)
    mbx.showinfo("AwA", "物理小玩具-交流电V1.0 By Aog \n   登录www.xwhouse.asia了解更多")


#获取交流电的数值~
label3 = tk.Label(Aog, text="omega / 匝数 / 磁通量 / 线圈面积:")
label3.pack(pady=5)

entry_freq = tk.Entry(Aog,width=20) #频率输入框
entry_freq.pack(pady=5)

entry_turn = tk.Entry(Aog, width=20) #匝数输入框
entry_turn.pack(pady=5)

entry_citongl = tk.Entry(Aog, width=20) #磁通量输入框
entry_citongl.pack(pady=5)

entry_square = tk.Entry(Aog, width=20) #线圈面积输入框
entry_square.pack(pady=5)

#处理输入框的数值
def get_number():
    #不知道交流电英语怎么说qwq
    global a,b,c,d#a=omega b=匝数 c=磁通量 d=线圈面积

    qwq = entry_freq.get()
    awa = entry_turn.get()
    zwz = entry_citongl.get()
    owo = entry_square.get()


    #判断omega写没写 
    if qwq:
        a=int(qwq)    
        mbx.showinfo("OK没毛病", f"omega = {a}")
        print(a)
    else:
        mbx.showwarning("不是哥们", "你至少得给我omega吧！")
        return  # 缺少参数就返回

    #判断匝数写没写
    if awa:
            b=int(awa)    
            mbx.showinfo("OK没毛病", f"匝数 = {b}")
            print(b)
    else:
        mbx.showwarning("不是哥们", "你至少得给我匝数吧！")
        return  # 缺少参数就返回

    #判断磁通量写没写
    if zwz:
        c=int(zwz)    
        mbx.showinfo("OK没毛病", f"磁通量 = {c}")
        print(c)
    else:
        mbx.showwarning("不是哥们", "你至少得给我磁通量吧！")
        return  # 缺少参数就返回
    
    #判断线圈面积写没写
    if owo:
        d=int(owo)    
        mbx.showinfo("OK没毛病", f"线圈面积 = {d}")
        print(d)
    else:
        mbx.showwarning("不是哥们", "你至少得给我线圈面积吧！")
        return  # 缺少参数就返回

    # 所有参数都获取成功后才画图
    draw_graph()

def draw_graph():
    # 画图函数
    global a, b, c, d
    scale = 50  # 缩放系数
    
    # 清空之前的画布
    t.clear()
    
    # 重新画坐标轴
    drawr()
    
    # 设置画笔
    t.penup()
    t.pensize(2)
    t.pencolor("red")
    
    # 画交流电波形
    for x in range(-400, 401, 5): 
        # 计算y值：e = N * B * S * omega * sin(omega * t)
        # 但你的公式好像写错了，应该是 N * B * S * omega * sin(omega * t)
        rad = a * x / 100  # t 用 x 代替，除以100让频率慢一点
        # 修正公式：应该是 b * c * d * a * m.sin(rad)
        y = b * c * d * a * m.sin(rad) * scale / 10000
        
        t.goto(x, y)
        t.pendown()
    
    t.penup()
    mbx.showinfo("完成", "画图完成！")

btn3 = tk.Button(Aog, 
                text="开始画图", 
                command=get_number)
btn3.pack(pady=10)


#懒得麻烦就当空行使了
label1 = tk.Label(Aog,
                  text="  ",
                  font=("微软雅黑", 10))
label1.pack(anchor="nw",pady=0.5,padx=0.5)


btn=tk.Button(Aog,text="需要坐标轴就点我awa",command=drawr)
btn.pack(anchor="nw",pady=5,padx=10)
Aog.mainloop()

#e=NBSomega*sinomegat
#e=I^2R