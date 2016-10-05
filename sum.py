with open ('/home/sum.txt','r') as f :
	data = f.readlines()
	for line in data:
		num = line.split()
		numbers_int = map(int, num)
		print numbers_int
		print sum(numbers_int)
		write_str = '%d'%(sum(numbers_int))
	f.close()
	with open ('/home/sum1.txt','a') as f1:  
		f1.write(write_str)
		f1.close()
