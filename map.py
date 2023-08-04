import random
import string
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serialport
# Set up the figure and axes for the graphs
fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8), (ax9, ax10, ax11, ax12)) = plt.subplots(3, 4, figsize=(12, 9))
ser = serialport.ser
# Create empty lists to store the received data
x_values = []
y_values = []
y_values1 = []
y_values2 = []
y_values3 = []
y_values4 = []
y_values5 = []
y_values6 = []
y_values7 = []
y_values8 = []
y_values9 = []
y_values10 = []
y_values11 = []


# Define a function to update the plots with data
def update_plot(frame):
    # Clear the previous plots
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()
    ax6.clear()
    ax7.clear()
    ax8.clear()
    ax9.clear()
    ax10.clear()
    ax11.clear()
    ax12.clear()
    # Generate a random number between 0 and 1
    rand_num = random.random()
    
    if rand_num < 0.1:  # Adjust the probability as desired
        # Specific string
        data = ser.readline()
        data_str = data.decode('latin-1')
    else:
        # Generate a random string
        data_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    
    # Process the data
    values = data_str.split(',')
    
    if len(values) >= 3:
        x_values.append(frame)
        y_values.append(int(values[1]))
        y_values1.append(int(values[2]))
        y_values2.append(float(values[3]))
        y_values3.append(float(values[4]))
        y_values4.append(float(values[5]))
        y_values5.append(float(values[6]))
        y_values6.append(float(values[7]))
        y_values7.append(float(values[8]))
        y_values8.append(float(values[9]))
        y_values9.append(float(values[10]))
        y_values10.append(float(values[10]))
        y_values11.append(float(values[11]))
    
    # Plot the data for the first graph
    ax1.plot(x_values, y_values, 'bo-')
    ax1.set_title('Graph 1')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    
    # Plot the data for the second graph
    ax2.plot(x_values, y_values1, 'ro-')
    ax2.set_title('Graph 2')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y1')

    ax3.plot(x_values, y_values2, 'ro-')
    ax3.set_title('Graph 3')
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y2')

    ax4.plot(x_values, y_values3, 'ro-')
    ax4.set_title('Graph 4')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y3')

    ax5.plot(x_values, y_values4, 'ro-')
    ax4.set_title('Graph 5')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y4')

    ax6.plot(x_values, y_values5, 'ro-')
    ax4.set_title('Graph 6')
    ax4.set_xlabel('X')
    ax4.set_ylabel('Y5')

    ax7.plot(x_values, y_values6, 'ro-')
    ax7.set_title('Graph 7')
    ax7.set_xlabel('X')
    ax7.set_ylabel('Y3')

    ax8.plot(x_values, y_values7, 'ro-')
    ax8.set_title('Graph 8')
    ax8.set_xlabel('X')
    ax8.set_ylabel('Y7')

    ax9.plot(x_values, y_values8, 'ro-')
    ax9.set_title('Graph 9')
    ax9.set_xlabel('X')
    ax9.set_ylabel('Y8')

    ax10.plot(x_values, y_values9, 'ro-')
    ax10.set_title('Graph 10')
    ax10.set_xlabel('X')
    ax10.set_ylabel('Y9')

    ax11.plot(x_values, y_values10, 'ro-')
    ax11.set_title('Graph 11')
    ax11.set_xlabel('X')
    ax11.set_ylabel('Y10')

    ax12.plot(x_values, y_values11, 'ro-')
    ax12.set_title('Graph 12')
    ax12.set_xlabel('X')
    ax10.set_ylabel('Y11')

    

# Create the animation
animation = FuncAnimation(fig, update_plot, interval=100)

# Show the plots
def show_plots():
    plt.tight_layout()
    plt.show()