import time
import board
import adafruit_dht

# sudo pip3 install adafruit-circuitpython-dht
# sudo apt-get install libgpiod2

dhtDevice = adafruit_dht.DHT11(board.D17)


def destroy():
    dhtDevice.exit()


def start():
    while True:
        try:
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("溫度={0:0.1f}C 濕度={1:0.1f}%".format(temperature_c, humidity))
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(3)


if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        destroy()
