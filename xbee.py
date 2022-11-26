from digi.xbee.devices import XBeeDevice
print("XBEE Confg")
xbee = XBeeDevice("COM1", 9600)
xbee.open()

# Set the destination address of the device.
#dest_address = XBee64BitAddress.from_hex_string("0013A20040XXXXXX")
#xbee.set_dest_address(dest_address)

# Read the operating PAN ID of the device.
dest_addr = xbee.get_dst_address()

# Set the PAN ID of the XBee to Team ID.
xbee.set_pan_id("2022ASI-005")

# Read the operating PAN ID of the device.
pan_id = xbee.get_pan_id()

# Read the output power level.
p_level = xbee.get_power_level()