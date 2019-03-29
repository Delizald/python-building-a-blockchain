input('Please enter your name: ')
my_name = input('Please enter your name: ')

file = open('name.txt', mode='w')
file
file.write(my_name)
file.close()
file = open('name.txt',mode ='r')
file.read()