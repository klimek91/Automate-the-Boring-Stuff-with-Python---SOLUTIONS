import time

start_time = time.time()
begin_time = start_time
input("Press enter to start stopwatch, pressing enter again will start a new lap")
lap = 1
while True:
    input()
    lap_time = str(round(time.time() - begin_time,2))
    total_time = str(round(time.time() - start_time,2))
    begin_time = time.time()
    print("LAP #{}: {} ({})".format(str(lap).rjust(2), total_time.rjust(5), lap_time.rjust(5)), end='')
    lap+=1