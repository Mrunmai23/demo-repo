import tkinter as tk
import serial
import serialport
import plain
# Assuming the serial port is "/dev/ttyACM0". Replace it with the appropriate port for your system.
ser = serialport.ser

def get_stage_value(serial_data):
    data = ser.readline()
    serial_data = data.decode('latin-1')
    values = serial_data.split(',')
    if len(values) > 2:
        try:
            stage_value = int(values[2])
            return stage_value
        except ValueError:
            return None
    else:
        return None

def get_stage_text(stage_value):
    if stage_value == 1:
        return "Launch Pad"
    elif stage_value == 2:
        return "Ascent1"
    elif stage_value == 3:
        return "Descent1"
    elif stage_value == 4:
        return "Descent2"
    else:
        return "Landed"

def update_stage_label():
    serial_data = ser.readline()
    stage_value = get_stage_value(serial_data)
    if stage_value is not None:
        stage_text = get_stage_text(stage_value)
        stage_label.config(text=stage_text)

    plain.frame10.after(100, update_stage_label)  # Schedule the next update after 100ms

# Create a Tkinter window


# Create a label to display the stage status
stage_label = tk.Label(plain.frame10, text="", font=("Helvetica", 20))
stage_label.pack(pady=20)

# Start the update loop to continuously check for new data


# Start the Tkinter main loop

