PI1 = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]
PI2=[27, 18, 13, 21, 19, 7, 28, 31, 26, 15, 32, 24, 3, 4, 22, 1, 11, 30, 5, 6, 25, 12, 20, 16, 10, 14, 17, 8, 9, 23, 29, 2]
PI3=[29,116,91,22,9,61,101,92,37,98,1,109,5,125,73,10,77,7,120,16,114,72,51,111,127,75,13,2,97,110,49,52,123,121,108,40,45,70,99,85,90,34,124,47,119,118,96,94,112,107,31,126,81,115,105,17,88,68,74,103,102,59,79,57,128,28,86,93,66,83,104,117,21,60,19,106,58,71,89,84,53,26,95,55,46,62,80,20,44,78,35,42,67,82,48,4,64,43,38,100,56,54,32,69,87,25,15,30,76,65,36,24,41,63,23,50,18,33,14,12,27,113,39,122,6,11,3,8]
PI=PI3

CP_11 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
CP_12 = [12,5,6,19,20,3,30,4,26,25,31,22,23,18,21,15,14,28,1,13,27,17,10,7,11,9,2,29]
CP_13 = [37,43,1,107,13,82,21,121,11,10,77,47,103,85,79,116,4,65,27,22,101,71,25,34,57,55,126,84,108,106,81,124,98,36,49,110,19,35,42,92,20,41,90,94,89,105,125,7,5,53,3,100,97,102,74,99,62,111,69,93,122,118,87,46,29,113,60,95,78,68,75,63,54,52,33,86,70,123,45,117,73,67,66,51,127,76,50,58,91,39,23,30,31,28,59,26,17,119,61,115,18,38,14,44,15,12,9,2,6,109,114,83]
CP_1=CP_13


CP_21 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]
CP_22 = [24,1,20,10,4,3,6,25,26,22,21,14,28,18,15,7,16,19,17,27,12,23,8,5]
CP_23 = [78,1,94,50,10,23,66,64,14,103,4,32,34,28,22,39,46,79,80,25,96,111,105,33,6,58,99,102,98,38,70,108,104,112,40,109,84,100,83,74,92,77,90,72,73,68,86,110,65,91,56,97,75,9,87,76,57,61,81,13,82,85,60,62,69,89,48,19,88,106,49,29,52,63,42,55,54,41,51,43,95,93,71,35,67,36,101,59,47,107,44,37,26,3,27,30,20,17,8,21,18,24,15,53,11,31,12,16,2,7,5,45]
CP_2=CP_23

#expansion boxes

E1 = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]
E2 = [16, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 1]
E3 = [64,1,2,3,4,5,
4,5,6,7,8,9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,33,
32,33,34,35,36,37,
36,37,38,39,40,41,
40,41,42,43,44,45,
44,45,46,47,48,49,
48,49,50,51,52,53,
52,53,54,55,56,57,
56,57,58,59,60,61,
60,61,62,63,64,1]
E=E3

#s-boxes

S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
],

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
],

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
],
   [[12, 7, 10, 13, 0, 11, 6, 1, 15, 2, 9, 4, 3, 8, 5, 14],
 [0, 6, 13, 3, 10, 9, 7, 12, 14, 8, 11, 5, 4, 2, 1, 15],
 [7, 1, 9, 14, 4, 2, 10, 13, 12, 6, 3, 8, 15, 5, 0, 11],
 [11, 12, 7, 0, 2, 15, 14, 5, 1, 10, 13, 3, 8, 6, 4, 9]],
   
[[0, 10, 7, 4, 12, 3, 11, 13, 14, 1, 9, 15, 5, 6, 2, 8],
 [9, 0, 5, 12, 2, 11, 14, 7, 10, 15, 6, 1, 13, 8, 3, 4],
 [7, 14, 11, 1, 8, 13, 2, 4, 0, 9, 12, 6, 15, 10, 5, 3],
 [6, 3, 9, 10, 5, 15, 12, 0, 8, 4, 2, 13, 14, 1, 11, 7]],
   
