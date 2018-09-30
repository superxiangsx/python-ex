#from sys import argv

#read and print the file you typed

#The fisrt method start
'''
print("Type the file name:", end = '')
filename = input()
txt = open(filename)
print("Here's your file:")
print(txt.read())
txt.close()
'''
#The first method stop

#The sencond method start

txt = open(input("Type the file name here:"))   #open the file you typed
print("Here's your file:")
print(txt.read())   #read the file you typed, and print it
txt.close() #close the file

#The second method stop

#The third method start
#print(open(input("Type the file name here:")).read())
# How can I close the file??
