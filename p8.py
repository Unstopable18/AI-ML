
class LightSwitch():
    def sOn(self):
        self.s=True
    def sOff(self):
        self.s=False
    def sShow(self):
        print(self.s)

#main code
#main code
bulb=input('Enter on or off:\t')
lightBulb=LightSwitch()
if(bulb=='on'):
    lightBulb.sOff()
    lightBulb.sShow()
elif(bulb=='off'):
    lightBulb.sOn()
    lightBulb.sShow()