[[0, 10, 11, 13, 6, 1, 12, 7, 5, 9, 8, 2, 3, 14, 15, 4],
 [2, 11, 8, 14, 7, 13, 4, 1, 12, 6, 5, 9, 0, 10, 3, 15],
 [15, 6, 12, 10, 3, 9, 0, 5, 4, 11, 7, 1, 13, 2, 14, 8],
 [12, 9, 6, 5, 10, 0, 3, 14, 7, 4, 11, 8, 1, 15, 13, 2]],
   
   
[[1, 15, 13, 6, 7, 9, 14, 0, 11, 12, 8, 3, 4, 10, 2, 5],
 [8, 4, 7, 1, 13, 2, 11, 14, 5, 3, 9, 12, 10, 15, 6, 0],
 [2, 5, 8, 15, 11, 0, 13, 3, 4, 10, 1, 6, 14, 9, 7, 12],
 [9, 2, 3, 13, 12, 7, 15, 4, 10, 1, 6, 11, 0, 14, 5, 8]],
   
[[11, 6, 12, 10, 1, 13, 7, 0, 14, 9, 2, 5, 8, 3, 4, 15],
 [14, 1, 5, 15, 0, 10, 3, 12, 11, 4, 8, 2, 13, 7, 6, 9],
 [4, 9, 8, 3, 13, 6, 14, 5, 2, 15, 7, 12, 1, 10, 11, 0],
 [10, 12, 0, 9, 3, 5, 15, 6, 13, 7, 11, 4, 14, 2, 1, 8]],
   
[[9, 2, 6, 12, 5, 11, 15, 1, 14, 7, 3, 0, 8, 13, 4, 10],
 [5, 6, 0, 15, 3, 9, 12, 10, 8, 11, 14, 1, 13, 4, 2, 7],
 [14, 4, 2, 11, 8, 1, 7, 13, 0, 3, 9, 12, 5, 15, 10, 6],
 [0, 12, 10, 1, 7, 2, 9, 15, 13, 6, 4, 11, 14, 8, 3, 5]],
   
   
[[15, 6, 12, 3, 1, 13, 10, 0, 9, 5, 7, 8, 2, 14, 4, 11],
 [14, 7, 0, 9, 11, 12, 5, 2, 4, 8, 13, 3, 1, 6, 10, 15],
 [4, 11, 8, 13, 15, 6, 2, 1, 14, 7, 3, 10, 5, 0, 9, 12],
 [12, 3, 2, 15, 7, 4, 9, 10, 0, 13, 11, 1, 14, 8, 5, 6]],
 
[[3, 11, 8, 5, 13, 0, 14, 6, 1, 15, 4, 10, 2, 12, 7, 9],
 [9, 2, 3, 13, 5, 8, 10, 14, 6, 7, 0, 11, 15, 4, 12, 1],
 [11, 6, 7, 3, 4, 5, 13, 15, 14, 10, 2, 9, 8, 0, 1, 12],
 [14, 1, 13, 6, 3, 10, 4, 12, 15, 2, 9, 8, 5, 11, 0, 7]],
 
]

#p-boxes

P1 = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]
P2 = [12,3,4,2,16,1,8,9,14,10,6,15,7,5,13,11]
P3 = [56 ,37 ,30 ,61 ,4 ,55 ,10 ,52 ,16 ,9 ,58 ,7 ,36 ,34 ,51 ,23 ,40 ,64 ,42 ,19 ,20 ,45 ,47 ,17 ,24 ,54 ,14 ,49 ,28 ,59 ,50 ,31 ,48 ,62 ,60 ,39 ,46 ,29 ,27 ,35 ,57 ,43 ,44 ,32 ,33 ,38 ,26 ,41 ,8 ,22 ,2 ,18 ,15 ,25 ,12 ,1 ,21 ,63 ,13 ,6 ,5 ,11 ,53 ,3]
P=P3

