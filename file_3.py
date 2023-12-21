
"""
The program that determines and displays the cheapest product
and the name of the store that sells it.
"""

import csv

file_adress='/Users/mariialeskovets/Desktop/Intership applications/Portfolio_Python_/work_with_files/file_3/'

with open(file_adress+'prices.csv', encoding='utf-8') as file:
        rows=list(csv.DictReader(file,delimiter=';',quotechar='"'))
        b=[]
        m=list(rows[0].keys())[0]
        a,d={},{}
        for i in rows:
            for k,v in i.items():
                if v.isdigit()==True:
                    v=int(v)
                    d[k]=v
            p=list(i.values())[0]
            z=[list(i.values())[0],min(d.items(),key=lambda x: x[1])]
            b.append(z)
        o=min(b,key=lambda x: x[1][1])
        print(o[1][0]+':'+' '+o[0])
