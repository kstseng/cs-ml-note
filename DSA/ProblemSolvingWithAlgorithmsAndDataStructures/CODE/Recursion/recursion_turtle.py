import turtle

def drawSprial(myTurtle, lineLen):
    """
    """
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(45)
        drawSprial(myTurtle, lineLen - 5)


def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        ## 先右轉 20 度
        t.right(20)
        tree(branchLen - 15, t)
        ## 再左轉 40 度
        t.left(40)
        tree(branchLen - 15, t)
        ## 再回到原先角度
        t.right(20)
        ## 退回到原先的起始點
        t.backward(branchLen)
    
def main():
    ## 螺旋
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()

    drawSprial(myTurtle, 100)
    myWin.exitonclick()

    ## 畫樹
    t = turtle.Turtle()
    myWin = turtle.Screen()
    ## 預設是面向右邊
    ## 因此把他左轉 90 度
    t.left(90)
    tree(75, t)
    
    for i in range(7):
        t.right(45)
        tree(75, t)
    myWin.exitonclick()

if __name__ == "__main__":
    main()