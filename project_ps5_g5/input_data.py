import requests
import time
import sys
import writecsv

DELAY = 500
PATH = 'positions.csv'

def get_IP():
    ip1 = "192.168.213.191" # kunal's esp32
    ip = "192.168.40.38"   # usual ip address when i connect to my network _void> (might change idk)
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    return ip

def connect(DELAY=1000):
    ESP32_IP = get_IP()  # Replace with the actual IP address of your ESP32
    data = '' # format (x, y)
    x0 = y0 = 0
    while True:
        try:
            response = requests.get(f"http://{ESP32_IP}/")
            if response.status_code == 200:
                # status code of 200 in an HTTP response signifies a successful request
                # the accompanying data should be available in the response body
                data = response.text
                print("Received data:", data)
                
                x, y = parse(data)
                x0, y0 = writecsv.write(x, y, x0, y0, PATH)
            else:
                print("Error:", response.status_code)
        except Exception as e:
            print("Exception:", e)

        time.sleep(DELAY/1000)  # Adjust the interval as needed

def parse(txt:str):
    # txt: (x, y)
    x, y = map(int, txt[1:-1].split(', '))
    return x, y

if __name__ == '__main__':
    writecsv.init(PATH)
    connect(DELAY)