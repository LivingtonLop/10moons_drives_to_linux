import hid 
import json

def convert_bytes_a_string (d):
    for key, value in d.items():
        if isinstance (value, bytes):
            d[key]= value.decode('utf-8','ignore')
        elif isinstance (value, (int, float)):
            d[key]= value
        else:
            d[key]= str(value)
    return d

devices = hid.enumerate()

devices_convert = [convert_bytes_a_string(d) for d in devices]


with open("test/devices.json","w") as file:
    json.dump(devices_convert, file, indent=4) 
