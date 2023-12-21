'''
Input sample:

ball,color,purple
ball,size,4
ball, notes, it's round
cup,color,blue
cup,size,1
cup,notes,none

Each line of this fragment contains three values separated by commas: the name of the object,
the property of this object, the value of the property. 

The function condense_csv() takes two arguments in the following format:

filename — name of the csv file, for example, data.csv;

id_name — common name for objects

The function transforms the content of a file into the CSV format, by
grouping the rows in the first column and naming the first column by id_name argument.
The function should writes the result to the file_1_output.csv file.
'''




import csv

file_adress='/Users/mariialeskovets/Desktop/Intership applications/Portfolio_Python_/work_with_files/file_1/'
file_adress_save='/Users/mariialeskovets/Desktop/Intership applications/Python/'

def condense_csv(filename,id_name):
    with open(filename, encoding='utf-8') as file:
        rows=list(csv.reader(file,delimiter=',',quotechar='"'))
        d={}
        b={}
        c=[id_name]
        e=dict()
        f=[]
        for i in rows:
            a=dict(zip(i[1::1],i[2::1]))
            a2=''.join(list(a.keys()))
            b.setdefault(i[0],{}).update(a)
            d.setdefault(id_name,{}).update(b)
            c.append(i[0])
            c.append(a2)
        for k,v in d.items():
            for k1,v1, in v.items():
                e[k]=k1
                e.update(v1)
                f.append(e)
                e=dict()
        columns=list(f[0].keys())
        with open(file_adress_save+'file_1_output.csv','w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns, delimiter=',')
            writer.writeheader()
            for row in f:
                writer.writerow(row)

"""
Test Samples
"""
d1='data1.csv'
d2='data2.csv'
d3='data3.csv'
d4='data4.csv'
file_test={d1:"ID",d2:"ID",d3:"Position",d4:"ID"}
condense_csv(file_adress+d3,id_name=file_test[d3])
   
    
    















