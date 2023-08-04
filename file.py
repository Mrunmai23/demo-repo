def main():
    while(True):
        for i in range (10 ):
            data_str="10,5,8,7,6,9,3,7,i"
            flight_file = open("D:\GENEARL\XBEE Confg\demo-repo\Data\data5.csv", "a")
            
            flight_file.write(data_str)
            flight_file.write("\n")

            flight_file.close()
    
main()