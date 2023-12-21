"""
The program writes test table to the file sorted_student_counts.csv,
arranging all columns in ascending order of classes,
and if classes coincide, in ascending order of letters.
"""

import csv
file_adress='/Users/mariialeskovets/Desktop/Intership applications/Portfolio_Python_/work_with_files/file_2/'
file_adress_save='/Users/mariialeskovets/Desktop/Intership applications/Python/'

with open(file_adress+'student_counts.csv',
          encoding='utf-8') as file:
        rows=list(csv.DictReader(file,delimiter=',',quotechar='"'))
        columns=list(rows[0].keys())
        y=[columns[0]]
        columns=columns[1:]
        column=list(map(lambda x: x.split('-'),columns))
        column1=list(map(lambda x: [int(x[0]),x[1]],column))
        column3=sorted(column1,key=lambda x: x[1])
        column2=sorted(column3,key=lambda x: x[0])
        for i in column2:
            i=str(i[0])+'-'+i[1]
            y.append(i)
        with open(file_adress_save+'file_2_output.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=y, delimiter=',')
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
