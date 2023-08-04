import tkinter as tk
import random
import string
import folium
import tkintermapview
from PIL import Image, ImageTk
import serialport
# Initialize arrays for latitude and longitude
latitude_data = []
longitude_data = []

rand_num = random.random()
ser=serialport.ser 
if rand_num < 0.1:  # Adjust the probability as desired
    # Specific string
    data = ser.readline()
    data_str = data.decode('latin-1')
else:
    # Generate a random string
    data_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
values = data_str.split(',')
def generate_map():
    # Generate a random location for the map
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)

    # Create the Folium map
    map_obj = folium.Map(location=[latitude, longitude], zoom_start=20)

    return map_obj

def update_plot(data):
    global latitude_data, longitude_data, map_canvas

    # Process the data
    
    try:
        lat, lon = float(values[-1]), float(values[-2])  # Extract latitude and longitude
        # Append lat and lon to their respective arrays
        latitude_data.append(lat)
        longitude_data.append(lon)
    except ValueError:
        # In case of an error, simply return without updating the plot
        return

    # Create a new map canvas with updated markers
    new_map_canvas = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
    new_map_canvas.pack()

    # Add new markers for the updated latitude and longitude data points
    for lat, lon in zip(latitude_data, longitude_data):
        new_map_canvas.set_marker(lat, lon, text="2022ASI-005")

    # Destroy the previous map canvas
    map_canvas.destroy()

    # Update the map canvas reference
    map_canvas = new_map_canvas  # Corrected placement of the global declaration

# Create the Tkinter window
root = tk.Tk()
root.title("GPS Data Plot with Map Background")

# Create the initial map canvas
map_canvas = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
map_canvas.pack()

# Simulate receiving serial data in a loop (replace this with your actual data receiving mechanism)


def simulate_data():
    for data in values:
        update_plot(data)
        print(data)
        root.update()  # Update the Tkinter window to refresh the map
        root.after(1000)  # Delay between each iteration (in milliseconds)
print(values)
# Start the Tkinter main loop
root.after(100, simulate_data)
root.mainloop()