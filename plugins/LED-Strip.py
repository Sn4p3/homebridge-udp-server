import serial
import colorutils

class Plugin(object):
    name = "LED-Strip"

    def __init__(self):
        super(Plugin, self).__init__()
        self.ser = serial.Serial("/dev/tty.usbserial-1410")
        self.ser.baudrate = 9600
        self.currentHue = 0.0
        self.currentSaturation = 1.0
        self.currentBrightness = 1.0


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
        #print("hue:" + str(self.currentHue) + "; saturation: " + str(self.currentSaturation) + "; brightness: " + str(self.currentBrightness))
    def close(self):
        self.ser.close()
