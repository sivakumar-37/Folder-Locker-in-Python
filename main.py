print('Python provides us various uses of it which makes our life simple!!!')
print('In my project I have taken few of its uses and show them before you!!!')
print('Choices:')
print('Enter 1 for sending emails through python')
print('Enter 2 to Play the game-Space Invaders')
print('Enter 3 to secure your file/folder(s) using python')
print('Enter 4 to exit')
#Modules for game
import turtle
import os
import math
import random
from tkinter import *
# Modules for email
import base64
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders
import os.path
#modules for file/folder hider
import argparse
import shutil
import subprocess
from pyads import ADS

choice = int(input('Enter your choice>>>'))

if choice == 1:
    # Getting details of emails of the sender and reciever
    e=input("Enter gmail>>>")
    p=getpass.getpass()
    se=input("Enter email you want to send>>>")
    su=input("Enter subject>>>")
    m=input("Enter message>>>") 
    email=str(e)
    password=str(p)
    send_to_email=str(se)
    subject=str(su)
    message=str(m)
    # storing  the information to the server
    msg=MIMEMultipart()
    msg['from']=email
    msg['to']=send_to_email
    msg['subject']=subject
    # To attach the text to the mail
    msg.attach(MIMEText(message,'plain'))
    part=MIMEApplication("Application","octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition","attachment;filename= %s"  % filename)
    msg.attach(part)
    # To connect the server
    server= smtplib.SMTP_SSL('smtp.gmail.com',465)
    #To login to the server
    server.login(email,password)
    text=msg.as_string()
    # Sending the mail
    server.sendmail(email,send_to_email,text)
    # Exiting the server
    server.quit()
    
