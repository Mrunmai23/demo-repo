import serial
import csv
import datetime

# Replace 'COMx' with the appropriate serial port name on your system
ser = serial.Serial('COM4', baudrate=9600)  # Adjust baudrate as per your serial device configuration

csv_file = 'D:\GENEARL\XBEE Confg\demo-repo\Data\data5.csv'

# Function to read data from the serial port and save it to CSV
def save_to_csv(csv_file):
    with open(csv_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Timestamp', 'Data'])  # Writing column headers

        try:
            while True:
                # Read data from the serial port (assumed to be a string)
                serial_data = ser.readline()

                # Get the current timestamp (you may use other time-related libraries for more precision)
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

                # Save data to CSV
                csv_writer.writerow([timestamp, serial_data])

        except KeyboardInterrupt:
            print("Data saving to CSV stopped.")
        except Exception as e:
            print("Error occurred:", str(e))

# Call the function to start saving data to CSV
save_to_csv(csv_file)
