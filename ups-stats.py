import subprocess

cmd = "upsc ups"
output = ""
measurements = ["battery.charge",
    "battery.charge.low",
    "battery.charge.warning",
    "battery.runtime",
    "battery.runtime.low",
    "battery.voltage",
    "battery.voltage.nominal",
    "driver.parameter.pollfreq",
    "driver.parameter.pollinterval",
    "input.transfer.high",
    "input.transfer.low",
    "input.voltage",
    "input.voltage.nominal",
    "output.voltage",
    "ups.delay.shutdown",
    "ups.delay.start",
    "ups.load",
    "ups.realpower.nominal",
    "ups.timer.shutdown",
    "ups.timer.start"                 
]
string_measurements = ["battery.mfr.date",
    "battery.type",
    "device.mfr",
    "device.model",
    "device.serial",
    "device.type",
    "driver.name",
    "driver.parameter.port",
    "driver.parameter.synchronous",
    "driver.version",
    "driver.version.data",
    "driver.version.internal",
    "ups.beeper.status",
    "ups.mfr",
    "ups.model",
    "ups.productid",
    "ups.serial",
    "ups.status",
    "ups.test.result",
    "ups.vendorid"
]

p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)

for line in p.stdout.readlines(): #read and store result in log file
    line = line.decode("utf-8").rstrip()
    key = line[: line.find(":")]
    value = line[line.find(":") + 2: ]

    if key in string_measurements:
        value = '"' + value + '"'
    measurement = key + "=" + value
    if output != "":
        measurement = "," + measurement
    output += measurement

output = "upsc " + output.rstrip()
print(output, end = '')