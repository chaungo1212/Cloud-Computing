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
            
command_inputFile = "input-sample-1.txt"
with open(command_inputFile) as c:
    content = c.read().splitlines()
    
logging.basicConfig(filename='aggiestack-log.txt ', level=logging.INFO, format='%(asctime)s %(name)s %(message)s', filemode='w')

table_hardware = {}
table_rack = {}
table_img = {}
table_flavor = {}

current_hardware = {}

for command in content:
    c = command.split(' ')
    a1 = c[0]
    a2 = c[1]
    a3 = c[2]
    if a1 == 'aggiestack':
		l1 = ''.join([a1, ' ', a2])
			##aggiestack config
		if l1 == 'aggiestack config':
			if a3 == '--hardware':
				print('> Show config hardware: ')
				filename  = 'hdwr-config.txt'
				with open(filename) as f:
					content = f.read().splitlines()
					for i in range(1,2):
						data = content[i].split(' ')
						table_rack[data[0]]= data[1] # make table for rack
					for i in range(4, len(content)): # Skip the first line since the first line record the amount except for the data.
						data = content[i].split(' ')
						table_hardware[data[0]] =[data[1], data[2], data[3], data[4],data[5]] # make a table for hardware
						current_hardware = table_hardware

			elif a3 == '--images':
				print('> Show config images: ')
				filename  = "image-config.txt"  
				with open(filename) as f:
					content = f.read().splitlines()
					for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
						data = content[i].split(' ')
						table_img[data[0]] = [data[1],data[2]] 
			elif a3 == '--flavors':
				print('> Show config flavors: ')
				filename  = "flavor-config.txt"  
				with open(filename) as f:
					content = f.read().splitlines()
					for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
						data = content[i].split(' ') 
						table_flavor[data[0]] =[data[1], data[2], data[3]] 		   
			else:
				sys.stderr.write("Error: File does not exist\n")
				logging.info(str(c) + " Failure")
		##aggiestack server
		elif l1 == 'aggiestack server':
			if a3 == 'create':
				print ('>show create')
			elif a3 == 'delete':
				print ('>Show delete')
			elif a3 == 'list':
				print ('>Show lists')
			else:
				sys.stderr.write("Error: File does not exist\n")
		##aggiestack admin
		elif l1 == 'aggiestack admin':
			a4 = c[3]
			l2 = ''.join([a3, ' ', a4])
			if l2 == 'show hardware':
				print('> Show hardware: ')
				printDict(table_hardware)
			elif l2 == 'show instances':
				print('> Show instances: ')
			else:
				sys.stderr.write("Error: File does not exist\n")
		 ## aggiestack show
		elif l1 == 'aggiestack show':
			if a3 == 'hardware':
				print("> Show hardware: ")
				printDict(table_hardware)
			elif a3 == 'images':
				print('> Show images: ')
				printDict(table_img)
			elif a3 == 'flavors':
				print('> Show flavors: ')
				printDict(table_flavor)
			else:
				sys.stderr.write("Error: File does not exist\n")
		else:
			sys.stderr.write("Error: File does not exist\n")
    else: 
        sys.stderr.write("Error: File does not exist. (Command begin with aggiestack)\n")