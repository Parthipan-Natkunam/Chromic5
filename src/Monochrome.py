import random
from .HEX2HSL import *
from .HSL2HEX import *
class Monochrome:
    
    def monocolors(self,RGB=None,n=None):
        if n is None:
            self.n = 2
        else:
            self.n = n
        if RGB is None:
            self.C_list = [None]*256
            for k in range(256):
                self.C_list[k] = k
            self.R = hex(random.choice(self.C_list))[2:]
            self.G = hex(random.choice(self.C_list))[2:]
            self.B = hex(random.choice(self.C_list))[2:]
            if(len(self.R)==1):
                self.R = "0" + self.R
            if(len(self.G)==1):
                self.G = "0" + self.G
            if(len(self.B)==1):
                self.B = "0" + self.B
            self.RGB = "#"+self.R+self.G+self.B
            HSLdata = HEX2HSL(self.RGB)
            Chromatics = HSLdata.getHSL()
            self.H = Chromatics[0]
            self.S = Chromatics[1]
            self.L = Chromatics[2]
        else:
            self.RGB = RGB
            HSLdata = HEX2HSL(self.RGB)
            Chromatics = HSLdata.getHSL()
            self.H = Chromatics[0]
            self.S = Chromatics[1]
            self.L = Chromatics[2]
        
        final_RGB = [None]*self.n
        for i in range(self.n-1):
            self.L +=0.05
            if (self.L>1):
                self.L-=0.2
            self.S +=0.03
            if(self.S>1):
                self.S-=0.2
            res_HSL = [self.H,self.S,self.L]
            res_RGB = HSL2HEX(res_HSL)
            final_RGB[i] = res_RGB.getHEX()
        final_RGB[self.n-1] = self.RGB
        return(final_RGB)
    
