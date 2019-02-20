import turtle

def drawTriangle(points, color, myTurtle):
    """
    """
    myTurtle.fillcolor(color)
    myTurtle.up()
    ## 第一個點（左下）
    myTurtle.goto(points[0][0], points[0][1])
    ## 顯示線
    myTurtle.down()
    ## 開始上色
    myTurtle.begin_fill()
    ## 第二個點（上）
    myTurtle.goto(points[1][0], points[1][1])
    ## 第三個點（右下）
    myTurtle.goto(points[2][0], points[2][1])
    ## 回到第一個點
    myTurtle.goto(points[0][0], points[0][1])
    ## 填滿顏色
    myTurtle.end_fill()

def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
def sierpinski(points, degree, myTurtle):
    """
    """
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        ## 以左下為基礎點
        ## 對上跟右取中段
        sierpinski(
            [
            ## 第一個點：左下
            points[0], 
            ## 第二個點：上
            getMid(points[0], points[1]), 
            ## 第三個點：右下
            getMid(points[0], points[2])
            ], 
            degree - 1, myTurtle
        ), 
        ## 以上為基礎點
        ## 對左下跟右下取中段
        sierpinski(
            [
            ## 第一個點：上
            points[1], 
            ## 第二個點：左下
            getMid(points[0], points[1]), 
            ## 第三個點：右下
            getMid(points[1], points[2])
            ], 
            degree - 1, myTurtle
        ), 
        ## 以右下為基礎點
        ## 對左跟上取中段
        sierpinski(
            [
            ## 第一個點：右下
            points[2], 
            ## 第二個點：上
            getMid(points[2], points[1]), 
            ## 第三個點：左下
            getMid(points[0], points[2])
            ], 
            degree - 1, myTurtle
        )

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()

if __name__ == "__main__":
    main()