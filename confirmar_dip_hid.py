import pywinusb.hid as winhid

#windows
def listar_dispositivos_hid_wind():
    dispositivos = winhid.find_all_hid_devices()
    for dispositivo in dispositivos:
        print(f"Dispositivo HID: {dispositivo.product_name}")

listar_dispositivos_hid_wind()

import hid 

def listar_dispositivos_hid():
    # Enumerar dispositivos HID conectados
    dispositivos = hid.enumerate()
    for dispositivo in dispositivos:
        print(f"Dispositivo HID: {dispositivo.get('product_string', 'Desconocido')}")

listar_dispositivos_hid()