tmp=int(input("enter amount of numbers to be stored:"))#inputing a value to determin list length
list= [0] * tmp#creating a list
for i in range (tmp):#looping to input the list
     tmp2=int(input("enter integer:"))#inputing the value to a temporary variable tmp2
     list[i]=tmp2#storing the value in temporaru variable to list
i=0#reinitialising the varibale to reuse on another loop
for i in range (tmp):#looping to output inital list of numbers
     print(list[i])#outputing inital list of numbers
i=0#reinitialising the varibale to reuse on another loop
for i in range (tmp-1):#looping to perform bubble sort
    j=i#initalising j to 0 to loop
    for j in range (tmp-i-1):
        if(list[j]>list[j+1]):#test to see if swap is required
            tmp2=list[j+1]#swapping
            list[j+1]=list[j]
            list[j]=tmp2
i=0#reinitialising the varibale to reuse on another loop
for i in range (tmp):#looping to print sorted list
    print(list[i])#printing sorted list
