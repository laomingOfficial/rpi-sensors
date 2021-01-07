import Adafruit_DHT
import time

# git clone https://github.com/laomingofficial/Adafruit_Python_DHT
# sudo mkdir -p /usr/local/lib/python3.7/dist-packages/
# sudo python3 setup.py install

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17


def start():
    while True:
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("溫度={0:0.1f}C 濕度={1:0.1f}%".format(temperature, humidity))
        else:
            print("傳感器讀取失敗.")
        time.sleep(3)


if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        exit()
