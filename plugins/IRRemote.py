import serial

class Plugin(object):
    name = "IRRemote"

    def __init__(self):
        super(Plugin, self).__init__()
        self.ser = serial.Serial("/dev/tty.usbserial-1410")
        self.ser.baudrate = 9600
        self.currentColor = -1
        self.currentSaturation = 100
        self.currentBrightness = 1
        self.ser.write('FFE01F')
        self.ser.write('FF00FF')
        self.ser.write('FF00FF')
        self.ser.write('FF00FF')
        self.ser.write('FF00FF')


    def execute(self, variable, value):
        if variable == "on":
            if value == True:
                self.ser.write('FFE01F')
                print("   [*] IRRemote on")
            else:
                self.ser.write('FF609F')
                print("   [*] IRRemote off")
        elif variable == "hue":
            color = int(reMap(int(value), 360, 0, 17, 1))
            if color == self.currentColor or self.currentSaturation < 20:
                print "do nothing"
                return
            elif color == 1:
                #1 under red
                self.ser.write('FF30CF')
            elif color == 2:
                #2 under red
                self.ser.write('FF08F7')
            elif color == 3:
                #3 under red
                self.ser.write('FF28D7')
            elif color == 4:
                #4 under red
                self.ser.write('FF18E7')
            elif color == 5:
                #green
                self.ser.write('FF906F')
            elif color == 6:
                #1 under green
                self.ser.write('FFB04F')
            elif color == 7:
                #2 under green
                self.ser.write('FF8877')
            elif color == 8:
                #3 under green
                self.ser.write('FFA857')
            elif color == 9:
                #4 under green
                self.ser.write('FF9867')
            elif color == 10:
                #blue
                self.ser.write('FF50AF')
            elif color == 11:
                #1 under blue
                self.ser.write('FF708F')
            elif color == 12:
                #2 under blue
                self.ser.write('FF48B7')
            elif color == 13:
                #3 under blue
                self.ser.write('FF6897')
            elif color == 14:
                #4 under blue
                self.ser.write('FF58A7')
            elif color == 15:
                #rot
                self.ser.write('FF10EF')

            self.currentColor = color
            print("   [*] IRRemote color changed")
        elif variable == "saturation":
            if int(value) < 20:
                #weiss
                self.ser.write('FFC03F')
            self.currentSaturation = int(value)
        elif variable == "brightness":
            v = int(value)
            brightness = (int((v+39)/20)-1)
            steps = abs(self.currentBrightness - brightness)
            for i in range(steps):
                if self.currentBrightness > brightness:
                    self.ser.write('FF40BF')
                else:
                    self.ser.write('FF00FF')
            self.currentBrightness = brightness

    def close(self):
        self.ser.close()

def reMap(value, maxInput, minInput, maxOutput, minOutput):

	value = maxInput if value > maxInput else value
	value = minInput if value < minInput else value

	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput

	scaledThrust = float(value - minInput) / float(inputSpan)

	return minOutput + (scaledThrust * outputSpan)
