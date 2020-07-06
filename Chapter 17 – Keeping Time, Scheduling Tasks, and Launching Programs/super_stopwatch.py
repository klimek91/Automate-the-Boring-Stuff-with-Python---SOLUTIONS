import time


input("Press enter to start stopwatch and next enter to start next lap ")
start_time = time.time()
begin_time = start_time
lap = 1

while True:
    input()
    lap_time = round(time.time() - begin_time,2)
    all_time = round(time.time() - start_time,2)
    begin_time = time.time()
    print("LAP#{} {}s, total time {}s".format(lap, lap_time, all_time),end='')
    lap +=1