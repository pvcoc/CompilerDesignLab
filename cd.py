def CheckDivisibilty(A):
	oddbits = 0
	evenbits = 0
	for stringg in range(len(A)):
		if (A[stringg] == '1'):
			if (stringg % 2 == 0):
				evenbits+=1
			else:
				oddbits+=1
	if (abs(oddbits - evenbits) % 3 == 0):
		print("Yes It is Divisibe By 3" + "")
	else:
		print("No IT is Not Divisible By 3" + "")
A = "1010"
CheckDivisibilty(A)
	
