from os import urandom
from ctypes import CDLL
import string
import hashlib

key = ""
ciphertext = ""

def get_key():
    global key
    c = urandom(1)
    #print(c)
    if len(key)!=5: # stops if length of the key is 5
        if c not in string.ascii_lowercase and c not in string.ascii_uppercase :
            get_key() #works like a loop
            
        else:
            key += c # adding ramdomly generated uppercase or lower case letters to a string variable
            get_key() #loop.
            #print "Key : ",key
            #print ord(c)
    
def xor_encrypt(x):
    global key
    global ciphertext
    get_key()
    print "Key : ",key
    hex_key = key.encode("hex") # Converting key to hex and storing in a variable
    print "Hex Key : ",hex_key
    key_list = [hex_key[i]+hex_key[i+1] for i in range(0,len(hex_key),2)] # Making an array of hex encoded key 
    print "Key List : ",key_list
    for i in xrange(len(x)): # x used here for it's length
        ciphertext += chr(ord(x[i]) ^ int(key_list[i%5], 16))

    
if __name__ == "__main__":
    #plaintext = input("Enter the plaintext to be encrypted: ")
    plaintext = ""
    xor_encrypt(plaintext)
    print ("Ciphertext : ",ciphertext)
    if hashlib.md5(plaintext).digest().encode("hex") == "067abbb88d2201a393ba660728f83b84":
        print "Yeah!....You are a genius!"
    else:
        xor_encrypt(plaintext)
    #print "Encoded Ciphertext : ",ciphertext.encode("hex")
    #print "Encoded Ciphertext : ",ciphertext.decode("hex")  Doesn't work.