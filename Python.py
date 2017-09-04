import sys
import logging

command_inputFile = "CLI.txt"
with open(command_inputFile) as c:
    content = c.read().splitlines()
    
logging.basicConfig(filename='aggiestack-log.txt ', level=logging.INFO, format='%(asctime)s %(name)s %(message)s', filemode='w')

for command in content:
    #print(command)
    c = command.split(' ')
    a1 = c[0]

    a2 = c[1]

    a3 = c[2]

    l1 = ''.join([a1, ' ', a2])
    #logger1 = logging.getLogger(str(c))
    if l1 == 'aggiestack config':
  
        if a3 == '--hardware':
            sys.stdout.write('hardware\n')
            filename  = 'hdwr-config.txt'
            with open(filename) as f:
                content = f.readlines();
            #logger1.info('Successful')
            logging.info(str(c) + ' Successful')
            #logging.basicConfig(filename='aggiestack-log.txt ', level=logging.INFO)
            #logging.info("Successful")
            #logging.info("aggiestack config --hardware hdwr-config.txt")
        elif a3 == '--images':
            sys.stdout.write('image\n')
            filename  = "image-config.txt"  
            with open(filename) as f:
                content = f.readlines();
            logging.info(str(c) + ' Successful')
        elif a3 == '--flavors':
            sys.stdout.write('flavor\n')
            filename  = "flavor-config.txt"  
            with open(filename) as f:
                content = f.readlines();
            logging.info(str(c) + ' Successful')                    
        else:
            sys.stderr.write("Error: Cannot find the command\n")
            logging.info(str(c) + " Failure")
 
    elif l1 == 'aggiestack show':
        print(a3)
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
    else:
        sys.stderr.write("Error: Cannot find the command\n")
        logging.info(str(c) + ' Failure')
