import subprocess
import sys
import fileinput

# For c6h6, homo and lumo are at orbital 21 and 22, respectively
# in the case of c10h8, they are at orbital 34 and 35, respectively
molecule = 'C10H8'
orbitals = {34: "HOMO", 35:"LUMO"}
for key, value in orbitals.items():
        for i in range(5):
                if key == 34: level = key - i
                else: level = key + i
                command = 'cubegen 0' + ' MO=' + str(level) + ' ' + molecule + '.fchk ' + molecule + '_' + value + '_' + str(i) + '.cub'
                print(command)
                process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
                output, error = process.communicate()

