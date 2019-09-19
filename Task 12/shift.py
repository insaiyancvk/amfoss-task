import string


def shift(x):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    n = []
    for i in x:
        if i.isupper() is True:
            n.append(upper[(upper.index(i)-3)%26])
        elif i.islower() is True:
            n.append(lower[(lower.index(i)-3)%26])
        elif i.isdigit() is True:
            n.append(digits[(digits.index(i)-3)%10])
    return n

#def xor(x):
 #   return ''.join(chr(ord(i)^(10)) for i in x)


if __name__=="__main__":
    print "Enter what you got after decoding:"

    arr = raw_input()

    your_code = shift(arr) # increasses the input value by 3
    print your_code