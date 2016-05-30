
class HEX2HSL:
    def __init__(self,RGB):
        self.RGB = RGB
        self.R = int((self.RGB[1:3]),16)
        self.G = int((self.RGB[3:5]),16)
        self.B = int((self.RGB[5:7]),16)
        self.H = 0;
        self.S = 0;
        self.L = 0;
        R = (self.R/255)
        G = (self.G/255)
        B = (self.B/255)
        minVar = min(R,G,B)
        maxVar = max(R,G,B)
        delta = maxVar - minVar
        self.L = (minVar+maxVar)/2
        if(delta==0):
            self.H = 0
            self.S = 0
        else:
            if(self.L<0.5):
                self.S = delta/(maxVar+minVar)
            else:
                self.S = delta/(2-maxVar-minVar)
            mid_R = (((maxVar-R)/6)+(delta/2))/delta
            mid_G = (((maxVar-G)/6)+(delta/2))/delta
            mid_B = (((maxVar-B)/6)+(delta/2))/delta
            if(R==maxVar):
                self.H = mid_B-mid_G
            elif(G==maxVar):
                self.H = (1/3)+mid_R-mid_B
            elif(B==maxVar):
                self.H = (2/3)+mid_G-mid_R
            if(self.H<0):
                self.H += 1
            if(self.H>1):
                self.H -= 1
    def getHSL(self):
        self.HSL = [self.H,self.S,self.L]
        return(self.HSL)
        
            
            
