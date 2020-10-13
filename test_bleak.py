import logging
import asyncio
import platform
import sys

from bleak import BleakClient, BleakScanner, discover

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
h = logging.StreamHandler(sys.stdout)
h.setLevel(logging.DEBUG)
log.addHandler(h)


async def print_services(mac_addr: str):
    devices = await discover()
    batter_monitor_device = None
    for d in devices:
        if d.name == 'BatteryMonitor':
            batter_monitor_device = d.address
    device = await BleakScanner.find_device_by_address(batter_monitor_device)
    async with BleakClient(device) as client:

        for service in client.services:
            log.info("[Service] {0}: {1}".format(service.uuid, service.description))
            for char in service.characteristics:
                if "read" in char.properties:
                    try:
                        value = bytes(await client.read_gatt_char(char.uuid))
                    except Exception as e:
                        value = str(e).encode()
                else:
                    value = None
                log.info(
                    "\t[Characteristic] {0}: (Handle: {1}) ({2}) | Name: {3}, Value: {4} ".format(
                        char.uuid,
                        char.handle,
                        ",".join(char.properties),
                        char.description,
                        value,
                    )
                )
                for descriptor in char.descriptors:
                    value = await client.read_gatt_descriptor(descriptor.handle)
                    log.info(
                        "\t\t[Descriptor] {0}: (Handle: {1}) | Value: {2} ".format(
                            descriptor.uuid, descriptor.handle, bytes(value)
                        )
                    )


mac_addr = (
    "24:71:89:cc:09:05"
    if platform.system() != "Darwin"
    else "BatteryMonitor"
)
loop = asyncio.get_event_loop()
loop.run_until_complete(print_services(mac_addr))
