import string

def decode(x):
    return x.decode('hex') 

if __name__=="__main__":
    
    print "Enter what you got after decoding:"

    arr = raw_input()

    your_code = decode(arr)

    print your_code