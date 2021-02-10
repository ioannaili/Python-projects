"""
This is a function called maxDistance that takes as input a list of distances and a positive integer.
The function returns the largest sum of items in the list so that they do not exceed the integer passed as the second argument.
"""
def maxDistance(a,num):
    
  maxSum=0
  maxtemp=0

  for i in range(len(a)):
  
        maxtemp=maxSum+a[i]
        if (maxtemp<num):
          maxSum=maxtemp
          maxtemp=0
        elif (maxtemp>num):
            maxtemp=0
            continue
        
        
  return maxSum
        
     

a=[]
size=int(input("Enter list length: "))
print("Enter distances: ")
for i in range(size): 
    data=int(input())
    a.append(data)
num=int(input("Enter number: "))
a.sort(reverse=True)
maxsu=maxDistance(a,num)
print(maxsu)


