size= int(input("Enter size of set 1 : "))
size1= int(input("Enter size of set 2 : "))
print("\nFor set 1:")
list1=[]
for _ in range(size):
   element=int(input("enter elements:"))
   list1.append(element)
print("set 1=",list1)

print("\nFor set 2:")
list2=[]
for _ in range(size1):
   element=int(input("enter elements:"))
   list2.append(element)
print("set 2=",list2)

choice=0
while choice!=10:
 print("\n____________________________")
 print("**************MENU***********")
 print("1.add")
 print("2.remove")
 print("3.contains")
 print("4.size")
 print("5.intersection")
 print("6.union")
 print("7.Difference")
 print("8.Subset")
 print("9.Proper Subset")
 print("10.Exit")
 print("_____________________________\n")

 choice=int(input("enter choice:"))
 print()

 if choice==1:
  e=int(input("enter number to add:"))
  list1.append(e)
  print("set 1",list1)
 elif choice==2:
  e=int(input("enter number to remove"))
  if e in list1:
   list1.remove(e)
   print("set 1=",list1)
  else:
    print(e,"is not in set 1!!")

 elif choice==3:
  e=int(input("enter number to search in set 1:"))
  if e in list1:
   print("number present in set 1")
  else:
   print("number is not present in set1!!")
  print("set1=",list1)

 elif choice==4:
  print("set 1 contains{} elements!!".format(len(list1)))

 elif choice==5:
  list3=[element for element in list1 if element in list2]
  print("set 1",list1)
  print("set2 ",list2)
  print("Intersection",list3)

 elif choice==6:
  list3=list1.copy()
  for element in list2:
    if element not in list1:
       list3.append(element)
  print("set 1",list1)
  print("set2 ",list2)
  print("Union",list3)

 elif choice==7:
   list3=[element for element in list1 if element not in list2]
   print("set 1",list1)
   print("set2 ",list2)
   print("set1-set2",list3)

 elif choice==8:
  print("set 1",list1)
  print("set2 ",list2)

  def sub():
    flag=0
    for e in list2:
      if e not in list1:
        flag=1
    if flag==1:
       print("set 2 is not a subset of set1!!")
    else:
       print("set 2 is a subset of set1")
  sub()

 elif choice==9:
    print("set 1",list1)
    print("set2 ",list2)
    if sorted(list1)==sorted(list2):
       print("set 2 is a proper subset of set1")
    else:
       print("set 2 is a not proper a subset of set1")



 elif choice==10:
  print("Thanks for using this program...!!!")
  break  
 elif choice<1 or choice>10:
  print("plz enter a valid choice!!") 