list= [""] * 12 #creating a list to store 12 strings
for i in range (12):#looping to input 
    str1=input("enter name:")
    list[i]=str1#assiging the string to the list
i=0#re-initialising the varibale i to reuse it on another loop
for i in range (10):#looping to concanate
    strr=list[i]+list[1+i]+list[i+2]#joining the stings
    l=len(strr)-1#cheaking for the length of the string
    str2=""
    while (l>=0):
       str2+=strr[l]
       l=l-1
    if(strr==str2):
       print("palindrome")
    else:
       print("not palindrome")
