with open('data', 'w') as f:
	with open('H2.com.log', 'r') as my_data_file:
		lines = my_data_file.readlines()
		energies = []
		for i, line in enumerate(lines):
			if i == 358:
				line_len = len(line)
				for j in range(line_len):
					if ord(line[j]) >= 48 and ord(line[j]) <= 57:
						string = line[j:len(line)-1]
						string = string.replace("D", "e")
						f.write(string)
						f.write("\n")
						break
				break
				
