from datetime import datetime
import time

now = datetime.now()
print("python script started at: ", now.strftime("%H:%M:%S"))
i = 1
while i < 10:
    now = datetime.now()
    print("working task(s) {task_num} of 5 at {time_now}...".format(task_num=i, time_now=now.strftime("%H:%M:%S")))
    time.sleep(5)
    i += 1

print("job completed at: ", now.strftime("%H:%M:%S"))
      
