'''
The program displays the file structure of the desktop.zip
archive and the size of each file in uncompressed form.
Since the archive has its own folder hierarchy,
each nesting level is separated by two spaces.
'''

file_adress='/Users/mariialeskovets/Desktop/Intership applications/Portfolio_Python_/work_with_files/file_5/'



from zipfile import ZipFile
def convert_bytes(size):
    if size>=1073741824:
        return str(round(size/1073741824))+' '+'GB'
    if size>=1048576:
        return str(round(size/1048576))+' '+'MB'
    if size>=1024:
        return str(round(size/1024))+' '+'KB'
    if size<1024:
        return str(size)+' '+'B'
    
with ZipFile(file_adress+'desktop.zip') as zip_file:
    files_names=zip_file.infolist()
    for i in files_names:
        if i.is_dir()==False:
            size=i.file_size
            b=i.filename
            b=b.split('/')
            b=list(filter(lambda x: x!='',b))
            if len(b)-1==0:
                print(b[len(b)-1],convert_bytes(size))
            else:
                print((len(b)-1)*'  '+b[len(b)-1],convert_bytes(size))
        else:
            b=i.filename
            b=b.split('/')
            b=list(filter(lambda x: x!='',b))
            if len(b)-1==0:
                print(b[len(b)-1])
            else:
                print((len(b)-1)*'  '+b[len(b)-1])
    
