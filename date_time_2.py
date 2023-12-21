"""
The program puts all the dairy's
records in chronological order and displays the result.
"""

from datetime import datetime


file_adress='/Users/mariialeskovets/Desktop/Intership applications/copy Portfolio/date_time/date_time_2/'

with open(file_adress+'diary.txt','r',encoding='utf-8') as file:
    f=[line.strip().split('\n') for line in file.read().split('\n\n')]
    result=dict()
    p=[]
    for k in f:
        for i  in k:
            try:
                a=datetime.strptime(i,'%d.%m.%Y; %H:%M')
            except:
                result[a]=result.get(a,p)+[i]
    
z=''
for key,value in sorted(result.items(),key=lambda x:x[0]):
    t=key.strftime('%d.%m.%Y; %H:%M')
    v='\n'.join(value)
    u=[t,v]
    u='\n'.join(u)+'\n\n'
    z+=u
print(z[:-1])
