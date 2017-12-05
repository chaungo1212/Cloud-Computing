import sys
import logging

table_hardware = {}
table_rack = {}
table_img = {}
table_flavor = {}
current_hardware = {}
table_instance = {}
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
	
def can_host(table_hardware, table_rack, table_image, table_flavor, hardware, image, flavor):
	rack = table_hardware[hardware][0]
	remainCapacity = int(table_rack[rack][0])
	imgSize = int(table_image[image][0])
	if imgSize <= remainCapacity:
		avail_mem = int(table_hardware[hardware][2]) # available mem
		avail_ndisks = int(table_hardware[hardware][3]) # available num-disks
		avail_nvcpus = int(table_hardware[hardware][4]) # available num-vcpus
		flav_mem = int(table_flavor[flavor][0])
		flav_ndisks = int(table_flavor[flavor][1])
		flav_nvcpus = int(table_flavor[flavor][2])
		if avail_mem >= flav_mem and avail_ndisks >= flav_ndisks and avail_nvcpus >= flav_nvcpus:
			return hardware
	return "Fail"
	
command_inputFile = "input-sample-1.txt"
with open(command_inputFile) as c:
    content = c.read().splitlines()           
    
logging.basicConfig(filename='aggiestack-log.txt ', level=logging.INFO, format='%(asctime)s %(name)s %(message)s', filemode='w')

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
					for i in range(1,3):
						data = content[i].split(' ')
						table_rack[data[0]]= [data[1]] # make table for rack
					for i in range(4, len(content)): # Skip the first line since the first line record the amount except for the data.
						data = content[i].split(' ')
						table_hardware[data[0]] =[data[1], data[2], data[3], data[4],data[5]] # make a table for hardware
						current_hardware = table_hardware
				print('Write into log file')
				logging.info(str(c) + ' Successful') 
			elif a3 == '--images':
				print('> Show config images: ')
				filename  = "image-config.txt"  
				with open(filename) as f:
					content = f.read().splitlines()
					for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
						data = content[i].split(' ')
						table_img[data[0]] = [data[1],data[2]]
				print('Write into log file')						
				logging.info(str(c) + ' Successful') 
			elif a3 == '--flavors':
				print('> Show config flavors: ')
				filename  = "flavor-config.txt"  
				with open(filename) as f:
					content = f.read().splitlines()
					for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
						data = content[i].split(' ') 
						table_flavor[data[0]] =[data[1], data[2], data[3]]
				print('Write into log file')
				logging.info(str(c) + ' Successful') 
			else:
				sys.stderr.write("Error: File does not exist\n")
				logging.info(str(c) + " Failure")
		##aggiestack server
		elif l1 == 'aggiestack server':
			if a3 == 'create':
				print ('>show server create')
				a4 = c[3] # --image
				a5 = c[4] # IMAGE
				a6 = c[5] # --flavor	
				a7 = c[6] # FLAVOR_NAME
				a8 = c[7] #INSTANCE_NAME
				for hardware in table_hardware:
					Result = can_host(table_hardware, table_rack, table_img, table_flavor, hardware, a5, a7)
					if Result != "Fail": # There exists a machine to host the virtual server. 
						table_instance[a8] = [a5, a7, Result] # Create instance
						imgSize = int(table_img[a5][0]) # Update corresponding rack's capacity.
						remain_capacity = int(table_rack[table_hardware[Result][0]][0])
						remain_capacity = remain_capacity - imgSize
						table_rack[table_hardware[Result][1]] = str(remain_capacity)
						remain_mem = int(table_hardware[Result][2]) # Upate the machine's info. # available mem
						remain_ndisks = int(table_hardware[Result][3]) # available num-disks
						remain_nvcpus = int(table_hardware[Result][4]) # available num-vcpus
						remain_mem = remain_mem - int(table_flavor[a7][0])
						remain_ndisks = remain_ndisks - int(table_flavor[a7][1])
						remain_nvcpus = remain_nvcpus - int(table_flavor[a7][2])
						table_hardware[Result][2] = str(remain_mem)
						table_hardware[Result][3] = str(remain_ndisks)
						table_hardware[Result][4] = str(remain_nvcpus)
						print('> Instance name: '+a8)
						print('> Image name: '+ a5)
						print('> Flavor name: ' +a7)
						print('> Hardware name:' + Result)
						print('>Successfully create instance name')
						break
					#logging.info(str(c) + ' Successful') 	
				else:
					print('>Failed to create instance name')
			elif a3 == 'delete':
				print('> Show server delete: ')
				a4 = c[3] # INSTANCE_NAME
				if a4 in table_instance.keys():
					imgName = table_instance[a4][0]
					flavorName = table_instance[a4][1]
					machineName = table_instance[a4][2]
					avail_capacity = int(table_rack[table_hardware[machineName][0]][0]) # Update the capacity of the rack.
					imgSize = int(table_img[imgName][0])
					avail_capacity = avail_capacity + imgSize
					table_rack[table_hardware[machineName][0]][0] = str(avail_capacity)
					avail_mem = int(table_hardware[machineName][2]) # Upate the machine's info. 
					avail_ndisks = int(table_hardware[machineName][3]) 
					avail_nvcpus = int(table_hardware[machineName][4])
					avail_mem = avail_mem + int(table_flavor[flavorName][0])
					avail_ndisks = avail_ndisks + int(table_flavor[flavorName][1])
					avail_nvcpus = avail_nvcpus + int(table_flavor[flavorName][2])
					table_hardware[machineName][2] = str(avail_mem)
					table_hardware[machineName][3] = str(avail_ndisks)
					table_hardware[machineName][4] = str(avail_nvcpus)
					del table_instance[a4]
					print('Successfully delete instance_name ')
					logging.info(str(c) + ' Successful') 
				else:
					print('Failed to delete instance_name')
			elif a3 == 'list':
				print ('>Show server lists')
				sys.stdout.write('----------------------------------\n')
				sys.stdout.write("#" + str(len(table_instance)) + "\n")
				for instancename in table_instance:
					sys.stdout.write(instancename + ' ')
					list = table_instance[instancename]
					for i in range(0,len(list)-1):
						sys.stdout.write(str(list[i] + " "))
					sys.stdout.write("\n")
				sys.stdout.write('----------------------------------\n')
				logging.info(str(c) + ' Successful') 
			else:
				sys.stderr.write("Error: File does not exist\n")
		##aggiestack admin
		elif l1 == 'aggiestack admin':
			a4 = c[3]
			l2 = ''.join([a3, ' ', a4])
			if l2 == 'show hardware':
				print('> Admin hardware: ')
				printDict(table_rack)
				printDict(table_hardware)
			elif l2 == 'show instances':
				print('> Admin show instances: ')
				sys.stdout.write('----------------------------------\n')
				sys.stdout.write("#" + str(len(table_instance)) + "\n")
				for instancename in table_instance:
					sys.stdout.write(instancename + ' ')
					list = table_instance[instancename]
					sys.stdout.write(str(list[len(list)-1] + "\n"))
				sys.stdout.write('----------------------------------\n')
				logging.info(str(c) + ' Successful') 
			elif a3 == 'evacuate':
				print('>Admin evacuate RACK_NAME: ' + a4)
				for instancename in table_instance:
					hardwarename = table_instance[instancename][2]
					if table_hardware[hardwarename][0] == a4: # The instance need to move to other rack.
						image = table_instance[instancename][0]
						flavor = table_instance[instancename][1]
						can_move = False
						for desthardware in table_hardware:
							if table_hardware[desthardware][0]!= a4:
								Result = can_host(table_hardware, table_rack, table_img, table_flavor, desthardware, image, flavor)
								if Result != "Fail": # Move this instance to the result hardware
									table_instance[instancename][2] = Result # Update the instance location for the hardware
									table_rack[table_hardware[Result][0]][0] = str(int(table_rack[table_hardware[Result][0]][0]) - int(table_img[image][0])) # Update the chosen rack's capacity
									table_hardware[Result][2] = str(int(table_hardware[Result][2]) - int(table_flavor[flavor][0]))
									table_hardware[Result][3] = str(int(table_hardware[Result][3]) - int(table_flavor[flavor][1]))
									table_hardware[Result][4] = str(int(table_hardware[Result][4]) - int(table_flavor[flavor][2]))
									can_move = True
									sys.stdout.write(instancename + ": Move to hardware-" + Result + " on rack-" + table_hardware[Result][0] + ".\n")
									break
						if can_move == False:
							sys.stdout.write(instancename + ": Can not find any rack or hardware to allocate.\n")
			elif a3 == 'remove':
				print ('>Admin remove MACHINE:')
			elif a3 == 'add':
				print('>Admin add:')
			else:
				sys.stderr.write("Error: File does not exist\n")
		 ## aggiestack show
		elif l1 == 'aggiestack show':
			if a3 == 'hardware':
				print('> Show hardware: ')
				printDict(table_rack)
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
