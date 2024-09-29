import time
import os

def pomodoro(work_time, break_time):
    while True:
        print("Work time!")
        time.sleep(work_time * 60)
        os.system('say "Time for a break!"')
        print("Break time!")
        time.sleep(break_time * 60)
        os.system('say "Time to work!"')

work_time = 25
break_time = 5

pomodoro(work_time, break_time)
