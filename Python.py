import sys
import logging
    
#image data check again pls!!!!!!!!!!!!!!!!!!!!!!
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
        #logger1 = logging.getLogger(str(c))
        if l1 == 'aggiestack config':
            if a3 == '--hardware':
                sys.stdout.write('hardware\n')
                filename  = 'hdwr-config.txt'
                with open(filename) as f:
                    content = f.read().splitlines()
                    for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
                    #print(content[i])
                        data = content[i].split(' ')
                        table_hardware[data[0]] =[data[1], data[2], data[3], data[4]] 
                        #logger1.info('Successful')
                        current_hardware = table_hardware
                    logging.info(str(c) + ' Successful')
                        #logging.basicConfig(filename='aggiestack-log.txt ', level=logging.INFO)
                        #logging.info("Successful")
                        #logging.info("aggiestack config --hardware hdwr-config.txt")
            elif a3 == '--images':
                sys.stdout.write('image\n')
                filename  = "image-config.txt"  
                with open(filename) as f:
                    content = f.read().splitlines()
                    for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
                    #print(content[i])
                        data = content[i].split(' ')
                        table_img[data[0]] =data[1] 
                logging.info(str(c) + ' Successful')
            elif a3 == '--flavors':
                sys.stdout.write('flavor\n')
                filename  = "flavor-config.txt"  
                with open(filename) as f:
                    content = f.read().splitlines()
                    for i in range(1, len(content)): # Skip the first line since the first line record the amount except for the data.
                    #print(content[i])
                        data = content[i].split(' ')
                        table_flavor[data[0]] =[data[1], data[2], data[3]] 
                logging.info(str(c) + ' Successful')                    
            else:
                sys.stderr.write("Error: Cannot find the command\n")
                logging.info(str(c) + " Failure")
 
        elif l1 == 'aggiestack show':
            if a3 == 'hardware':
                sys.stdout.write('show hardware\n')
                logging.info(str(c) + ' Successful')
            elif a3 == 'images':
                sys.stdout.write('show images\n')
                logging.info(str(c) + ' Successful')
            elif a3 == 'flavors':
                sys.stdout.write('show flavors\n')
                logging.info(str(c) + ' Successful')
            elif a3 == 'all':
                sys.stdout.write('show all\n')
                logging.info(str(c) + ' Successful')
            else:
                sys.stderr.write("Error: Cannot find the command\n")
                logging.info(str(c) + " Failure")
        elif l1 == 'aggiestack admin':
            #print("Debug "+a3)
            if a3 == 'show':
                print('admin')
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
                    sys.stdout.write("Yes\n")
                else:
                    logging.info(str(c) + "Failure")
                    sys.stderr.write("Error: " + a4 + " can not host " + a5 + " flavor\n") 
        else:
            sys.stderr.write("Error: Cannot find the command\n")
            logging.info(str(c) + ' Failure')
            
    else: 
        sys.stderr.write("Error: Cannot find the command\n")
        logging.info(str(c) + ' Failure')
