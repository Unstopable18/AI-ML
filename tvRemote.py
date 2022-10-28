from operator import truediv
from time import sleep
class remote():
    def __init__(self):
        self.power=False
        self.volume=0
        self.mute=False

    def onP(self):
        sleep()
        self.power=True
    
    def offP(self):
        self.power=False
    
    def onM(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            self.mute=True

    def offM(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            self.mute=False

    def inV(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            if(self.mute==False):
                self.offM()
            if(self.volume<10):
                self.volume+=1

    def deV(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            if(self.volume>0):
                self.volume-=1

    def show(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            print("Power:\t",self.power,'\nVolume:\t',self.volume,'\nMute:\t',self.mute)
r=remote()
r.show()
r.inV()
r.onP()
r.inV()
r.inV()
r.show()
r.deV()
r.show()


