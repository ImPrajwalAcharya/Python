import requests
import tkinter as tk
def show():
    city=textBox.get()
    requesturl=f"{baseurl}?appid={API_KEY}&q={city}"
    response=requests.get(requesturl)
    if response.status_code==200:
        label1=tk.Label(root,text='Weather of '+city)
        canvas1.create_window(150,20,window=label1)
        data=response.json()
        weather=data["weather"][0]["description"]
        label1=tk.Label(root,text='Weather : ' +weather)
        canvas1.create_window(100,50,window=label1)
        temperature=data['main']["temp"]
        label1=tk.Label(root,text='Temperature : ' +str( temperature)+' kelvin')
        canvas1.create_window(100,100,window=label1)
    else:
        label1=tk.Label(root,text='error')
        canvas1.create_window(250,200,window=label1)
root=tk.Tk()
canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()
textBox = tk.Entry(root, width=10, font="Calibri 10")
canvas1.create_window(150, 150, window=textBox)
API_KEY='9e4cf60e5ba77d4d3bb154803e97a00f'
baseurl="http://api.openweathermap.org/data/2.5/weather"

button1 = tk.Button(text='Click Me',command=show, bg='brown',fg='white')
canvas1.create_window(150, 200, window=button1)

root.mainloop()    