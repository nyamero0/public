import math
import turtle
turtle.title("Clock")
class Clock(object):
    hourHandLength = 100
    minHandLength = 125
    secHandLength = 150
    clockRadius = 200
    lengthEnum = (hourHandLength, minHandLength, secHandLength)
    @staticmethod
    def cycleRatio(value : int, base : int):
        return value % base / (base/2)
    @staticmethod
    def ratioToSlope(ratio : (int | float)):
        return (
            math.sin(math.pi * ratio),
            math.cos(math.pi * ratio)
        )
    def __init__(self, hour, minute, sec):
        self.pen = turtle.Turtle()
        self.hourHandPen = turtle.Turtle()
        self.minHandPen = turtle.Turtle()
        self.secHandPen = turtle.Turtle()
        self.handPens = {"hour":(self.hourHandPen, 12), "minute":(self.minHandPen, 60), "second":(self.secHandPen, 60)}
        self.hour = hour
        self.minute = minute
        self.sec = sec
        self.pen.screen.delay(0)
        self.pen.speed(0)
        self.pen.ht()
        self.hourHandPen.pensize(6)
        self.minHandPen.pensize(5)
        self.secHandPen.pensize(4)
        self.hourHandPen.pencolor("green")
        self.minHandPen.pencolor("blue")
        self.secHandPen.pencolor("red")
    def draw(self):
        self.pen.penup()
        self.pen.sety(-Clock.clockRadius)
        self.pen.pensize(4)
        self.pen.pendown()
        self.pen.circle(Clock.clockRadius)
        self.pen.penup()
        self.pen.home()
        self.pen.pensize(3)
        tempEnum = ("12", "3", "6", "9")
        paddingEnum = [(0, -27),(-10,-14.5),(0,-2),(12,-14.5)]
        for i in range(4):
            x, y = Clock.ratioToSlope(i / 2)
            self.pen.penup()
            self.pen.home()
            self.pen.goto(x*Clock.clockRadius+paddingEnum[i][0],y*Clock.clockRadius+paddingEnum[i][1])
            self.pen.write(tempEnum[i], False, align="center", font=("Romans", 18, "normal"))
        self.pen.penup()
        self.pen.home()
        handPens_values = list(self.handPens.values())
        tempEnum = (self.hour + self.minute / 60, self.minute, self.sec)
        for i in range(len(handPens_values)):
            pen, baseCycle = handPens_values[i]
            pen.ht()    
            pen.screen.delay(0)
            pen.speed(0)
            x , y = Clock.ratioToSlope(Clock.cycleRatio(tempEnum[i],baseCycle))
            pen.goto(x * Clock.lengthEnum[i], y * Clock.lengthEnum[i])
            pen.penup()
            pen.home()
    def clear(self):
        self.pen.clear()
    def updateHand(self, handName : str, value : (int, (int | float))):
        pen, baseCycle = self.handPens[handName]
        pen.clear()
        pen.penup()
        pen.home()
        pen.pendown()
        x, y = Clock.ratioToSlope(Clock.cycleRatio(value[0], baseCycle))
        pen.goto(x * value[1], y * value[1])
        pen.penup()
        pen.home()
        pen.pendown()
    def clearHand(self, handName : str):
        self.handPens[handName][0].clear()

def main():
    clock = Clock(9, 15, 0)
    clock.draw()
    turtle.mainloop()
if __name__ == "__main__":
    main()