PI_11 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
PI_12 = [16, 32, 13, 14, 19, 20, 6, 28, 29, 25, 17, 22, 3, 26, 10, 24, 27, 2, 5, 23, 4, 15, 30, 12, 21, 9, 1, 7, 31, 18, 8, 11]
PI_13 = [11, 28, 127, 96, 13, 125, 18, 128, 5, 16, 126, 120, 27, 119, 107, 20, 56, 117, 75, 88, 73, 4, 115, 112, 106, 82, 121, 66, 1, 108, 51, 103, 118, 42, 91, 111, 9, 99, 123, 36, 113, 92, 98, 89, 37, 85, 44, 95, 31, 116, 23, 32, 81, 102, 84, 101, 64, 77, 62, 74, 6, 86, 114, 97, 110, 69, 93, 58, 104, 38, 78, 22, 15, 59, 26, 109, 17, 90, 63, 87, 53, 94, 70, 80, 40, 67, 105, 57, 79, 41, 3, 8, 68, 48, 83, 47, 29, 10, 39, 100, 7, 61, 60, 71, 55, 76, 50, 35, 12, 30, 24, 49, 122, 21, 54, 2, 72, 46, 45, 19, 34, 124, 33, 43, 14, 52, 25, 65]
PI_1 = PI_13
accum=[]
acc=[]

#left shift for sub key generation

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]



def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)
        array.extend([int(x) for x in list(binval)])
    return array

def bit_array_to_string(array):
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in  nsplit(array,8)]])  
    return res

def binvalue(val, bitsize):  
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval
    return binval

def nsplit(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

ENCRYPT=1
DECRYPT=0

class des():
    global roun
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()
     
    #encryption
   
    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < kinw:
            raise "Key Should be 8 bytes long"
        elif len(key) > kinw:
            key = key[:kinw]
        lx = len(text)
        if (lx%kinw)!=0 :
            for i in range(0,kinw-lx%kinw) :
                text=text+" "
        self.password = key
        self.text = text
   
       
        if padding and action==ENCRYPT:
            self.addPadding()
        elif len(self.text) % kinw != 0:
            raise "Data size should be multiple of 8"
       
        self.generatekeys()
        text_blocks = nsplit(self.text, kinw)
       
       
        result = list()
       
        for block in text_blocks:
            acc.clear()
            for i in range(0,roun+1):
                acc.append([])
            #print("input block is "+str(block))
            #print("printing blocks of text :"+str(block)+"\n")
            block = string_to_bit_array(block)#Convert the block in bit array
            acc[0]=block
            block = self.permut(block,PI)
            g, d = nsplit(block, w)
            tmp = None
            #print("running for roun value"+str(roun))
            for i in range(0,roun):
              #  print("the round number is "+str(i))
                d_e = self.expand(d, E)
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d_e)
                else:
                    tmp = self.xor(self.keys[roun-1-i], d_e)
                tmp = self.substitute(tmp)
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
                acc[i+1]=self.permut(d+g, PI_1)
               # print(str(i)+" acci"+str(acc[i]))
           
            result += self.permut(d+g, PI_1)
        final_res = bit_array_to_string(result)
        if padding and action==DECRYPT:
            return self.removePadding(final_res)
        else:
            return final_res
   
    #basic fiestal structure implementation
   
    def substitute(self, d_e):
        subblocks = nsplit(d_e, 6)
        result = list()
        for i in range(len(subblocks)):
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2)
            column = int(''.join([str(x) for x in block[1:][:-1]]),2)
            val = S_BOX[i][row][column]
            bin = binvalue(val, 4)
            result += [int(x) for x in bin]
        return result
   
    #round function for multiple rounds
   
    def permut(self, block, table):#Permut the given block using the given table (so generic method)
        return [block[x-1] for x in table]
   
    def expand(self, block, table):#Do the exact same thing than permut but for more clarity has been renamed
        return [block[x-1] for x in table]
   
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x^y for x,y in zip(t1,t2)]
   
    def generatekeys(self):#Algorithm that generates all the keys
        self.keys = []
        key = string_to_bit_array(self.password)
        #print("key:"+str(len(key))+"  "+str(key)+"\n")
        key = self.permut(key, CP_1)
        g, d = nsplit(key, kfrh)
        for i in range(roun):
            g, d = self.shift(g, d, SHIFT[i])
            tmp = g + d
            self.keys.append(self.permut(tmp, CP_2))
     

    def shift(self, g, d, n):
        return g[n:] + g[:n], d[n:] + d[:n]
   
    def addPadding(self):
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)
   
    def removePadding(self, data):
        pad_len = ord(data[-1])
        return data[:-pad_len]
   
    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)
   
    #decrption
   
    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)
   

