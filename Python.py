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
    
    if a1 == 'aggiestack':
        l1 = ''.join([a1, ' ', a2])
        ##aggiestack config
        if l1 == 'aggiestack config':
            if a3 == '--hardware':
                filename  = 'hdwr-config.txt'
                with open(filename) as f:
                    content = f.read().splitlines()
                    for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
                        data = content[i].split(' ')
                        table_hardware[data[0]] =[data[1], data[2], data[3], data[4]] # make a table for hardware
                        current_hardware = table_hardware
                    logging.info(str(c) + ' Successful') 

            elif a3 == '--images':
                filename  = "image-config.txt"  
                with open(filename) as f:
                    content = f.read().splitlines()
                    for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
                        data = content[i].split(' ')
                        table_img[data[0]] = [data[1]] 
                logging.info(str(c) + ' Successful')
                
            elif a3 == '--flavors':
                filename  = "flavor-config.txt"  
                with open(filename) as f:
                    content = f.read().splitlines()
                    for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
                        data = content[i].split(' ') 
                        table_flavor[data[0]] =[data[1], data[2], data[3]] 
                logging.info(str(c) + ' Successful') 
                                   
            else:
                sys.stderr.write("Error: File does not exist\n")
                logging.info(str(c) + " Failure")
        ## aggiestack show
        elif l1 == 'aggiestack show':
            if a3 == 'hardware':
                print("> Show hardware: ")
                printDict(table_hardware)
                logging.info(str(c) + ' Successful')
            elif a3 == 'images':
                print('> Show images: ')
                printDict(table_img)
                logging.info(str(c) + ' Successful')
            elif a3 == 'flavors':
                print('> Show flavors: ')
                printDict(table_flavor)
                logging.info(str(c) + ' Successful')
            elif a3 == 'all':
                print('> Show all: ')
                print('--Hardware: ')
                printDict(table_hardware)
                print('--Image: ')
                printDict(table_img)
                print('--Flavor: ')
                printDict(table_flavor)
                logging.info(str(c) + ' Successful')
            else:
                sys.stderr.write("Error: File does not exist\n")
                logging.info(str(c) + " Failure")
        ## aggiestack admin
        elif l1 == 'aggiestack admin':
            if a3 == 'show':
                print('> Admin show hardware')
                printDict(current_hardware)
                logging.info(str(c) + ' Succesful ')
            elif a3 == 'can_host':
                a4 = c[3] # machine name
                a5 = c[4] # flavor name
                if current_hardware.get(a4) == None:
                    logging.info(str(c) + "Failure")
                    continue
                if table_flavor.get(a5) == None:
                    logging.info(str(c) + "Failure")
                    continue
                avail_mem = int(current_hardware[a4][1]) # available mem
                avail_ndisks = int(current_hardware[a4][2]) # available num-disks
                avail_nvcpus = int(current_hardware[a4][3]) # available num-vcpus
                flav_mem = int(table_flavor[a5][0])
                flav_ndisks = int(table_flavor[a5][1])
                flav_nvcpus = int(table_flavor[a5][2])
                if avail_mem >= flav_mem and avail_ndisks >= flav_ndisks and avail_nvcpus >= flav_nvcpus:
                    logging.info(str(c) + "Success")
                    sys.stdout.write(str(a4) + " can host " + str(a5) + "?: Yes\n")
                    print('----------------------------------')
                else:
                    logging.info(str(c) + "Failure")
                    sys.stderr.write("Error: " + a4 + " can not host " + a5 + " flavor\n") 
                    
        else:
            sys.stderr.write("Error\n")
            logging.info(str(c) + ' Failure')
            
    else: 
        sys.stderr.write("Error: File does not exist. (Command begin with aggiestack)\n")
        logging.info(str(c) + ' Failure')
