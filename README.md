# homebridge-udp-server

The python udp-server for the homebridge-udp-plugin

```
Usage:
  python Main.py
```

To write own plugins for the server follow this scheme:

```
  class Plugin(object):
    """docstring for Plugin."""
    name = "Test-Plugin"

    def __init__(self):
        super(Plugin, self).__init__()

    def execute(self, variable, value):
        print "This is a test"

    def close(self):
        print "close test plugin"

```

The name have to be the same as in the homebridge accessory attribute "plugin" and it has to be unique!
Whenever the server recieves a udp-message directed to the plugin, the execute methode is triggered with a variable name and its value passed.
If there is something (for example a serial connection) that has to be closed, integrate it into the close methode.

The following plugin passes "00" followed by the rgb-values in hex from a udp-accessory to an arduino via serial:

```
import serial
import colorutils

class Plugin(object):
    name = "LED-Strip"

    def __init__(self):
        super(Plugin, self).__init__()
        self.ser = serial.Serial("/dev/tty.usbserial-1410")
        self.ser.baudrate = 9600
        self.currentHue = 0.0
        self.currentSaturation = 100.0
        self.currentBrightness = 100.0

    def execute(self, variable, value):
        if variable == "on":
            if value == True:
                c = colorutils.hsv_to_rgb((self.currentHue, self.currentSaturation/100, self.currentBrightness/100))
                self.ser.write('00%02x%02x%02x' % c)
                print("   [*] LED-Strip on")
            else:
                self.ser.write('00000000')
                print("   [*] LED-Strip off")
            return
        elif variable == "hue":
            self.currentHue = float(value)
            c = colorutils.hsv_to_rgb((self.currentHue, self.currentSaturation/100, self.currentBrightness/100))
            self.ser.write('00%02x%02x%02x' % c)
            print("   [*] LED-Strip change color")
        elif variable == "saturation":
            self.currentSaturation = float(value)
        elif variable == "brightness":
            self.currentBrightness = float(value)
            print("   [*] LED-Strip change brightness")
            
    def close(self):
        self.ser.close()
```

The homebridge-accessory would look like this (note that the plugin names have to match):

```
"accessories": [
      {
        "accessory": "UDP",
        "name": "Light",
        "mode": "lightbulb",
        "modeConfig": {"hue": true, "saturation": true, "brightness": true},
        "plugin": "Test-Plugin",

        "host": "127.0.0.1",
        "port": 1234
      }
}
```
