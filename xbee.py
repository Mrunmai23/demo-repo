#Source: https://github.com/digidotcom/xbee-python/blob/master/examples/configuration/SetAndGetParametersSample/SetAndGetParametersSample.py
from digi.xbee.devices import XBeeDevice , RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
from digi.xbee.util.utils import hex_to_string

def main():
    configure_xbee()

def comp_port(port):
    
    #Baud rate= rate of bits transfered per seconds
    Baud_rate=9600 

local_xbee = XBeeDevice('COM4', 9600)
remote_xbee=(local_xbee,XBee64BitAddress)

def set_pan_id():
   
    # Set the PAN ID of the XBee to Team ID.
    local_xbee.set_pan_id("5")
    print("Local XBEE pan id ")



def reset_local_xbee():
    
    local_xbee.reset
    print("Local XBEE Reset Successfull")

def get_local_xbee():

    
    print("LOCAL XBEE:")
    print("Hardware Version:  ",local_xbee.get_hardware_version)
    print("Xbee Protocol:  ",local_xbee.get_protocol)
    #print("NETID:    ",local_xbee.get_net_id())
    print("PANID:    ",local_xbee.get_pan_id())
    #print("Power Level:    ",local_xbee.get_net_id())
    print("Dst Address: ",local_xbee.get_dest_address())



def configure_xbee():

    print("Configuration Function ")
   
      
    remote_xbee=(local_xbee,XBee64BitAddress)

    local_xbee.open()

    # Check if device is configured to apply changes.
    apply_changes_enabled = local_xbee.is_apply_changes_enabled()

    # Configure the device not to apply parameter changes automatically.
    if apply_changes_enabled:
        local_xbee.enable_apply_changes(False)

    #set parametrs

    set_pan_id()
    

    # Apply changes.
    local_xbee.apply_changes()
    # Write changes.
    local_xbee.write_changes()
    print("Parameter Setting For Local XBEE Successfull!")

    #Get Parameters
    get_local_xbee()
    

    #To reset the device
    reset_local_xbee()
    
      
     
if __name__=='__main__':
    main()