d = des()






import numpy as np

#graph for avalanche

import matplotlib.pyplot as plt
def diff(row1,row0):
    sum=0
    for f in range(0,len(row1)):
        sum=sum+abs(row1[f]-row0[f])
    return sum

#function for avalanche effect

def avalanche(roune,text,key,twow):
    arrin=string_to_bit_array(text)
    d=des()
    global accum
    global roun
   
   
   
     
   
    accum=np.zeros((twow+1,roune+1,twow))
  #  print(accum.shape)
    accum[0][0]=arrin
    for r in range(1,roune+1):
           
            roun=r
            rounvalue=d.encrypt(key,bit_array_to_string(arrin))
            accum[0][r] =(string_to_bit_array(rounvalue))
   
   
    for f in range(0,twow):
     
        arrin[f]=1-arrin[f]
        accum[f+1]=arrin
       
        for r in range(1,roune+1):
           
            roun=r
       
           
            rounvalue=d.encrypt(key,bit_array_to_string(arrin))
            accum[f+1][r]=(string_to_bit_array(rounvalue))
           # print(d.decrypt(key,d.encrypt(key,bit_array_to_string(arrin))))
           # print(bit_array_to_string(arrin))
            #print("rewwwffffffffffffffffffffff")
       
        arrin[f]=1-arrin[f]
   
  #  print(accum.shape)
    hero = np.zeros((twow+1,roun+1))

    for sample in range(0,twow+1):
          for row in range(0,roun+1):
       
               x=diff(accum[sample][row],accum[0][row])
               hero[sample][row]=x
       

    hero1 = np.delete(hero, (0), axis=0)

    av=np.mean(hero1, axis = 0)
    x = []
    for g1 in range(0,roun+1):
        x.append(g1)
    print(av)
    y = av.tolist()
   
    #avalanche plots with hamming distance
 
    plt.plot(x, y)
 

    plt.xlabel('rounds')
 
    plt.ylabel('Hamming Distance')
 
 
    plt.title('Avalanche')
    plt.show()
     
    return av
   
   

#avalanche(roun,text,key,twow)
def string_to_freqlist(tex):
    lis=np.zeros((256))
   
    for char in tex:
        ba=string_to_bit_array(char)
        res = int("".join(str(x) for x in ba), 2)
        lis[res]=lis[res]+1
    return lis

#function for frequency plots

def frequency(ro,te,ke):
    frew=np.zeros((ro+1,256))
    frew[0]=string_to_freqlist(te)
    global roun
    d=des()
    for ri in range(1,ro+1):
        roun=ri
        frew[ri]=string_to_freqlist(d.encrypt( ke, te))
    lis=np.arange(256)
   
    for ill in range(0,ro+1):
        plt.figure(ill+1)
        li = lis
        y = frew[ill]
        print("ooooooo")
        print(y.shape)
        plt.plot(li,y)
        plt.show()
   
   
    return
   



import tkinter as tk

from tkinter import *
def show():
    f1=fu.get()
    if f1==1:
        outext.delete(0.0,END)
        i=intext.get("0.0",END)
        st=""
        for char in i:
            ch=char
            if char>='a' and char<='z':
                ch=chr(ord('z')-ord(char)+ord('a'))
            elif char>='A' and char<='Z':
                ch=chr(ord('Z')-ord(char)+ord('A'))
            elif char>='0' and char<='9':
                ch=chr(ord('9')-ord(char)+ord('0'))
       
            st=st+ch
        outext.insert(0.0,st)
    elif f1==2:
        intext.delete(0.0,END)
        i=outext.get("0.0",END)
        st=""
        for char in i:
            ch=char
            if char>='a' and char<='z':
                ch=chr(ord('z')-ord(char)+ord('a'))
            elif char>='A' and char<='Z':
                ch=chr(ord('Z')-ord(char)+ord('A'))
            elif char>='0' and char<='9':
                ch=chr(ord('9')-ord(char)+ord('0'))
       
            st=st+ch
        intext.insert(0.0,st)
