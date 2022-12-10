#file write

'''file=open('E:\demo\demofile.txt','w')
file.write('this is the 1st page on the web \n')
file.write('this is the 2nd page on the web site\n')
file.close()'''

#file read only

'''file=open('E:\demo\demofile.txt','r')
print(file.read(10))
file.close ()'''

#append the file 

'''file =open('E:\demo\demofile.txt','a')
file.write("this is the 3rd line\n ")
file.close()'''

#read mode loop all daata 
file =open('E:\demo\demofile.txt','r')
for l in file:
    print (l)
file.close()
