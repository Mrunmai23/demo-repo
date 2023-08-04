import serial

def main():
    ser = serial.Serial('COM6', baudrate=9600)
    
    # Discard initial garbage values
    discard_initial_garbage(ser)
    
    with open("flight.csv", "a", encoding='utf-8', errors='ignore') as flight_file:
        flight_file.write("Timestamp,Data\n")  # Write header to the CSV file
        while True:
            try:
                data = ser.readline()
                data_str = data.decode('latin-1', errors='ignore').strip()
                if data_str:  # Only write non-empty lines
                    flight_file.write(f"{get_timestamp()},{data_str}\n")
                    flight_file.flush()  # Flush to ensure immediate write
                    print(f"{get_timestamp()} - {data_str}")
            except KeyboardInterrupt:
                print("KeyboardInterrupt: Stopping data collection.")
                break
            except Exception as e:
                print(f"Error: {e}")

def discard_initial_garbage(serial_port, max_attempts=10):
    # Discard initial garbage values up to max_attempts times
    for _ in range(max_attempts):
        serial_port.readline()

def get_timestamp():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    main()
