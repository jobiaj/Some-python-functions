def randomGen(start, end):
	from random import randint
	return(randint(int(start), int(end)))
print randomGen(10,20)