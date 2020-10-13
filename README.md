# humidor2000
Overengineered humidor maintenance software.

## Running with arduino-cli

Aruidno libraries required:

```
Name                      Installed Available   Location Description
Adafruit_NeoPixel         1.6.0    -           user     Arduino library for controlling singl...
Adafruit_NeoPXL8          1.0.4    -           user     Arduino library for controlling 8 Neo...
Adafruit_Zero_DMA_Library 1.0.8    -           user     DMA helper/wrapped for ATSAMD21 such ...
Arduino_HTS221            1.0.0    -           user     Allows you to read the temperature an...
ArduinoBLE                1.1.3    -           user     Enables BLE connectivity on the Ardui...
```

connect to board
```
cd arduino/
arduino-cli board attach serial:///dev/cu.usbmodem141401 humidor2000
```

compile
```
cd arduino
arduino-cli -vvv compile --fqbn arduino:mbed:nano33ble humidor2000/
```

upload
```
cd arduino
arduino-cli -vvv upload -p /dev/cu.usbmodem141401 --fqbn arduino:mbed:nano33ble humidor2000/
```


#### Tips:

Using screen to connect to the arduino serial port

```
screen /dev/cu.usbmodem141401 9600
```

## Resources

https://mjoldfield.com/atelier/2009/02/arduino-cli.html
