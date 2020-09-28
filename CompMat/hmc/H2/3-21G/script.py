import sys
import fileinput
import subprocess
import time

# replace all occurences of 'sit' with 'SIT'
prev = '0.07'
for i in range(31):
	bondLength = 0.70 + 0.01*i
	bondLength = "{}".format(bondLength)
	for j, line in enumerate(fileinput.input('H2.com.tmp', inplace=1)):
		sys.stdout.write(line.replace(prev, bondLength))

	command = 'g16 H2.com.tmp'
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	with open('testdata.txt', 'a') as f:
		with open('H2.com.log', 'r') as my_data_file:
			lines = my_data_file.readlines()
			for i, line in enumerate(lines):
				if i == 358:
					line_len = len(line)
					for j in range(line_len):
						if ord(line[j]) >= 48 and ord(line[j]) <= 57:
							string = line[j:len(line)-1]
							string = string.replace("D", "e")
							f.write(bondLength)
							f.write("\t")
							f.write(string)
							f.write("\n")
							break
					break
	prev = bondLength
