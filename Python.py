import sys
import logging

command_inputFile = "CLI.txt"
with open(command_inputFile) as c:
    #content = c.readlines()
    content = c.read().splitlines()
    
#c = content[0].split(' ')
#print(c[0])
for command in content:
    print(command)
    c = command.split(' ')
    a1 = c[0]

    a2 = c[1]

    a3 = c[2]

    l1 = ''.join([a1, ' ', a2])

    if l1 == 'aggiestack config':
  
        if a3 == '--hardware':
            #sys.stdout.write('hardware\n')
            filename  = "hdwr-config.txt"
            with open(filename) as f:
                content = f.readlines();
              #  for line in content:
                  #  print(line)
        elif a3 == '--images':
            #sys.stdout.write('image\n')
            filename  = "image-config.txt"  
            with open(filename) as f:
                content = f.readlines();
           #     for line in content:
                  #  print(line)

        elif a3 == '--flavors':
            #sys.stdout.write('flavor\n')
            filename  = "flavor-config.txt"  
            with open(filename) as f:
                content = f.readlines();
              #  for line in content:
                  #  print(line)
                    
        else:
            print('error1')
 
    elif l1 == 'aggiestack show':
        print(a3)
        if a3 == 'hardware':
            print('1')
        #    sys.stdout.write('show hardware\n')
        elif a3 == 'images':
            print('2')
        #    sys.stdout.write('show images\n')
        elif a3 == 'flavors':
            print('3')
         #   sys.stdout.write('show flavors\n')
        elif a3 == 'all':
            print('34')
        #    sys.stdout.write('show all\n')
        else:
            print('error2')
    else:
        print('error3')
