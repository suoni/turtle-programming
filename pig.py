import turtle as t
t.screensize(400, 300, "#fff")
t.pensize(3)
t.colormode(255)                                    #设置GBK颜色范围为0-255
t.color((255,155,192),"pink")                       #设置画笔颜色和填充颜色(pink)
t.speed(10)
                            #绘制小猪佩奇的鼻子
t.penup()                                           #提笔
t.goto(-100,100)                                    #画笔前往坐标(-100,100)位置
t.pendown()                                         #落笔
t.seth(-30)                                         #笔的角度为-30°

t.begin_fill()              #外形填充的开始标志
a=0.4
for i in range(120):
   if 0<=i<30 or 60<=i<90:
       a=a+0.08
       t.left(3)                                      #向左转3度
       t.forward(a)                                   #向前走a的步长
   else:
       a=a-0.08
       t.left(3)
       t.forward(a)
t.end_fill()                #依据轮廓填充

t.penup()                                               #提笔
t.seth(90)                                              #笔的角度为90度
t.forward(25)                                           #向前移动25
t.seth(0)                                               #转换画笔的角度为0
t.forward(10)
t.pendown()                                             #落笔
t.pencolor(255,155,192)                                 #设置画笔颜色
t.seth(10)                                              #笔的角度为10°
                         #绘制小猪佩奇的一个鼻眼
t.begin_fill()
t.circle(5)                                             #画一个半径为5的圆
t.color(160,82,45)                                      #设置画笔和填充颜色
t.end_fill()

t.penup()                
t.seth(0)
t.forward(20)
t.pendown()
t.pencolor(255,155,192)
t.seth(10)
                       #绘制小猪佩奇的另一个鼻眼
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()

                      #绘制小猪佩奇的头
t.color((255, 155, 192), "pink")  #设置画笔颜色和填充颜色(pink)
t.penup()                         #提笔
t.seth(90)                        #笔的角度为90°
t.forward(41)                     #向前移动41
t.seth(0)                         #笔的角度为0°
t.forward(0)
t.pendown()                       #落笔
t.begin_fill()                    #外形填充的开始标志
t.seth(180)
t.circle(300, -30)                #利用circle()绘制小猪佩奇的头的外形
t.circle(100, -60)
t.circle(80, -100)
t.circle(150, -20)
t.circle(60, -95)
t.seth(161)
t.circle(-300, 15)
t.penup()
t.goto(-100, 100)
t.pendown()
t.seth(-30)
a = 0.4
for i in range(60):
    if 0 <= i < 30 or 60 <= i <90:
        a = a+0.08
        t.left(3)  # 向左转3度
        t.forward(a)  # 向前走a的步长
    else:
        a = a-0.08
        t.left(3)
        t.forward(a)
        t.end_fill()

       #绘制小猪佩奇的耳朵
t.color((255, 155, 192), "pink")
t.penup()
t.seth(90)
t.forward(-7)
t.seth(0)
t.forward(70)
t.pendown()
t.begin_fill()
t.seth(100)
t.circle(-50, 50)
t.circle(-10, 120)
t.circle(-50, 54)
t.end_fill()
t.penup()
t.seth(90)
t.forward(-12)
t.seth(0)
t.forward(30)
t.pendown()
t.begin_fill()
t.seth(100)
t.circle(-50, 50)
t.circle(-10, 120)
t.circle(-50, 56)
t.end_fill()

    #绘制小猪佩奇的眼睛
t.color((255, 155, 192), "white")
t.penup()
t.seth(90)
t.forward(-20)
t.seth(0)
t.forward(-95)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.penup()
t.seth(90)
t.forward(12)
t.seth(0)
t.forward(-3)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()
t.color((255, 155, 192), "white")
t.penup()
t.seth(90)
t.forward(-25)
t.seth(0)
t.forward(40)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()
t.color("black")
t.penup()
t.seth(90)
t.forward(12)
t.seth(0)
t.forward(-3)
t.pendown()
t.begin_fill()
t.circle(3)
t.end_fill()

#绘制小猪佩奇的腮
t.color((255, 155, 192))
t.penup()
t.seth(90)
t.forward(-95)
t.seth(0)
t.forward(65)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

#绘制小猪佩奇的嘴

t.color(239, 69, 19)
t.penup()              #抬笔
t.seth(90)             #笔的角度为90度
t.forward(15)          #向前移动15像素
t.seth(0)
t.forward(-100)
t.pendown()            #落笔
t.seth(-80)
t.circle(30, 40)
t.circle(40, 80)

#绘制小猪佩奇的身体

t.color("red", (255, 99, 71))
t.penup()              #抬笔
t.seth(90)             #笔的角度为90度
t.forward(-20)         #向前移动-20像素
t.seth(0)
t.forward(-78)
t.pendown()           #落笔
t.begin_fill()        #填充的开始标志
t.seth(-130)
t.circle(100,10)      #绘制圆弧
t.circle(300,30)
t.seth(0)
t.forward(230)       #向前移动230像素
t.seth(90)
t.circle(300,30)
t.circle(100,3)
t.color((255,155,192),(255,100,100))
t.seth(-135)
t.circle(-80,63)
t.circle(-150,24)
t.end_fill()         #填充的结束标志

#绘制小猪佩奇的手
t.color((255,155,192))
t.penup()              #抬笔
t.seth(90)             #笔的角度为90度
t.forward(-40)         #向前移动-40像素
t.seth(0)
t.forward(-27)
t.pendown()           #落笔
t.seth(-160)
t.circle(300,15)      #绘制圆弧
t.penup()              #抬笔
t.seth(90)
t.forward(15)
t.seth(0)
t.fd(0)
t.pendown()           #落笔
t.seth(-10)
t.circle(-20,90)
t.penup()              #抬笔
t.seth(90)
t.forward(30)
t.seth(0)
t.forward(237)
t.pendown()           #落笔
t.seth(-20)
t.circle(-300,15)
t.penup()              #抬笔
t.seth(90)
t.forward(20)
t.seth(0)
t.forward(0)
t.pendown()           #落笔
t.seth(-170)
t.circle(20,90)

#绘制小猪佩奇的脚
t.pensize(10)              #画笔大小为10
t.color((240,128,128))
t.penup()              #抬笔
t.seth(90)             #笔的角度为90度
t.forward(-75)
t.seth(0)
t.forward(-180)        #向前移动-180像素
t.pendown()           #落笔
t.seth(-90)           #笔的角度为-90度
t.forward(40)
t.seth(-180)
t.color("black")
t.pensize(15)         #画笔大小为15
t.forward(20)         #向前移动20像素
t.pensize(10)
t.color((240, 128, 128))
t.penup()              #抬笔
t.seth(90)
t.forward(40)
t.seth(0)
t.forward(90)         #向前移动90像素
t.pendown()           #落笔
t.seth(-90)           #笔的角度为-90度
t.forward(40)
t.seth(-180)          #笔的角度为-180度
t.color("black")
t.pensize(15)          #画笔大小为15
t.forward(20)

#绘制小猪佩奇的尾巴

t.pensize(4)             #画笔大小为4
t.color((255, 155, 192))
t.penup()                #抬笔
t.seth(90)               #笔的角度为90度
t.forward(70)            #向前移动70像素
t.seth(0)
t.forward(95)            #向前移动95像素
t.pendown()             #落笔
t.seth(0)
t.circle(70, 20)        #绘制圆弧
t.circle(10, 330)
t.circle(70, 30)
t.done()                #关闭turtle



