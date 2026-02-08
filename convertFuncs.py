import math
import conv

def convert_binary(x):
    y=""
    p=int(math.log(x,2))
    for i in range(p,-1,-1):
        if x>=2**i:
            y+="1"
            x-=2**i
        else:
            y+="0"
    return y
def convert_octal(x):
    y=""
    p=int(math.log(x,8))
    for i in range(p,-1,-1):
        if x>=8**i:
            y+=str(x//(8**i))
            x-=x//(8**i)*8**i
        else:
            y+="0"
    return y

def convert_hexadecimal(x):
    y=""
    p=int(math.log(x,16))
    for i in range(p,-1,-1):
        if x>=16**i:
            if x//(16**i)<10:
                y+=str(x//(16**i))
            else:
                y+=chr(x//(16**i)-10+ord('A'))
            x-=x//(16**i)*16**i
        else:
            y+="0"
    return y