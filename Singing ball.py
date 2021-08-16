#necessary modules
import turtle
import random
import winsound

#Window setup
win = turtle.Screen()#defines garphic window
win.bgcolor("black")
win.setup(width = 800,height=600) #to set the window popup size

#if you click left or right key, you can hear song until the ball hits the screen
def playX():
    winsound.PlaySound("X.wav",winsound.SND_ASYNC)
def playY():
    winsound.PlaySound("Y.wav",winsound.SND_ASYNC)
def play():
    winsound.PlaySound("laser.wav",winsound.SND_ASYNC) #to play the sound

win.listen()
win.onkeypress(playX,"Left")
win.onkeypress(playY,"Right")

#Word Display setup
anim_title = turtle.Turtle()
anim_title.speed(0)
anim_title.color("white")
anim_title.penup()
anim_title.setposition(15,3)
animstring = "SINGING BALL"
anim_title.write(animstring, False, align="center", font=("Times New Roman", 30, "bold"))
anim_title.hideturtle()

anim_title1 = turtle.Turtle()
anim_title1.speed(0)
anim_title1.color("white")
anim_title1.penup()
anim_title1.setposition(-160,-30)
animstring1 = "(Press Left or Right key to hear the 'SONG')"
anim_title1.write(animstring1, False, align="left", font=("calibri", 15, "normal"))
anim_title1.hideturtle()


#ball setup
ball = turtle.Turtle()
colors = ["blue","white","red","light green","purple","cyan"]
ball.color(random.choice(colors))
ball.shape("circle")
ball.shapesize(2.7,2.7)

#speed of the bouncing ball
spdX = random.randint(1,2) 
spdY = random.randint(1,2)


#condition to bounce the ball with the respective speed
while True:
    
    ball.setx(ball.xcor() + spdX) #ball move towards the x-axis
    ball.sety(ball.ycor() + spdY) #ball move towards the y-axis

    #x-axis
    if ball.xcor() > 390 or ball.xcor() < -390:
        spdX = spdX * -1 #bounce back while hits the window
        play() #play music while hits the window
        
    #y-axis
    if ball.ycor() > 290 or ball.ycor() < -290:
        spdY = spdY * -1 #bounce back while hits the window
        play() #play music while hits the window
        
turtle.done()
