import sys
import logging

def printDict(dict):
    sys.stdout.write('----------------------------------\n')
    sys.stdout.write("#" + str(len(dict)) + "\n")
    for key in dict:
        sys.stdout.write(key + ' ')
        list = dict[key]
        for i in range(len(list)):
            sys.stdout.write(str(list[i] + " "))
        sys.stdout.write("\n")
    sys.stdout.write('----------------------------------\n')
            
command_inputFile = "CLI.txt"
with open(command_inputFile) as c:
    content = c.read().splitlines()
    
logging.basicConfig(filename='aggiestack-log.txt ', level=logging.INFO, format='%(asctime)s %(name)s %(message)s', filemode='w')

table_hardware = {}
table_img = {}
table_flavor = {}
current_hardware = {}

for command in content:
    c = command.split(' ')
    a1 = c[0]
    a2 = c[1]
    a3 = c[2]
	a4 = c[3]
    
	if a1 == 'aggiestack':
		l1 = ''.join([a1, ' ', a2])
		##aggiestack server
		if l1 == 'aggiestack server':
			if a3 == 'create':
				print('> Show create: ')
			elif a3 == 'delete':
				print('> Show delete: ')
			elif a3 == 'list':
				print('> Show all instances running list: ')
			else:
				sys.stderr.write("Error: File does not exist\n")
				logging.info(str(c) + " Failure")
        ## aggiestack admin
        if l1 == 'aggiestack admin':
		#	l2 = ''.join([a3, ' ', a4])
            if a3 == 'show hardware':
                print('> Admin show hardware')
                printDict(current_hardware)
                logging.info(str(c) + ' Succesful ')
			elif a3 == 'show instances':
				print('> Admin show instances')
			else:
				sys.stderr.write("Error\n")
				logging.info(str(c) + ' Failure')
		else: 
		sys.stderr.write("Error: File does not exist. (Command begin with aggiestack)\n")
		logging.info(str(c) + ' Failure')
    else: 
		sys.stderr.write("Error: File does not exist. (Command begin with aggiestack)\n")
		logging.info(str(c) + ' Failure')