def encry():
    #encryption
    wid=fu.get()
    rs=roundbox.get("0.0",END)
    ro = int(rs)
    global w
    w=int(wid/2)
    global PI
    global PI1
    global PI3
       
    global P
    global P3
    global E
    global E3
    global CP_2
    global CP_23
    global CP_1
    global CP_13
    global PI_1
    if w==64:
        PI=PI3
        PI_1 = PI_13
        P=P3
        E=E3
        CP_2=CP_23
        CP_1=CP_13
    elif w==16:
        PI=PI2
        PI_1 = PI_12
        P=P2
        E=E2
        CP_2=CP_22
        CP_1=CP_12
       
    elif w==32:
        PI=PI1
        PI_1 = PI_11
        P=P1
        E=E1
        CP_2=CP_21
        CP_1=CP_11
       
    global roun
    roun=ro
    print("roun is"+str(roun))
   
   
    global twow
    twow=2*w
    global k
    k=2*w
    global kinw
    kinw=int(k/8)
    global kfr
    kfr=int((k*7)/8)
    global kfrh
    kfrh=int(kfr/2)
   
    outext.delete(0.0,END)
    i=intext.get("0.0",END)
    i=i[:-1]
    ke=keybox.get("0.0",END)
    ke=ke[:-1]
    d=des()
    print("8888888888888")
    print(len(i))
    outi=d.encrypt(ke,i)
    print("output block is"+str(outi))
    print(len(outi))
    print("8888888888888")
   
    outext.insert(0.0,outi)
 


def decry():
    #decryption function
    wid=fu.get()
    rs=roundbox.get("0.0",END)
    ro = int(rs)
    global w
    w=int(wid/2)
    global PI
    global PI1
    global PI3
       
    global P
    global P3
    global E
    global E3
    global CP_2
    global CP_23
    global CP_1
    global CP_13
    global PI_1
    if w==64:
        PI=PI3
        PI_1 = PI_13
        P=P3
        E=E3
        CP_2=CP_23
        CP_1=CP_13
    elif w==16:
        PI=PI2
        PI_1 = PI_12
        P=P2
        E=E2
        CP_2=CP_22
        CP_1=CP_12
        print(CP_1)
    elif w==32:
        PI=PI1
        PI_1 = PI_11
        P=P1
        E=E1
        CP_2=CP_21
        CP_1=CP_11
        print(PI)
    global roun
    roun=ro
    print("roun is"+str(roun))
   
   
    global twow
    twow=2*w
    global k
    k=2*w
    global kinw
    kinw=int(k/8)
    global kfr
    kfr=int((k*7)/8)
    global kfrh
    kfrh=int(kfr/2)
   
    outext.delete(0.0,END)
    i=intext.get("0.0",END)
    i=i[:-1]
    ke=keybox.get("0.0",END)
    ke=ke[:-1]
    d=des()
    print("8888888888888")
    print(len(i))
    outi=d.decrypt(ke,i)
    print(len(outi))
    print("8888888888888")
   
    outext.insert(0.0,outi)

#avalanche function

def ava():
    wid=fu.get()
    rs=roundbox.get("0.0",END)
    ro = int(rs)
    global w
    w=int(wid/2)
    global PI
    global PI1
    global PI3
       
    global P
    global P3
    global E
    global E3
    global CP_2
    global CP_23
    global CP_1
    global CP_13
    global PI_1
    if w==64:
        PI=PI3
        PI_1 = PI_13
        P=P3
        E=E3
        CP_2=CP_23
        CP_1=CP_13
    elif w==16:
        PI=PI2
        PI_1 = PI_12
        P=P2
        E=E2
        CP_2=CP_22
        CP_1=CP_12
        print(CP_1)
    elif w==32:
        PI=PI1
        PI_1 = PI_11
        P=P1
        E=E1
        CP_2=CP_21
        CP_1=CP_11
        print(PI)
    global roun
    roun=ro
    print("roun is"+str(roun))
   
   
    global twow
    twow=2*w
    global k
    k=2*w
    global kinw
    kinw=int(k/8)
    global kfr
    kfr=int((k*7)/8)
    global kfrh
    kfrh=int(kfr/2)
   
    outext.delete(0.0,END)
    i=intext.get("0.0",END)
    i=i[:-1]
    ke=keybox.get("0.0",END)
    ke=ke[:-1]
    d=des()
    av=avalanche(roun,i,ke,twow)
    print("av is:"+str(av))
    outi=str(av)
    outext.insert(0.0,outi)
   
