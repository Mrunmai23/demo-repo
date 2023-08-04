import plain
from tkinter import *
import gps
import SerialMonitor
import map
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
#5225+++++++
import Systemstats
button1 = Button(plain.frame5,wraplength=200, text="SYSTEM STATISTICS")
button1.config(background="light slate blue",foreground="white", font=('Arial', 18),command=lambda:Systemstats.update_stage_label())
button1.place(x=30, y=50)

button = Button(plain.frame5,wraplength=200, text="SERIAL MONITOR")
button.config(background="light slate blue",foreground="white", font=('Arial', 20),command=lambda:SerialMonitor.read_serial())
button.place(x=30, y=180)

def update_graphed_data():
    frame = 0  # You can set an appropriate value for the frame
    map.update_plot(frame)
    map.show_plots()
# Your other GUI setup code

button = Button(plain.frame5, wraplength=200, text="GRAPHED DATA", command=update_graphed_data)
button.config(background="light slate blue", foreground="white", font=('Arial', 20))
button.place(x=30, y=310)

button = Button(plain.frame5,wraplength=200, text="GPS MAP")
button.config(background="light slate blue",foreground="white", font=('Arial', 21),command=lambda:gps.loop(gps.map_widget))
button.place(x=30, y=450)

plain.window.mainloop()