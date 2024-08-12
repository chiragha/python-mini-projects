import time
import datetime
import pygame


def setAlarm(alarmTime):
    print(f"Alarm set for {alarmTime}")
    alarm_sound = "my_music.mp3"
    is_running = True


    while is_running:
         curr_time = datetime.datetime.now().strftime("%H:%M:%S")
         print(curr_time)


         if curr_time == alarmTime:
              print("WAKE UP!")

              pygame.mixer.init()
              pygame.mixer.music.load(alarm_sound)
              pygame.mixer.music.play()

              while pygame.mixer.music.get_busy():
                time.sleep(1)

              is_running = False
         
         time.sleep(1)

        
    

if __name__ ==  "__main__":
      alarmTime = input("Enter the alarm clock time (HH:MM:SS): ")
      setAlarm(alarmTime)