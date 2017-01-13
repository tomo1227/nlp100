def cipher(input):
	a=""
	for i in str:
		a += chr(219-ord(i)) if i.islower() else i
	return a
		
str = "Atbash is a simple substitution cipher for the Hebrew alphabet."
str = cipher(str)
print (str)
str = cipher(str)
print (str)