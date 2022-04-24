from gpiozero import Robot
import time
import RPi.GPIO as GPIO
from tkinter import *
from picamera import PiCamera
from time import sleep
from twython import Twython
import time
import adafruit_dht    
import os
from datetime import datetime
import time
import h5py
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from UpdatedCardAnalyzer import *
import os
# Initialize GPIO
now = datetime.now()
i = 0
tempF = 70.1
humidity = 29
bot = Robot(left=(25,7),right=(9,10))
camera = PiCamera()
camera.resolution = (640,480)
GPIO.setwarnings(False)		# suppress warnings
GPIO.setmode(GPIO.BCM)

led_f = 16
led_l = 21
led_b = 20
led_r = 12
GPIO.setup(led_f,GPIO.OUT)		# setting gpio pin #18 to output
GPIO.setup(led_l,GPIO.OUT)
GPIO.setup(led_b,GPIO.OUT)
GPIO.setup(led_r,GPIO.OUT)



#main =Tk()
def leftKey(event):
    GPIO.output(led_f,GPIO.HIGH)
    GPIO.output(led_r,GPIO.HIGH)
    GPIO.output(led_b,GPIO.HIGH)
    bot.left(0.5)
    print("left")
    GPIO.output(led_l,GPIO.LOW)
def rightKey(event):
    GPIO.output(led_f,GPIO.HIGH)
    GPIO.output(led_l,GPIO.HIGH)
    GPIO.output(led_b,GPIO.HIGH)
    bot.right(0.5)
    GPIO.output(led_r,GPIO.LOW)
    print("right")
def upKey(event):
    GPIO.output(led_l,GPIO.HIGH)
    GPIO.output(led_r,GPIO.HIGH)
    GPIO.output(led_b,GPIO.HIGH)
    bot.forward()
    GPIO.output(led_f,GPIO.LOW)
    print("forward")
def downKey(event):
    GPIO.output(led_f,GPIO.HIGH)
    GPIO.output(led_r,GPIO.HIGH)
    GPIO.output(led_l,GPIO.HIGH)
    bot.backward()
    GPIO.output(led_b,GPIO.LOW)
    print("backward")
def ctrlKey(event):
    GPIO.output(led_f,GPIO.HIGH)
    GPIO.output(led_r,GPIO.HIGH)
    GPIO.output(led_b,GPIO.HIGH)
    GPIO.output(led_b,GPIO.HIGH)
    bot.stop()
    print("stop")
def escKey(event):
    import sys; sys.exit()
def preview(*args):
    camera.start_preview(fullscreen=False, window = (150, 125, 1280, 720))
def stoppreview(*args):
    camera.stop_preview()
def take_picture(*args):
    global i
    i +=1
    camera.capture(f'/home/pi/Pictures/picture{i}.jpg')
def take_png(*args):
    global i
    i +=1
    camera.capture(f'/home/pi/Pictures/cards/picture{i}.png')
def tweet_picture():
    global i
    print("hello")
    image = open(f'/home/pi/Pictures/picture{i}.jpg','rb')
    message = "Another one!"
    response = twitter.upload_media(media=image)
    media_id =[response['media_id']]
    twitter.update_status(status=message,media_ids=media_id)
    print("check timeline")
def tweet_temp():
    global tempF
    now = datetime.now()
    d_string = now.strftime('%Y-%m-%d')        # date: year-mm-dd
    t_string = now.strftime('%H:%M:%S') 
    message = "The temp at {} is {}F".format(t_string, tempF)
    twitter.update_status(status=message)
def tweet_humid():
    global humidity
    now = datetime.now()
    t_string = now.strftime('%H:%M:%S') 
    message = "The humidity at {} is {}%".format(t_string, humidity)
    twitter.update_status(status=message)
def take_temp():
    global tempF
    temperature = dht_device.temperature
    tempF = temperature * 9/5 +32
    print (tempF)
    message = "The temperature is {}F".format(tempF)
    label3 = Label(text= message )
    label3.place(x=30, y=500)
def take_humid():
    global humidity
    humidity = dht_device.humidity
    print (humidity)
    message = "The humidity is {}%".format(humidity)
    label4 = Label(text= message )
    label4.place(x=30, y=600)



    
