

#rewrite an file
txt = open(input("Type the file name here:"), 'w')   #open the file you typed

txt.truncate() #delete content of the file

l1 = input("line1:")
l2 = input("line2:")
l3 = input("line3:")
txt.write(l1 + "\n" + l2 + "\n" + l3)
print("Writing completed, and here is the new file:")
txt = open("ex13_sample.txt")
print(txt.read())

txt.close() #close the file