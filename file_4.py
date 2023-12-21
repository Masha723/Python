"""
The program  processes only JSON files and displays the first and
last names of football players playing for the Arsenal football club.
The players must be listed in first name lexicographic order and,
if there is a match, in last name lexicographic order, each on a separate line.

"""



from zipfile import ZipFile
import json
result=[]

file_adress='/Users/mariialeskovets/Desktop/Intership applications/Portfolio_Python_/work_with_files/file_4/'
name=file_adress+'data.zip'
    
with ZipFile(name) as zip_file:
    files_names= {i.split('/')[-1]:i for i in zip_file.namelist()}
    json_names=list(filter(lambda x: x[0][-4:]=='json',files_names.items()))
    json_names=list(map(lambda x: x[1],json_names))
    foot_ball=[]
with ZipFile(name) as zip_file:
    zip_file.extractall()
    for i in json_names:
        with open(i,encoding='utf-8') as file:
            try:
                rows=json.load(file)
                if rows['team']=='Arsenal':
                    result.append([rows['first_name'],rows['last_name']])
            except ValueError:
                continue
    result1=sorted(result,key=lambda x: x[1])
    for i in sorted(result1):
        print(*i)
                




