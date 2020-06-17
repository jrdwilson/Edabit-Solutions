#Three different ways of solving the hamming problem
def hamming_distance(txt1, txt2):
	return sum(x!=y for (x,y) in zip(txt1,txt2))

def hamming_distance(txt1, txt2):
    return len([1 for ch1, ch2 in zip(txt1, txt2) if ch1 != ch2])

def hamming_distance(txt1, txt2):
	count = 0
	for i in range (len(txt1)):
		if (txt1[i]!=txt2[i]):
			count+=1
	return count
