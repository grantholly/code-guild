#this file object called output will be created in write mode
output = open("/home/grant/spam.txt", "w")

#this file object is created in read mode
input = open("/home/grant/data.txt", "r")

#this objects will store the entire contents of input as a string
#passing a number to .read() like .read(10) will read only
#the top 10 lines from the file
my_file = input.read()

#this variable will store the first line of the input file
#files are iterable objects, so the next call to .readline
#will return the next line in the file
single_line = input.readline()

for line in input:
    print(line)

#here the output file will write and save the string
#created by single_line 
output.write(single_line)

output.write("this line came from Python")

#this will allow you pass in a python object to be saved in output
output.write("this value is from python: %s") % X

#similar to .readlines(), .writelines() can be used with looping
#to send data into a file to be saved by the file system

#this will wipe out the data in memory for the file object
output.close()

#this will wipe out the data in memory without closing the file
output.flush()

