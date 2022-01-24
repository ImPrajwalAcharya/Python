import requests
import tkinter as tk
import time
def func(event):
    show()
def show():
    city=textBox.get()
    requesturl=f"{baseurl}?appid={API_KEY}&q={city}"
    response=requests.get(requesturl)
    if response.status_code==200:
        label5['text']=''
        label2['text']='Weather of '+city
        data=response.json()
        weather=data["weather"][0]["description"]
        label3['text']='Weather : ' +weather
        temperature=data['main']["temp"]
        label4['text']='Temperature : ' +str( temperature)+' kelvin'
        label1['text']=''
    else:
        label5['text']='Error Enter correct City'
    textBox.delete(0,'end')
root=tk.Tk()
canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()
label1=tk.Label(root,text='Enter the Name of city')
canvas1.create_window(150,10,window=label1)
textBox = tk.Entry(root, width=30, font="Calibri 10")
canvas1.create_window(150, 150, window=textBox)
API_KEY='9e4cf60e5ba77d4d3bb154803e97a00f'
root.bind('<Return>', func)
baseurl="http://api.openweathermap.org/data/2.5/weather"
label2=tk.Label(root,text='')
label3=tk.Label(root,text='')
label4=tk.Label(root,text='')
label5=tk.Label(root,text='')
canvas1.create_window(150,30,window=label2)
canvas1.create_window(100,50,window=label3)
canvas1.create_window(100,100,window=label4)
canvas1.create_window(150,250,window=label5)
button1 = tk.Button(text='Update',command=show, bg='blue',fg='white')
canvas1.create_window(150, 200, window=button1)
canvas1.pack()
root.mainloop()    