#function of frequency

def free():
    wid=fu.get()
    rs=roundbox.get("0.0",END)
    ro = int(rs)
    global w
    w=int(wid/2)
    global PI
    global PI1
    global PI3
       
    global P
    global P3
    global E
    global E3
    global CP_2
    global CP_23
    global CP_1
    global CP_13
    global PI_1
    if w==64:
        PI=PI3
        PI_1 = PI_13
        P=P3
        E=E3
        CP_2=CP_23
        CP_1=CP_13
    elif w==16:
        PI=PI2
        PI_1 = PI_12
        P=P2
        E=E2
        CP_2=CP_22
        CP_1=CP_12
       # print(CP_1)
    elif w==32:
        PI=PI1
        PI_1 = PI_11
        P=P1
        E=E1
        CP_2=CP_21
        CP_1=CP_11
      #  print(PI)
    global roun
    roun=ro
    global twow
    twow=2*w
    global k
    k=2*w
    global kinw
    kinw=int(k/8)
    global kfr
    kfr=int((k*7)/8)
    global kfrh
    kfrh=int(kfr/2)
    outext.delete(0.0,END)
    i=intext.get("0.0",END)
    i=i[:-1]
    ke=keybox.get("0.0",END)
    ke=ke[:-1]
    d=des()
    frequency(ro,i,ke)
    return
   
 

m = tk.Tk(screenName=None,  baseName=None,  className='Crpyter',  useTk=1)

#basic user interface is implemented by tkinter
# using tkinter module for user interface , so we have to import the tkinter module
#Python offers multiple options for developing GUI (Graphical User Interface).
#Out of all the GUI methods, tkinter is the most commonly used method.
#It is a standard Python interface to the Tk GUI toolkit shipped with Python.
#Python with tkinter is the fastest and easiest way to create the GUI applications.

#To create a tkinter app:

#                        1)Import the module – tkinter
#                        2)Create the main window (container)
#                        3)Add any number of widgets to the main window
#                        4)Apply the event Trigger on the widgets.
 

l1=Label(m, text="INPUT",fg='red')
l2=Label(m,text="OUTPUT",fg='red')
l3=Label(m,text="width : ")
l4=Label(m,text="number of rounds : ")
l5=Label(m,text="key : ")
l6=Label(m,text="Note : for avalanche use 64 as the width")

l1.grid(row=6,column=0)
l2.grid(row=6,column=2)
l3.grid(row=0,column=1)
l4.grid(row=2,column=1)
l5.grid(row=4,column=1)
l6.grid(row=6,column=1)

fu=IntVar()
rd1=Radiobutton(m,text="32",variable=fu,value=32)
rd2=Radiobutton(m,text="64",variable=fu,value=64)
rd3=Radiobutton(m,text="128",variable=fu,value=128)

rd1.grid(row=1,column=0)
rd2.grid(row=1,column=1)
rd3.grid(row=1,column=2)
d = des()

intext=Text(m,width=30,height=20,wrap=WORD)
keybox=Text(m,width=20,height=5,wrap=WORD)
roundbox=Text(m,width=3,height=1,wrap=WORD)
intext.grid(row=7,column=0)
roundbox.grid(row=3,column=1)
keybox.grid(row=5,column=1)
outext=Text(m,width=30,height=20,wrap=WORD)
outext.grid(row=7,column=2)
act1=Button(m,text="encrypt",command=encry,bg='red')
act2=Button(m,text="decrypt",command=decry,bg='green')
act3=Button(m,text="Avalanche",command=ava,bg='blue')
act4=Button(m,text="Frequency plot",command=free,bg='yellow')
act1.grid(row=8,column=0)
act2.grid(row=8,column=1)
act3.grid(row=8,column=2)
act4.grid(row=8,column=3)
m.mainloop()