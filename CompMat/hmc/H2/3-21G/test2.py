with open('test.txt', 'w') as f:
	for i in range(10):
		string = "{}".format(i)
		string += " "
		f.write(string)
		f.write(string)
		f.write('\n')