'''
def calculate():
    global label2
    model = load_model('/home/pi/Documents/Final/select_cards.h5')
    if len(os.listdir('/home/pi/Pictures/cards')) % 5 == 0:
        l = []
        for i in range(1, 5):
            img = cv2.imread(f'/home/pi/Pictures/cards/picture{i}.png')
            img = cv2.resize(img,(150,150))
            img = np.reshape(img,[1,150,150,3])
            detected = np.argmax(model.predict(img), axis=-1)
            l.append(detected)
        l0 = l_to_l0(l)
        l1 = numeric(l0)
        result = hand(l0, l1)
        label2['text'] = f'{result}'
            
    else:
        print('Wrong number of pictures in directory')    
'''
##Do not post twitter info
consumer_key = '9lMYL5ePAQRwFJPl0zHRxLkcu'
consumer_secret ='mL36tVYXjZscn4rqTozZZYNIoO5X1NHU7wCfeYIFjSynDSo4uR'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAANyZWgEAAAAASRe8zBOtLCp3qoVVI7gPtjto1RU%3D7L8pJ3QFreMnisfnAAFC9tszP8ndBgHf48XtIn4Zq2ko0tzfdM'
access_token = '1468329797248221184-MCGUbtJzXwBXVxJfxc1VQzvAYKZfcT'
access_token_secret = 'Jj36vCEWenml7Go8vOKODiKCeYmKeRjJuTUP5JMa5uDHV'

twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)
###DH11 Sensor info
# Kill any processes using the libgpio daemon 
cmd = "sudo pkill -9 libgpiod_pulsei"
os.system(cmd) 
# Initial the dht device, with data pin connected to:
dht_device = adafruit_dht.DHT11(4) # connecting to GPIO pin # 17
# Sleep for a few seconds to initialize the sensor
time.sleep(5)   


### LED

# Initialize GPIO




top = Tk()
top.geometry('1500x1500')
label = Label(top, text = "IIOT Rover")
'''
label.config(font = ("Courier",14))
label.pack()
label2 = Label(text="Testing")
label2.place(x=1300, y=500)
'''
T = Text(top, height = 5, width = 52)


b1 = Button(top,text = "Preview",command = preview, activeforeground = "green", activebackground = "yellow")
b2 = Button(top,text = "Stop Preview",command = stoppreview, activeforeground = "red", activebackground = "yellow")
b3 = Button(top,text = "Take Picture", command = take_picture, activeforeground = "yellow", activebackground = "black")
b4 = Button(top,text = "Tweet Picture",command = tweet_picture, activeforeground = "yellow", activebackground = "black")
b8 = Button(top,text = "Tweet temperature",command = tweet_temp ,activeforeground = "yellow", activebackground = "black")
b9 = Button(top,text = "Tweet Humidity", command = tweet_humid,activeforeground = "yellow", activebackground = "black")
b6 = Button(top,text = "Take temperature", command = take_temp, activeforeground = "yellow", activebackground = "black")
b7 = Button(top,text = "Take Humidity", command = take_humid, activeforeground = "yellow", activebackground = "black")	
#b5 = Button(top,text = "Calculate",command = calculate, activeforeground = "yellow", activebackground = "pink")
#b10 = Button(top,text = "Take png",command = take_png, activeforeground = "yellow", activebackground = "pink")
b1.place(x =30,y=50)
b2.place(x =30,y=100)
b3.place(x =30,y=250)
b4.place(x =30,y=300)
b6.place(x =30,y=450)
b7.place(x =30,y=550)
b8.place(x =30,y=650)
b9.place(x =30,y=700)
#b5.place(x =1300,y=450)
#b10.place(x =30,y=800)

top.bind('<Left>',leftKey)
top.bind('<Right>',rightKey)
top.bind('<Up>',upKey)
top.bind('<Down>',downKey)
top.bind('<Control_L>',ctrlKey)
top.bind('<Escape>',escKey)
top.bind('<p>',preview)
top.bind('<s>',stoppreview)
top.bind('<t>',take_picture)
#top.bind('<c>',calculate)
top.mainloop()
GPIO.cleanup()
