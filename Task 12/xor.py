import string

def xor(x):
    return ''.join(chr(ord(i)^(10)) for i in x)

if __name__=="__main__":
    print "Enter what you got after decoding:"

    arr = raw_input()

    your_code = xor(arr) #prints the value after 10 ascii codes

    print your_code