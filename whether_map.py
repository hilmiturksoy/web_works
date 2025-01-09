import tkinter as tk
from tkinter import ttk, Label, Image
import requests
import json
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageTk
from web_works.link_checker import entry



#Request https://api.openweathermap.org/data/2.5/weather?q=London&appid={API key}

def city(city):
    api_key = "8cc6d1d2af3d3daff1fd3b8259e536ca"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    r = requests.get(url, params=params)
    data = r.json()

    if r.status_code == 200:
        temp = f"{round(data['main']['temp'] - 273.15, 2)} °C"
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        city_name = data['name']

        # Get all info
        print(f"City: {city_name}\nWeather: {description}\nTemperature: {temp}\nWind Speed: {wind_speed} m/s")
        result = f"City: {city_name}\nWeather: {description}\nTemperature: {temp}\nWind Speed: {wind_speed} m/s"
        return result

    else:
        return f"Error: {r.status_code}"



#Create WINDOW
root = tk.Tk() #Window
root.geometry("800x600")
root.resizable(True, True)
root.title("Weather Map")
root.grid()
root = Label(root, text="Weather Map") #Label
root.pack()

#Entry
entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black", width=30)
entry.pack()
entry.insert(tk.END, "Eskisehir")

#Button
button = tk.Button(root, text="Check", activebackground="#b89c39", activeforeground="white", width=10, command=lambda: city(entry.get()))
button.pack()

#Backgraund
image_path = "D:/Pythonold/9444.jpg"
image = Image.open(image_path)
resize_img=image.resize((800, 600))
photo = ImageTk.PhotoImage(resize_img)


#Canvas
canvas = tk.Canvas(root, width=resize_img.width, height=resize_img.height)
canvas.pack(fill="both", expand=True)

# Add the background image to the Canvas
canvas.create_image(0, 0, image=photo, anchor="nw")



# Add a Label on top of the Canvas
label = Label(root, text="update_label", bg="lightblue", fg="black", font=("Arial", 16))
label.place(x=50, y=210)




root.mainloop()


