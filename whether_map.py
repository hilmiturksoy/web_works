import tkinter as tk
from tkinter import Label
import requests
from PIL import Image, ImageTk

def city(city_name):
    api_key = "8cc6d1d2af3d3daff1fd3b8259e536ca"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city_name, "appid": api_key}
    r = requests.get(url, params=params)
    data = r.json()

    try:

        if r.status_code == 200:
            temp = f"{round(data['main']['temp'] - 273.15, 2)} °C"
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            city_name = data['name']

            result = f"City: {city_name}\nWeather: {description}\nTemperature: {temp}\nWind Speed: {wind_speed} m/s"
            return result
        else:
            return f"Error: {r.status_code}"
    except ValueError:
        return f"Error: {r.status_code}"
    except ZeroDivisionError:
        return f"Error: {r.status_code}"
    except SyntaxError:
        return f"Error: {r.status_code}"



def update_label():
    result = city(entry.get())
    label.config(text=result)  # Label'ın metnini güncelle
    canvas.tag_raise(update_label)  # Arka planın kaybolmaması için güncelleme fonksiyonu


root = tk.Tk()
root.geometry("600x400")
root.title("Weather App")

# Backgraund
image_path = "D:/Pythonold/9444.jpg"
image = Image.open(image_path)
resize_img = image.resize((600, 400))
photo = ImageTk.PhotoImage(resize_img)

# Canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=photo, anchor="nw")

# Entry
entry = tk.Entry(root, width=30)
entry.place(x=50, y=50)
entry.insert(0, "Eskisehir")

# Update
button = tk.Button(root, text="Check", command=update_label)
button.place(x=50, y=90)

#Label
label = Label(root, text="Enter a city and click Check", bg="#77addb", fg="white", font=("Times New Roman", 16))
label.place(x=50, y=210)


root.mainloop()
