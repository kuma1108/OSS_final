import datetime
import time

date=str(time.strftime('%m/%d',time.localtime(time.time())))
print(date)

with open('study_schedule.txt','r')as file:
    content = list()
    size=0
    for line in file: 
        content.append(line)
        size=size+1

today = list()
for i in range(size):
    data,todo = content[i].split(':') 
    if data==date:
        today.append(todo)

with open('today.txt','w') as file:
    file.write("TODAY : {0}<br>\n".format(str(time.strftime('%m/%d/%y',time.localtime(time.time())))))
    if len(today)==0:
        file.write("Nothing to review")
    else: 
        for i in today:
            file.write("{0}<br>\n".format(i))
        
        
        

