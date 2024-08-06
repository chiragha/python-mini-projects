import time

def countdown(my_time):
    while my_time:
        mins, secs = divmod(my_time, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        my_time -= 1

    print("TIME'S UP")

my_time = input('Enter the time in seconds: ')

countdown(int(my_time))