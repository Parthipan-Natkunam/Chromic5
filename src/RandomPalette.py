import random

class RandomPalette:
    def __init__(self):
        self.RGB =""
        self.C_list = [None]*256
        for C in range(256):
            C_list[C] = C
    #Random Pallette Generator
    def randomcolors(self):
        R = hex(random.choice(C_list))[2:]
        G = hex(random.choice(C_list))[2:]
        B = hex(random.choice(C_list))[2:]
        if(len(R)==1):
            R = "0" + R
        if(len(G)==1):
            G = "0" + G
        if(len(B)==1):
            B = "0" + B
        self.RGB = "#"+R+G+B
        return(self.RGB)
    
    #Grey Pallette Generator
    def greycolors(self):
        R = hex(random.choice(C_list))[2:]
        if(int(R,16)>1):
            G = hex(int(R,16)-2)[2:]
        else:
            G = hex(int(R,16)+2)[2:]
        if(int(G,16)>1):
            B = hex(int(G,16)-2)[2:]
        else:
            B = hex(int(G,16)+2)[2:]
        if(len(R)==1):
            R = "0" + R
        if(len(G)==1):
            G = "0" + G
        if(len(B)==1):
            B = "0" + B
        self.RGB = "#"+R+G+B
        return(self.RGB)
