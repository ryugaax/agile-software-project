from distutils.log import error
from threading import Timer
import time
from turtle import width
import cv2
import datetime
from tkinter import simpledialog
import os
import sendEmail
import json

class startRecording():
    def __init__(self):
        cap=cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        detection = False
        detection_stopped_time =  None
        timer_started = False
        SECONDS_TO_RECORD_AFTER_DETECTION = 5
        frame_size = (int(cap.get(3)) , int(cap.get(4)))
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        user_account = {}
        with open("logging_in.json" , "r") as read_file:
            user_account = json.load(read_file)

        while True:
            _,frame = cap.read()
            
            gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,5)
            eyes = eye_cascade.detectMultiScale(gray,1.1,3)
            
            # for (x,y,width,height) in faces:
            #     cv2.rectangle(frame,(x,y),(x+width , y+height),(0,255,0),3)
            # for (x,y,width,height) in eyes:
            #     cv2.rectangle(frame,(x,y),(x+width , y+height),(0,255,0),3)
            if len(faces) + len(eyes) > 0 :
                if detection:
                    timer_started = False
                else:
                    detection = True
                    # time : day - month - year - hour - minute - second
                    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                    print(current_time)
                    try:
                        os.mkdir('footages')
                    except:
                        print('')
                    out = cv2.VideoWriter( f"footages/{current_time}.mp4" , fourcc , 10 , frame_size)
                    print("start recording")
            elif detection:
                if timer_started:
                    if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                        detection = False
                        timer_started = False
                        print(user_account)
                        out.release()
                        sendEmail.footageSendTo(user_account["user_email"] , f"footages/{current_time}.mp4")
                        print("stop recording")
                else:
                    timer_started = True
                    detection_stopped_time = time.time()

                
            cv2.imshow("you are being watched" , frame)

            try:
                out.write(frame)
            except Exception as e:
                print(e)

            if cv2.waitKey(1) == ord('q'):  
                if pop_up() == user_account["user_password"]:
                    break

        out.release()
        cap.release()    
        cv2.destroyAllWindows()


def pop_up():
   pwd = simpledialog.askstring(" " , "please enter the password")
   return pwd