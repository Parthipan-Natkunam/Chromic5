from decimal import Decimal
class HSL2HEX:
    def __init__(self,HSL):
        self.H = HSL[0]
        self.S = HSL[1]
        self.L = HSL[2]
        self.R = 0
        self.G = 0
        self.B = 0
        if(self.S==0):
            self.R = Decimal(self.L*255)
            self.G = Decimal(self.L*255)
            self.B = Decimal(self.L*255)
        else:
            if(self.L<0.5):
                self.temp2 = self.L*(1+self.S)
            else:
                self.temp2 = (self.L+self.S)-(self.S*self.L)
            self.temp1 = 2*self.L - self.temp2
            self.R = Decimal(255*self.HTB(self.temp1,self.temp2,self.H+(1/3)))
            self.G = Decimal(255*self.HTB(self.temp1,self.temp2,self.H))
            self.B = Decimal(255*self.HTB(self.temp1,self.temp2,self.H-(1/3)))
        self.R = int(round(self.R,0))
        self.G = int(round(self.G,0))
        self.B = int(round(self.B,0))
    def HTB(self,t1,t2,h):
        if(h<0):
            h+=1
        if(h>1):
            h-=1
        if((6*h)<1):
            return(t1+(t2-t1)*6*h)
        if((2*h)<1):
            return(t2)
        if((3*h)<2):
            return(t1+(t2-t1)*((2/3)-h)*6)
        return(t1)
    def getHEX(self):
        temp_R = hex(self.R)[2:]
        temp_G = hex(self.G)[2:]
        temp_B = hex(self.B)[2:]
        if(len(temp_R)==1):
            temp_R = "0" + temp_R
        if(len(temp_G)==1):
            temp_G = "0" + temp_G
        if(len(temp_B)==1):
            temp_B = "0" + temp_B
        self.result = "#"+temp_R+temp_G+temp_B
        return(self.result)
