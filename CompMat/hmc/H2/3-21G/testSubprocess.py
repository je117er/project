import subprocess

command = 'g16 H2.com.tmp'
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
		
