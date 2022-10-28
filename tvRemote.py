from time import sleep

class remote():
    def __init__(self):
        self.power=False
        self.volume=0
        self.mute=True

    def onP(self):
        self.power=True
        print('🟢-Turning TV ON')
        my_str = 'SAMSUNG'
        for char in my_str:
            print(char, end=' ', flush=True)
            sleep(0.5)
        print('')
    
    def offP(self):
        self.power=False
        print('🔴-Turning TV OFF')
    
    def onM(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            self.mute=True
            print('🔇')

    def offM(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            self.mute=False
            print('🔊')

    def inV(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            if(self.mute==True):
                self.mute=False
            if(self.volume<10):
                self.volume+=1
                print(self.volume,'-🔊')

    def deV(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            if(self.volume>=1):
                self.volume-=1
                if(self.volume==0):
                    self.onM()
                else:
                    print(self.volume,'-🔉')
            
            

    def show(self):
        if(self.power==False):
            print('Please turn on TV')
        else:
            print("Power:\t",self.power,'\nVolume:\t',self.volume,'\nMute:\t',self.mute)
r=remote()
r.onP()
r.show()
r.inV()
r.inV()
r.show()
r.deV()
r.show()
r.deV()
r.deV()
r.deV()
r.show()




