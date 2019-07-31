# Description
Get data from USB-connected UPS into InfluxDB using Telegraf

Transforms `upsc` output like this:
```
battery.charge: 100
battery.charge.low: 10
battery.charge.warning: 20
battery.mfr.date: CPS
battery.runtime: 3690
battery.runtime.low: 300
battery.type: PbAcid
battery.voltage: 24.0
battery.voltage.nominal: 24
device.mfr: CPS
device.model: CP1500EPFCLCD
device.serial: CRMGT2000073
device.type: ups
driver.name: usbhid-ups
driver.parameter.pollfreq: 30
driver.parameter.pollinterval: 2
driver.parameter.port: /dev/ugen0.4
driver.parameter.synchronous: no
driver.version: 2.7.4
driver.version.data: CyberPower HID 0.4
driver.version.internal: 0.41
input.transfer.high: 260
input.transfer.low: 170
input.voltage: 239.0
input.voltage.nominal: 230
output.voltage: 260.0
ups.beeper.status: disabled
ups.delay.shutdown: 20
ups.delay.start: 30
ups.load: 11
ups.mfr: CPS
ups.model: CP1500EPFCLCD
ups.productid: 0501
ups.realpower.nominal: 900
ups.serial: CRMGT2000073
ups.status: OL
ups.test.result: No test initiated
ups.timer.shutdown: -60
ups.timer.start: -60
ups.vendorid: 0764
```
..into InfluxDB Line Protocol like this: 
```
ups battery.charge="100",battery.charge.low="10",battery.charge.warning="20",battery.mfr.date="CPS",battery.runtime="3690",battery.runtime.low="300",battery.type="PbAcid",battery.voltage="24.0",battery.voltage.nominal="24",device.mfr="CPS",device.model="CP1500EPFCLCD",device.serial="CRMGT2000073",device.type="ups",driver.name="usbhid-ups",driver.parameter.pollfreq="30",driver.parameter.pollinterval="2",driver.parameter.port="/dev/ugen0.4",driver.parameter.synchronous="no",driver.version="2.7.4",driver.version.data="CyberPower HID 0.4",driver.version.internal="0.41",input.transfer.high="260",input.transfer.low="170",input.voltage="241.0",input.voltage.nominal="230",output.voltage="260.0",ups.beeper.status="disabled",ups.delay.shutdown="20",ups.delay.start="30",ups.load="10",ups.mfr="CPS",ups.model="CP1500EPFCLCD",ups.productid="0501",ups.realpower.nominal="900",ups.serial="CRMGT2000073",ups.status="OL",ups.test.result="No test initiated",ups.timer.shutdown="-60",ups.timer.start="-60",ups.vendorid="0764"
```

## Usage

Edit the script `cmd` variable to reflect your setup. Specifically, change 'ups' to whatever you named your UPS in `NUT` or `upsd`.

Call the script from `telegraf.conf` like this
```
[[inputs.exec]]
   commands = ["python /mnt/vol01/system/telegraf/ups-stats.py"]
   timeout = "5s"
   interval = "10s"
   data_format = "influx"
```

## Compatibility
Tested on:
* Cyberpower CP1500EPFCLCD

If you're using this with a different UPS, please let me know so I can add it to the list
