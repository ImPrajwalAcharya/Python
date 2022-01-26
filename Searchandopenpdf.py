import shutil
import glob
import subprocess
import time
import os
def rev(x):
    return x[::-1]
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
path=desktop+'/**/*.pdf'
filelist=[]
filesearchlist=[]
print("This Works Only If Your Folder Or File is in desktop otherwise change path")
search=input("Write the name of pdf you want to search : ")
for file_name in glob.iglob(path,
                            recursive=True):
    length = len(file_name)
    filename = ''
    n = length - 1
    for i in range(length):
        if file_name[n] != '\\':
            filename = filename + file_name[n]
            n = n - 1
    filename = rev(filename)
    filelist.append(filename)
for i in filelist:
    for j in range(len(i)):
        if i[j].lower()==search[0].lower():
            if j+3<=len(i):
                if  i[j+1].lower()==search[1].lower():
                    if  i[j+2].lower()==search[2].lower():
                        if i[j+3].lower()==search[3].lower():
                            filesearchlist.append(i)

n=0
for i in filesearchlist:
    print(n,".",i)
    n=n+1
selecting=input("enter the file index you want to open")
length1=len(filesearchlist[int(selecting)])
for file_name in glob.iglob(path,
                            recursive=True):
    length = len(file_name)
    filetemp=file_name[length-length1:length]
    if filetemp==filesearchlist[int(selecting)]:
        print("Opening File wait ......")
        time.sleep(1)
        subprocess.Popen([file_name], shell=True)