elif choice == 2:
    #Set up the screen
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Space Invaders")
    #Register the shapes
    turtle.register_shape("player.gif")
    turtle.register_shape("enemy.gif")
    turtle.register_shape("bullet.gif")
    #To draw the Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
        border_pen.hideturtle()

    #Set the score to 0
    score = 0

    #Draw the score
    score_pen = turtle.Turtle()
    score_pen.speed(0)
    score_pen.color("black")
    score_pen.penup()
    score_pen.setposition(-290, 260)
    scorestring = "Score: %s" %score
    score_pen.write(scorestring, False, align="left",font=("arial", 14,"normal"))
    score_pen.hideturtle()

    #Create the player turtle
    player = turtle.Turtle()
    player.shape("player.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)
    playerspeed = 50

    #Choose a number of enemies
    number_of_enemies = random.randint(5, 10)
    #Create an empty list of enemies
    enemies = []
    #Add enemies to the list
    for i in range(number_of_enemies):
        #Create the enemy
        enemies.append(turtle.Turtle())
    for enemy in enemies:
        enemy.shape("enemy.gif")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)
    enemyspeed = 15

    #Create the players bullet
    bullet = turtle.Turtle()
    bullet.color("yellow")
    bullet.shape("bullet.gif")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)

    bullet.hideturtle()

    bulletspeed = 50

    #Define bullet state
    #ready - ready to fire
    #fire - bullet is firing
    bulletstate ="ready"

    #Move the player left and right
    def move_left():
        x = player.xcor()
        x -= playerspeed
        if x < -280:
            x = - 280
        player.setx(x)

    def move_right():
        x = player.xcor()
        x += playerspeed
        if x > 280:
            x = 280
        player.setx(x)

    def fire_bullet():
        #Declare bulletstate as a global if it needs changed
        global bulletstate
        if bulletstate == "ready":
            bulletstate = "fire"
            #Move the bullet to the just above the player
            x = player.xcor()
            y = player.ycor() + 10
            bullet.setposition(x, y)
            bullet.showturtle()

    def isCollision(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 50:
            return True
        else:
            return False

    def restart():
        import sys
        os.startfile(sys.argv[0])

    #Create keyboard bindings
    turtle.listen()
    turtle.onkey(move_left,"Left")
    turtle.onkey(restart, "r")
    turtle.onkey(move_right,"Right")
    turtle.onkey(fire_bullet,"space")

    #Main game loop
    while enemies:
        for enemy in enemies:
            #Move the enemy
            x = enemy.xcor()
            x += enemyspeed
            enemy.setx(x)
            #Move the enemyback and down
            if enemy.xcor() > 280:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #Change enemy direction
                enemyspeed *= -1

            if enemy.xcor() < -280:
                #Move all enemies down
                for e in enemies:
                    y = e.ycor()
                    y -= 40
                    e.sety(y)
                #Change enemy direction
                enemyspeed *= -1

            #Check for a collision between the bullet and the enemy
            if isCollision(bullet, enemy):
                #Reset the bullet
                bullet.hideturtle()
                bulletstate ="ready"
                bullet.setposition(0, -400)
                enemy.hideturtle()
                enemies.remove(enemy)
                #Update the score
                score += 10
                scorestring = "Score: %s" %score

                score_pen.clear()
                score_pen.write(scorestring, False, align="left",font=("Arial", 14,"normal"))

            if isCollision(player, enemy):
                player.hideturtle()
                enemy.hideturtle()
                lose = Tk()
                l = Label(lose,text = " Game Over!!" ,fg = 'white', bg = 'black')
                l.pack()
                lose.mainloop()       
                break

        #Move the bullet
        if bulletstate == "fire":
            y =bullet.ycor()
            y +=bulletspeed
            bullet.sety(y)
        #Check to see if the bullet has gone to the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate ="ready"
        
    win = Tk()
    l1 = Label(win,text = " You won!!" ,fg = 'white', bg = 'black')
    l1.pack()
    win.mainloop()

elif choice==3:
    
    #Create a text file for hiding
    tfile=open(r'C:\Users\GAYU-SIVA\AppData\Local\Programs\Python\Python37\text.txt','w')
    #Directory of the folder you want to lock
    direc = input("Which folder you would like to lock:")
    #To make the zip of the directory
    shutil.make_archive("lock", "zip", root_dir=str(direc))
    print('Zip is READY')
    #To delete the given directory
    try:
        shutil.rmtree(direc)
    except OSError as e:
        print("error: ", e.filename, "- ", e.strerror)
    print('Folder is DELETED')

    print("\tYou will be redirected to command prompt for this choice!!!(From the pyfile contained directory)")
    print("\tFollow the below commands ↓↓↓↓↓")
    print()
    print("\t\t>>>main.py test.txt -o(For seeing the hidden files)")
    print("\t\t>>>main.py test.txt -a lock.zip(For adding the files to alternate data stream)")
    print("\t\t>>>main.py test.txt -e(For extracting the hidden files)")
    print("\t\t>>>main.py test.txt -r(For removing the entire hidden files)")

    parser= argparse.ArgumentParser()
    #Options
    parser.add_argument('file',help= 'Specify File or Directory')
    parser.add_argument('-o','--output',help='print output to terminal',action='store_true')
    parser.add_argument('-a','--add',help='add stream to <file>',type=str)
    parser.add_argument('-e','--extract',help='extract all',action='store_true')
    parser.add_argument('-r','--remove',help='remove all',action='store_true')
    
    args=parser.parse_args()
    #If file is given
    if args.file:
        handler=ADS(args.file)
        #Adding the file into the Stream
        if args.add:
            handler.addStream(args.add)
        if handler.containStreams():
            for stream in handler.getStreams()[:]:#[:]--->To return the copy of the list
                #Output-->To see the items in the Stream
                if args.output:
                    print(args.file+':'+stream)
                #Extract-->To extract the items from the Stream
                if args.extract:
                    fh=open(stream,'wb')
                    fh.write(handler.getStreamContent(stream))
                    fh.close()
                #Remove-->To remove all the items from the Stream
                if args.remove:
                    handler.removeStream(stream)
        #If file not given
        else:
            print(parser.usage)
        #For redirecting to Commend Prompt
        subprocess.call('start',shell=True)
       

elif  choice == 4:
    print('\t\tYou missed our mesmerizing program')
    exit(5)

else:
    print('Invalid choice')




