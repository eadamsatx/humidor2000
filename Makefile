

connect:
	cd arduino && arduino-cli board attach serial:///dev/cu.usbmodem141401 humidor2000

compile: connect
	cd arduino && arduino-cli -vvv compile --fqbn arduino:mbed:nano33ble humidor2000/


upload: compile
	cd arduino && arduino-cli -vvv upload -p /dev/cu.usbmodem141401 --fqbn arduino:mbed:nano33ble humidor2000/
