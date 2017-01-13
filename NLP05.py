def ngram(input, n):
	print(input)
	last = len(input) - n + 1
	ret = []
	for i in range(0, last):
		ret.append(input[i : i + n])
	return ret
	
str = "I am an NLPer"
print (ngram(str,2))