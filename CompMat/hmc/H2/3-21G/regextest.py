with open('H2.com.log', 'r') as data_file:
    for i, line in data_file.readlines():
        if 'Orbital energies' in line:
