"""contacts = {"Alice" : "123-456-7890","Bob" : "945-879-1230", "Carol" : "136-275-2985"}

flag = True

while flag:
 
 r1 = int(input("You want to add a new contact? 1 if yes 0 if not"))
 
 if r1==1:
  
  rKey = input("Enter the name: ")
  rValue = input("Enter the number: ")

  #Comprobation
  for key,value in contacts.items():
   if rKey == key:
    print("Already registered")
    flag = False
    break
   
  contacts [rKey] = rValue
  print("Registered!! \n", print(contacts.items()))   
 else:
  print("bye") 
  flag=False """
  
   #---------------------------------------------------------------

set1 = {6, 8, 3, 5}
set2 = {1, 6, 7, 3, 4}
union = set1.union(set2)

intersection = set1.intersection(set2)
print(union)

print(intersection)
  
