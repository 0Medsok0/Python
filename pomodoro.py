from datetime import datetime, timedelta
import time

def pomodoro_timer():
    print("Начало сессии Pomodoro")
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=25)
    while True:
        now = datetime.now()
        if now > end_time:
            break
        time.sleep(60)
    print("Конец сессии Pomodoro!")

pomodoro_timer()
