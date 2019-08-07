from PIL import Image
import pytesseract
cap = Image.open("captcha.png")
theString = pytesseract.image_to_string(cap)
z = str(theString)
e = z.replace(' ','')
l = len(e)
p = e.find("+")
s = e.find("-")
pr = e.find("x")
pr1 = e.find("*")
qu = e.find("/")
if e[p]=="+":
	v1 = int(e[0:p])
	v2 = int(e[(p+1):(l)])
	print (v1+v2)
elif e[s]=="-":
	v1 = int(e[0:s])
	v2 = int(e[(s+1):(l)])
	print (v1-v2)
elif e[pr]=="x" :
	v1 = int(e[0:pr])
	v2 = int(e[(pr+1):(l)])
	print (v1*v2)
elif e[pr1]=="*":
	v1 = int(e[0:pr1])
	v2 = int(e[(pr1+1):(l)])
	print (v1*v2)	
elif e[qu]=="/":
	v1 = int(e[0:qu])
	v2 = int(e[(qu+1):(l)])
	print(v1/v2)