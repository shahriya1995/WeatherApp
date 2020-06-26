import requests
import tkinter
from tkinter import font
from PIL import ImageTk, Image

def test_function(entry):
    print("button clicked")

def format_response(weather):

    try:
        name = weather['city']['name']
        des = weather['list'][0]['weather'][0]['description']
        temp = weather['list'][0]['main']['temp']

        final_str =  'City:%s \nConditions: %s \nTemperature(F): %s' %(name, des, temp)
        print(final_str)
    except:
        final_str = "Not found"

    return final_str


def get_weather(city):

    weather_key = '470c76fbd31ef55bca8fdac10b2ee059'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q':city,'units': 'imperial'}
    response = requests.get(url,params=params)
    weather = response.json()
#     print(weather)
#     print(weather['city']['name'])
#     print (weather['list'][0]['weather'][0]['description'])
#     print (weather['list'][0]['main']['temp'])

    label['text'] = format_response(weather)

root = tkinter.Tk()

# set size of the GUI canvas
canvas = tkinter.Canvas(root, height=700 ,width=800)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("landscape.png"))
bg_label = tkinter.Label(root,image=img)
bg_label.place(relwidth=1,relheight=1)

frame = tkinter.Frame(root, bg='#80c1ff' ,bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1 ,anchor='n')

entry = tkinter.Entry(frame, font = ('Courier',40))
entry.place(relwidth=0.65,relheight=1)

button = tkinter.Button(frame,text = "Get Weather", font = ('Courier',20) ,command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight =1)

lower_frame= tkinter.Frame(root, bg='#80c1ff' ,bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6 ,anchor='n')

label = tkinter.Label(lower_frame, font = ('Courier',20))
label.place(relwidth=1,relheight=1)

root.mainloop()


