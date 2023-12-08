import requests
import time
import sys
import writecsv

DELAY = 500
PATH = 'positions.csv'

def get_IP():
    ip = "192.168.245.38"   # ip address of ESP web server, replace with the actual IP address of your ESP
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    return ip

def connect(DELAY=1000):
    ESP_IP = get_IP()  
    data = '' # format (x, y)
    x0 = y0 = 0
    while True:
        try:
            response = requests.get(f"http://{ESP_IP}/")
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
    # txt: x y theta
    x, y = map(int, txt.split(' ')[:-1])
    return x, y

if __name__ == '__main__':
    writecsv.init(PATH)
    connect(DELAY)
