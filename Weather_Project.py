import requests
from pprint import pprint
import tkinter
from tkinter import *
import datetime
from datetime import date


root=tkinter.Tk()
root.geometry("450x150")
root.title("Weather App")
img = PhotoImage(file='weather.png')
root.tk.call('wm', 'iconphoto', root._w, img)
mycolor = '#%02x%02x%02x' % (160, 184, 208)  
mycolor2 = '#40E0D0'   
root.configure(bg=mycolor)
tkinter.Button(root, bg=mycolor, fg='white',
               activebackground='yellow', activeforeground=mycolor2).grid()

root.resizable(False,False)
def show():
    root.geometry("450x500")
    x= entry_city.get()
    y= entry_lat.get()
    z= entry_lon.get()
    print(x)
    print(y)
    print(z)


    if x != "":

        url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=08dd5fc9b6986b5346acac964e572f3b&units=metric'.format(x)
        res = requests.get(url)
        data = res.json()
    else:
        
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=08dd5fc9b6986b5346acac964e572f3b&units=metric'.format(y,z)

        res = requests.get(url)
        data = res.json()
    
    temp=str(data['main']['temp'])+' degree celcius'
    wind_speed=str(data['wind']['speed'])+' m/s'
    latitude=data['coord']['lat']
    longitude=data['coord']['lon']
    description=data['weather'][0]['description']
    pressure=str(data['main']['pressure'])+' hPa'
    temp_max=str(data['main']['temp_max'])+' degree celsius'
    temp_min=str(data['main']['temp_max'])+' degree celsius'
    humidity=str(data['main']['humidity'])+' %'
    country=data['sys']['country']
    name=data['name']
    pprint(data)
    print('Temperature:{} '.format(temp))
    print('wind speed:{}'.format(wind_speed))
    print('Latitude:{}'.format(latitude))
    print('Longitude:{}'.format(longitude))
    print('Description:{}'.format(description))
    print('Pressure:{}'.format(pressure))
    print('Temperature max:{} '.format(temp_max))
    print('Temperature min:{} '.format(temp_min))
    print('Humidity:{}'.format(humidity))
    print('Country:{}'.format(country))
    print('Name:{}'.format(name))

    current_date = datetime.date.today()
    print(current_date)


    date.config(text=current_date)
    city.config(text=name)
    l.config(text=temp)
    l1.config(text=wind_speed)
    l2.config(text=latitude)
    l3.config(text=longitude)
    l4.config(text=description)
    l5.config(text=pressure)
    l6.config(text=temp_max)
    l7.config(text=temp_min)
    l8.config(text=humidity)
    l9.config(text=country)



label_city=Label(root,text=" Your City",width=7,font=90,bg='green')
label_city.grid(row=0,column=0,pady=5)
entry_city=Entry(root,width=25)
entry_city.grid(row=0,column=1)
label_location=Label(root,text=" Your Location",width=12,font=90,bg='green')
label_location.grid(row=1,column=0,pady=5)
entry_lat=Entry(root,width=15)
entry_lat.grid(row=1,column=1)
entry_lon=Entry(root,width=15)
entry_lon.grid(row=1,column=2)
b=Button(root,text="Show Weather",width=15,bg='blue',fg='black',command=show)
b.grid(row=2,column=1)
city=Label(root,text="",font=30,bg='#%02x%02x%02x' % (160, 184, 208))
city.grid(row=3,column=1,pady=4)
date=Label(root,text="",font=30,bg='#%02x%02x%02x' % (160, 184, 208))
date.grid(row=4,column=1,pady=4)
temp=Label(root,text="Temperature  :-",font=20,bg='orange')
temp.grid(row=5,column=0)
l=Label(root,text="",bg='orange')
l.grid(row=5,column=1)
wind=Label(root,text="Wind Speed  :-",font=20,bg='orange')
wind.grid(row=6,column=0)
l1=Label(root,text="",bg='orange')
l1.grid(row=6,column=1)
latitude=Label(root,text="Latitude  :-",font=20,bg='orange')
latitude.grid(row=7,column=0)
l2=Label(root,text="",bg='orange')
l2.grid(row=7,column=1)
longitude=Label(root,text="Longitude  :-",font=20,bg='orange')
longitude.grid(row=8,column=0)
l3=Label(root,text="",bg='orange')
l3.grid(row=8,column=1)
description=Label(root,text="Description  :-",font=20,bg='orange')
description.grid(row=9,column=0)
l4=Label(root,text="",bg='orange')
l4.grid(row=9,column=1)
pressure=Label(root,text="Pressure :-",font=20,bg='orange')
pressure.grid(row=10,column=0)
l5=Label(root,text="",bg='orange')
l5.grid(row=10,column=1)
temp_max=Label(root,text="Temperature Max :-",font=20,bg='orange')
temp_max.grid(row=11,column=0)
l6=Label(root,text="",bg='orange')
l6.grid(row=11,column=1)
temp_min=Label(root,text="Temperature Min :-",font=20,bg='orange')
temp_min.grid(row=12,column=0)
l7=Label(root,text="",bg='orange')
l7.grid(row=12,column=1)
humidity=Label(root,text="Humidity :-",font=20,bg='orange')
humidity.grid(row=13,column=0)
l8=Label(root,text="",bg='orange')
l8.grid(row=13,column=1)
country=Label(root,text="Country :-",font=20,bg='orange')
country.grid(row=14,column=0)
l9=Label(root,text="",bg='orange')
l9.grid(row=14,column=1)

root.mainloop()
