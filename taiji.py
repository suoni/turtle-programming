import turtle
R = 150                                #太极图半径
turtle.screensize(400, 300, "yellow")
turtle.pensize(3)
turtle.pencolor('black')
turtle.speed(1)
TJT_color = {1: 'white', -1: 'black'}  # 太极图填充色 1 白色 -1 黑色
color_list = [1, -1]
#先画半边，再画另一边
for c in color_list:
    turtle.fillcolor(TJT_color.get(c))
    turtle.begin_fill()
    #开始画出半边的轮廓
    turtle.circle(R / 2, 180)
    turtle.circle(R, 180)
    turtle.circle(R / 2, -180)
    turtle.end_fill()
                                #绘制该半边的鱼眼
    turtle.penup()
    turtle.goto(0, R / 3 * c)   #移动到该半边的鱼眼的圆上 R/3*c 表示移动到哪边
    turtle.pendown()
    turtle.fillcolor(TJT_color.get(-c))  #获取鱼眼填充色, 与该半边相反
    turtle.begin_fill()
    turtle.circle(-R / 6, 360)
    turtle.end_fill()
                             #回到原点，为下一循环的开始做准备
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
turtle.done()
