from tkinter import *
from tkinter import ttk
import requests

def data_get():
    try:
        city = com.get()  # Get the selected city
        api_key = "your_valid_api_key_here"  # Replace with your actual API key
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        ).json()

        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])

        # Convert Kelvin to Celsius and extract max and min temperatures
        temp_celsius = f"{data['main']['temp'] - 273.15:.2f}°C"
        temp_max_celsius = f"{data['main']['temp_max'] - 273.15:.2f}°C"
        temp_min_celsius = f"{data['main']['temp_min'] - 273.15:.2f}°C"

        temp_label1.config(text=f"{temp_celsius} (Max: {temp_max_celsius}, Min: {temp_min_celsius})")

        humidity_label2.config(text=f"{data['main']['humidity']}%")
        pressure_label1.config(text=f"{data['main']['pressure']} hPa")

    except Exception as e:
        print("Error:", e)

win = Tk()
win.title("Today's Weather with Max & Min Temp")
win.config(bg="sky blue")
win.geometry("590x750")

name_label = Label(win, text="Know Your Weather", font=("Comic Sans MS", 30, "bold"), bg="sky blue")
name_label.place(x=25, y=50, height=50, width=550)

list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
    "Gujarat", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand",
    "Karnataka", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Uttar Pradesh",
    "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
    "Puducherry"
]

com = ttk.Combobox(win, values=list_name, font=("Arial", 15))
com.place(x=25, y=120, height=50, width=550)
com.set("Select a City")

# Weather Condition
w_label = Label(win, text="Weather Condition", font=("Arial", 20))
w_label.place(x=25, y=220, height=50, width=210)
w_label1 = Label(win, text="", font=("Arial", 20))
w_label1.place(x=250, y=220, height=50, width=325)

# Description
wb_label = Label(win, text="Description", font=("Arial", 18))
wb_label.place(x=25, y=280, height=50, width=220)
wb_label1 = Label(win, text="", font=("Arial", 18))
wb_label1.place(x=250, y=280, height=50, width=325)

# Temperature
temp_label = Label(win, text="Temperature", font=("Arial", 20))
temp_label.place(x=25, y=340, height=50, width=220)
temp_label1 = Label(win, text="", font=("Arial", 20))
temp_label1.place(x=250, y=340, height=50, width=325)

# Humidity
humidity_label = Label(win, text="Humidity", font=("Arial", 20))
humidity_label.place(x=25, y=400, height=50, width=220)
humidity_label2 = Label(win, text="", font=("Arial", 20))
humidity_label2.place(x=250, y=400, height=50, width=325)

# Pressure
pressure_label = Label(win, text="Pressure", font=("Arial", 20))
pressure_label.place(x=25, y=460, height=50, width=220)
pressure_label1 = Label(win, text="", font=("Arial", 20))
pressure_label1.place(x=250, y=460, height=50, width=325)

# Button
done_button = Button(win, text="Get Weather", command=data_get, font=("Comic Sans MS", 30, "bold"))
done_button.place(relx=0.5, rely=0.3, anchor=CENTER)

win.mainloop()
