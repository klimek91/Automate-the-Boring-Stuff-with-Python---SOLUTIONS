import time, subprocess

count = 10
print("Countdown starts")

while count > 0:
    time.sleep(1)
    print(count)
    count-=1


subprocess.Popen(['start', 'alarm.wav'], shell=True)