str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str = str.split()

dict = {}
single = [0, 4, 5, 6, 7, 8, 14, 15, 18]
for i in range(len(str)):
	clen = 1 if i in single else 2
	dict[str[i][:clen]] = i + 1