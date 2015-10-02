#Mapping decimal number to 64-char system
table = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,."

#Convert 3 hexadecimal to 2 64-char
def hex_64(s):
	n = int(s, 16) 			#Convert to decimal
	l = n // 64			#Express the decimal in 64-base system as lr
	r = n % 64
	return dec_64(l) + dec_64(r)	#Convert l and r to char

#Encode a decimal number to 1 64-char
def dec_64(s):
	return table[s]			#look up l and r in table
	
#Decode 2 64-char to 3 hexadecimal
def decode(s):
	dec = table.index(s[0]) * 64 + table.index(s[1])	#Convert to decimal
	return hex(dec)[2:]					#Convert to hexadecimal

#Encode string
def zip(s):
	str = ''
	n = len(s) % 3						#Find out the number to triplets in the string
	if n:
		l = s[:-n]					#Triplets
		r = s[-n:]					#Remainder
	else:
		l = s						
		r = ''
	i = 0
	while i < len(l):
		str += hex_64(s[i : i + 3])			#Convert triplets to 2 * 64-char
		i += 3						
	str += '!' + r						#Append '!' and remainder to the converted triplets
	return str

#Decode string
def unzip(s):
	s = s.split('!')					#Split remainder and converted parts
	i = 0
	str = ''						
	while i < len(s[0]):
		str += decode(s[0][i:i+2])			#Decode encoded body
		i += 2
	str += s[1]
	return str
			
