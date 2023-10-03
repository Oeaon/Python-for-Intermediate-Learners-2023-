
myFile= open("student.txt","w")

myFile.write("Hello World!")

myFile.write("Angel")
myFile.write("Anthony")
myFile.write("John")

a=0
while a<3:
    
    a1 = input("Write a name: ")
    myFile.write(a1)
    a+=1


myFile.close()