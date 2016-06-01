import random
from .HEX2HSL import *
from .HSL2HEX import *
class ColorHarmony:
    def __init__(self):
        self.H = 0
        self.S = 0
        self.L = 0
    def beginColoring(self,RGB=None):
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
        else:
            self.RGB = RGB
    def analogus(self,RGB=None,n=None):
        if n is None:
            self.n = 2
        else:
            self.n = n
        if RGB is None:
            self.beginColoring()
        else:
            self.beginColoring(RGB)
        HSLdata = HEX2HSL(self.RGB)
        Chromatics = HSLdata.getHSL()
        self.H = Chromatics[0]
        self.S = Chromatics[1]
        self.L = Chromatics[2]
        final_RGB = [None]*self.n
        for i in range(self.n-1):
            self.H += 0.08
            self.L += ((random.randint(0,100))/100)
            if(self.H>1):
                self.H-=1
            if(self.L>1):
                self.L-=1
            res_HSL = [self.H,self.S,self.L]
            res_RGB = HSL2HEX(res_HSL)
            final_RGB[i] = res_RGB.getHEX()
        final_RGB[self.n-1]=self.RGB
        return(final_RGB)
    def compliment(self,RGB=None):
        if RGB is None:
            self.beginColoring()
        else:
            self.beginColoring(RGB)
        self.n = 2
        HSLdata = HEX2HSL(self.RGB)
        Chromatics = HSLdata.getHSL()
        self.H = Chromatics[0]
        self.S = Chromatics[1]
        self.L = Chromatics[2]
        final_RGB = [None]*self.n
        for i in range(self.n-1):
            self.H += 0.5
            self.L += ((random.randint(0,100))/100)
            if(self.H>1):
                self.H-=1
            if(self.L>1):
                self.L-=1
            res_HSL = [self.H,self.S,self.L]
            res_RGB = HSL2HEX(res_HSL)
            final_RGB[i] = res_RGB.getHEX()
        final_RGB[self.n-1]=self.RGB
        return(final_RGB)
    def splitcompliments(self,RGB=None):
        if RGB is None:
            self.beginColoring()
        else:
            self.beginColoring(RGB)
        self.n = 3
        HSLdata = HEX2HSL(self.RGB)
        Chromatics = HSLdata.getHSL()
        self.H = Chromatics[0]
        self.S = Chromatics[1]
        self.L = Chromatics[2]
        final_RGB = [None]*self.n
        for i in range(self.n-1):
            self.H+=0.4166666666667
            self.L += ((random.randint(0,100))/100)
            if(self.H>1):
                self.H-=1
            if(self.L>1):
                self.L-=1
            res_HSL = [self.H,self.S,self.L]
            res_RGB = HSL2HEX(res_HSL)
            final_RGB[i] = res_RGB.getHEX()
        final_RGB[self.n-1]=self.RGB
        return(final_RGB)
    def triadic(self,RGB=None):
        if RGB is None:
            self.beginColoring()
        else:
            self.beginColoring(RGB)
        self.n = 3
        HSLdata = HEX2HSL(self.RGB)
        Chromatics = HSLdata.getHSL()
        self.H = Chromatics[0]
        self.S = Chromatics[1]
        self.L = Chromatics[2]
        final_RGB = [None]*self.n
        for i in range(self.n-1):
            self.H+=0.3333
            self.L += ((random.randint(0,100))/100)
            if(self.H>1):
                self.H-=1
            if(self.L>1):
                self.L-=1
            res_HSL = [self.H,self.S,self.L]
            res_RGB = HSL2HEX(res_HSL)
            final_RGB[i] = res_RGB.getHEX()
        final_RGB[self.n-1]=self.RGB
        return(final_RGB)

    
