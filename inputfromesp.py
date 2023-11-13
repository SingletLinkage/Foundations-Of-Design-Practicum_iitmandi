import requests
import time
import sys

def get_IP():
    ip = "192.168.213.191" # usual ip address when i connect to my network _void> (might change idk)
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    return ip

def connect(DELAY=1000):
    ESP32_IP = get_IP()  # Replace with the actual IP address of your ESP32
    data = '' # format (x, y)
    while True:
        try:
            response = requests.get(f"http://{ESP32_IP}/")
            if response.status_code == 200:
                # status code of 200 in an HTTP response signifies a successful request
                # the accompanying data should be available in the response body
                data = response.text
                print("Received data:", data)
            else:
                print("Error:", response.status_code)
        except Exception as e:
            print("Exception:", e)

        time.sleep(DELAY//1000)  # Adjust the interval as needed
        if not data:
            return data

if __name__ == '__main__':
    connect(500)