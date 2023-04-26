from tkinter import *

from bs4 import BeautifulSoup
import requests
import tkinter as tk

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.1.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching......\n")
    soup = BeautifulSoup(res.text,'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    textbox.config(text=location + "\n Climate:" + info + "\n" + weather + "°C")
def get_weather():
    city = city_entry.get()
    city = city + " weather"
    weather(city)

# Create the GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("700x300")

# Create the widgets
city_entry = tk.Entry(root, font=('Arial', 14))
search_button = tk.Button(root, text="Search", command=get_weather)
result_label = tk.Label(root, font=('Arial', 18), justify='left')
label=tk.Label(root,text="Enter city name:")
label.grid(row=0,column=0)
textbox = Label(root, width=20, height=10,font=('Arial', 18))
textbox.grid(row=1, column=0,columnspan=4,padx=10, pady=10)
# Add the widgets to the GUIw
city_entry.grid(row=0,column=1 ,padx=10, pady=10)
search_button.grid(row=0,column=2,padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
