import tkinter as tk
import serial
import csv
import os.path
import serialport
from threading import Thread  # To run serial logging in a separate thread

window = tk.Tk()
width = 1250
height = 550
window.geometry("%dx%d" % (width, height))
window.config(bg="gray9")
window.title("Serial Logger Screen")
ser = serialport.ser  # replace with your own serial port and baud rate

text_box = tk.Text(window, height=2000, width=1200)
text_box.config(background="white", foreground="black", font=('Arial', 18))
text_box.pack()

file_path = "D:\GENEARL\XBEE Confg\demo-repo\Data\data5.csv"  # replace with your own file path
header_row = ["TEAM ID", "TIME STAMPING", "PACKET COUNT", "ALTITUDE", "PRESSURE", "TEMP", "VOLTAGE",
              "GNSS Time", "GNSS LATITUDE", "GNSS ALTITUDE", "GYRO X", "ACCELEROMETER X",
              "GYRO SPIN RATE", "FLIGHT SOFTWARE", "HUMIDITY", "PARTICLE COUNT", "DUST",
              "P2", "CHECKSUM", "ACCELEROMETER Y", "GYRO Y"]  # replace with your own column names

# Check if the file already exists, and create it if it doesn't
if not os.path.isfile(file_path):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header_row)

def read_serial():
    # Open the CSV file in append mode
    with open(file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        data = ser.readline()
        # decode the data to a string
        try:
            data_str = data.decode('latin-1')
        except UnicodeDecodeError:
            # handle decoding errors
            print("Error decoding data:", data)
            return
        # strip off any leading bytes before the string starting with "$$"
        start_str = "2022"
        start_idx = data_str.find(start_str)
        if start_idx != -1:
            data_str = data_str[start_idx:]
            # print the string on the Tkinter window
            text_box.insert('end', data_str + '\n')
            # split the data string by comma separator and write the resulting values to the CSV file
            csv_writer.writerow(data_str.split(','))
        text_box.see('end')
    window.after(10, read_serial)

# Close the CSV file when the tkinter window is closed
def on_closing():
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.after(10, read_serial)

def start_logging():
    thread = Thread(target=read_serial)
    thread.daemon = True  # The thread will close when the main GUI is closed
    thread.start()