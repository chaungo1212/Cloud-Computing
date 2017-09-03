import sys
#first command
command_1 = 'aggiestack config --hardware hdwr-config.txt'.split(' ')

a1 = command_1[0]

a2 = command_1[1]

a3 = command_1[2]

a4 = command_1[3]

#print (a1)

#print (a2)

#print (a3)

l1 = ''.join([a1, ' ', a2])

print (l1)


if l1 == 'aggiestack config':
  
    if a3 == '--hardware':
    
        sys.stdout.write('hardware\n')
        
##second command
command_2 = 'aggiestack config --images image-config.txt'.split(' ')

b1 = command_2[0]

b2 = command_2[1]

b3 = command_2[2]

b4 = command_2[3]

#print (b1)

#print (b2)

#print (b3)

l2 = ''.join([a1, ' ', a2])

print (l2)


if l2 == 'aggiestack config':
  
    if b3 == '--images':
    
        sys.stdout.write('image\n')


##third command
command_3 = 'aggiestack config --flavors flavor-config.txt'.split(' ')

c1 = command_3[0]

c2 = command_3[1]

c3 = command_3[2]

c4 = command_3[3]

#print (b1)

#print (b2)

#print (b3)

l3 = ''.join([a1, ' ', a2])

print (l3)


if l3 == 'aggiestack config':
  
    if c3 == '--flavors':
    
        sys.stdout.write('flavor\n')

   
##fourth command
command_4 = 'aggiestack show hardware'.split(' ')

d1 = command_4[0]

d2 = command_4[1]

d3 = command_4[2]

l4 = ' '.join([d1 ,d2])
print(l4)
if l4 == 'aggiestack show':
  
    if d3 == 'hardware':
    
        sys.stdout.write('show hardware\n')


##fifth command
command_5 = 'aggiestack show images '.split(' ')

e1 = command_5[0]

e2 = command_5[1]

e3 = command_5[2]

l5 = ' '.join([e1 ,e2])
print(l5)
if l5 == 'aggiestack show':
  
    if e3 == 'images':
    
        sys.stdout.write('show images\n')
        
        
##sixth command
command_6 = 'aggiestack show flavors '.split(' ')

f1 = command_6[0]

f2 = command_6[1]

f3 = command_6[2]

l6 = ' '.join([f1 ,f2])
print(l6)
if l6 == 'aggiestack show':
  
    if f3 == 'flavors':
    
        sys.stdout.write('show flavors\n')



##seventh command
command_7 = 'aggiestack show all '.split(' ')

g1 = command_7[0]

g2 = command_7[1]

g3 = command_7[2]

l7 = ' '.join([g1 ,g2])
print(l6)
if l7 == 'aggiestack show':
  
    if g3 == 'all':
    
        sys.stdout.write('show all\n')
