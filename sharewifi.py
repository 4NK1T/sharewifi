import os
import subprocess
import qrcode

def generateQR():
    # get OS name
    os_name = os.name

    if os_name == 'nt':
        # Windows OS
        try:
            # get the connected WiFi network name
            wifi_output = subprocess.check_output(["netsh", "wlan", "show", "interfaces"])
            wifi_output = wifi_output.decode('ascii')
            ssid_index = wifi_output.index('SSID')
            ssid = wifi_output[ssid_index:].split('\n')[0].split(': ')[1].strip()

            # Get the connected WiFi network and password
            password_output = subprocess.check_output(["netsh", "wlan", "show", "profile", ssid, "key=clear"])
            password_output = password_output.decode('ascii')
            key_index = password_output.index('Key Content')
            password = password_output[key_index:].split('\n')[0].split(': ')[1].strip()

            # create QR code for WiFi network name and password
            qr_data = 'WIFI:T:WPA;S:{};P:{};;'.format(ssid, password)
            qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=2, border=2)
            qr.add_data(qr_data)
            qr.make(fit=True)
            qr.print_ascii(tty=True)
        except subprocess.CalledProcessError:
            print("Error: Not connected to a known wifi network.")
    else:
        # Unix-based OS
        try:
            wifi_output = subprocess.check_output(["iwgetid", "-r"])
            wifi_output = wifi_output.decode('ascii').strip()

            password_output = subprocess.check_output(["sudo", "grep", "psk=", "/etc/NetworkManager/system-connections/{}.nmconnection".format(wifi_output)])
            password_output = password_output.decode('ascii')
            password = password_output.split('=')[1].strip()

            # create QR code for WiFi network name and password
            qr_data = 'WIFI:T:WPA;S:{};P:{};;'.format(wifi_output, password)
            qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=2, border=2)
            qr.add_data(qr_data)
            qr.make(fit=True)
            qr.print_ascii(tty=True)
        except subprocess.CalledProcessError:
            print("Error: Not connected to a known wifi network.")

if __name__ == '__main__':
    generateQR()
