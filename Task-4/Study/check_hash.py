import hashlib
flag = raw_input("Enter the flag you have got : ")
#flag = "232e0c4133152c090d350e241d41311e37180f331f2559193f08"
# flag = "You completed the Advanced XOR"
if hashlib.md5(flag).digest().encode("hex") == "067abbb88d2201a393ba660728f83b84":
    print "Yeah!....You are a genius!"
else:
    print "Oops! Sorry your flag is not correct!"
    print "Check the source code of the encrypting script again"
